from netmiko import ConnectHandler
import netmiko

router = {'device_type': 'cisco_ios', 'host': '192.168.56.105', 'username': 'cisco','password': 'cisco123!','port': '22', 'secret': 'cisco123!', 'verbose': True}

def branch (command1, command2, command3, command4, command5, command6):
    connection = ConnectHandler(**router)
    prompt = connection.find_prompt()
    if '>' in prompt:
        connection.enable()
    cmd = command1+"\n"+command2+"\n"+command3+"\n"+command4+"\n"+command5+"\n"+command6

    if not connection.check_config_mode(): 
        connection.config_mode()  
    connection.send_config_set(cmd.split('\n'))
    connection.exit_config_mode()  
    connection.disconnect()