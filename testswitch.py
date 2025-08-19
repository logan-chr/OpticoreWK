import netmiko
from netmiko import ConnectHandler


switch = {
    'device_type':'cisco_ios',
    'host':'10.1.10.240',
    'username':'optiadmin',
    'password':'opt1adm1n',
    'port':22,
    'secret':'opt1adm1n'
}

def shutdown():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    arr = ['configure terminal','interface fastEthernet 0/3','shutdown','exit','logout']
    ssh.send_config_set(arr)
    ssh.disconnect

def noshutdown():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    arr = ['configure terminal','interface fastEthernet 0/3','no shutdown','exit','logout']
    ssh.send_config_set(arr)
    ssh.disconnect()
def peek():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    output = ssh.send_command('show running-config interface fastEthernet 0/3',)
    ssh.disconnect()
    if 'shutdown' in output:
        return False
    else:
        return True


def power():
 
    ssh = ConnectHandler(**switch)
    ssh.enable()
    output = ssh.send_command('show power inline')
    
    print(output)

    
    ssh.disconnect

def run():
    flag = True
    while flag:
        print()
        print('======')
        print('>>>',end='')
        a = input()
        if a == 'on':
            noshutdown()
        elif a =='off':
            shutdown()
        elif a=='peek':
            peek()
        elif a=='power':
            power()
        elif a=='end':
            flag = False
    