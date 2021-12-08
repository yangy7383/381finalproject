import time
import Reconfigure_VPN as R
import Get_VPN_IP as G

# Genie import
from genie.conf import Genie

# import the genie libs
from genie.libs import ops # noqa

# Parser import
from genie.libs.parser.iosxe.show_interface import ShowIpInterfaceBrief

# Import Genie Conf
from genie.libs.conf.interface import Interface

#exit_flag = False
origin_ip = "172.16.0.2"

class MonitorVPN():
    def setup(self, testbed):
        genie_testbed = Genie.init(testbed)
        self.device_list = []
        str = ""
        for device in genie_testbed.devices.values():
            try:
                device.connect()
            except Exception as e:
                print("Failed to establish connection to '{}'".format(
                    device.name))
                str += "\nFailed to establish connection to "+ device.name
            self.device_list.append(device)
        return str

    def learn_interface(self):
        text=""
#        global exit_flag
#        while exit_flag == False:
        global origin_ip
        for dev in self.device_list:
            self.parser = ShowIpInterfaceBrief(dev)
            out = self.parser.parse()
            print(out)
            self.intf1 = []
            # let's find  the interface
            for interface, value in out['interface'].items():
                if (interface == 'GigabitEthernet2') and (origin_ip not in value['ip_address']):
                    newip = value['ip_address']
                    text+="\n"+interface +" on " + dev.name + " has a changed IP causing the VPN to fail."

                    command1 = "no crypto isakmp key cisco address " + origin_ip
                    command2 = "crypto isakmp key cisco address " + newip
                    command3 = "crypto map Crypt 10 ipsec-isakmp"
                    command4 = "no set peer " + origin_ip
                    command5 = "set peer " + newip
                    command6 = "exit"

                    R.branch(command1, command2, command3, command4, command5, command6)
                    text+="\n"+command1+"\n"+command2+"\n"+command3+"\n"+command4+"\n"+command5+"\n"+command6
                    text+="\n"+"The VPN has been reconfigured."   
                    self.intf1.append(Interface(name=interface, device=dev))
                    origin_ip = G.get_ip()
            return text

if __name__ == "__main__":
    # Test Functions
    mon = MonitorInterfaces()
    mon.setup('testbed/router2.yml')
    intfl = mon.learn_interface()
    print(intfl)
