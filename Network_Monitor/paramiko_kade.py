import paramiko
import time

def connect(server_ip, server_port, user, passwd):
    ssh_client= paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd, 
                 look_for_keys=False, allow_agent=False)
    return ssh_client

#conntect(192.168.10.101, 403, cisco, cisco123!)

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command):
    print(f'Sendingcommand: {command}')
    shell.send(command  + '\n')
    #time.sleep(timeout)

def show(shell, command, n=10000, timeout = 1):
#    print(f'Sendingcommand: {command}')
#    shell.send('show ip interface brief\n')
    shell.send('enable'  + '\n')
    shell.send(command  + '\n') 
    time.sleep(timeout)
    output1 = shell.recv(n)
    output = output1.decode('utf-8')

    return output

def close(ssh_client):
        if  ssh_client.get_transport().   is_active() == True:
            print('Closing connection')
            ssh_client.close()