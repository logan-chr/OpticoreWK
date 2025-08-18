import netmiko
from netmiko import ConnectHandler
import pandas as pd

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

def noshutdown():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    arr = ['configure terminal','interface fastEthernet 0/3','no shutdown','exit','logout']
    ssh.send_config_set(arr)
def peek():
    print('peeking')
    ssh = ConnectHandler(**switch)
    ssh.enable()
    output = ssh.send_command('show running-config interface fastEthernet 0/3')
    if 'shutdown' in output:
        print('off')
    else:
        print('on')
    ssh.disconnect


def power():
    print('peeking')
    ssh = ConnectHandler(**switch)
    ssh.enable()
    output = ssh.send_command('show power inline')
    frame = pd.DataFrame(output)
    print(frame)

    
    ssh.disconnect


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
    