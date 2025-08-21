import netmiko
from netmiko import ConnectHandler
from dotenv import load_dotenv
import os
load_dotenv()
username = os.getenv('USERNAME')

switch = {
    'device_type':'cisco_ios',
    'host':os.getenv('ADDRESS'),
    'username':os.getenv('USERNAME'),
    'password':os.getenv('PASSWORD'),
    'port':22,
    'secret':os.getenv('SECRET')
}

def shutdown():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    arr = ['configure terminal','interface fastEthernet 0/3','shutdown','exit','interface fastEthernet 0/5','shutdown','exit','logout']
    ssh.send_config_set(arr)
    ssh.disconnect


def noshutdown():
    print(switch)
    ssh = ConnectHandler(**switch)
    ssh.enable()
    arr = ['configure terminal','interface fastEthernet 0/3','no shutdown','exit','interface fastEthernet 0/5','no shutdown','exit','logout']
    ssh.send_config_set(arr)
    ssh.disconnect()


def peek():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    output = ssh.send_command('show running-config interface fastEthernet 0/3',)
    output2 = ssh.send_command('show running-config interface fastEthernet 0/5',)
    ssh.disconnect()
    if 'shutdown' in output and 'shutdown' in output2:
        return False
    else:
        return True


def power():
 
    ssh = ConnectHandler(**switch)
    ssh.enable()
    output = ssh.send_command('show power inline fa0/3 | include auto')
    output2 = ssh.send_command('show power inline fa0/5 | include auto')
    ssh.disconnect
    return(float(output[28:33].replace(' ',''))+float(output2[28:33].replace(' ','')))

    

