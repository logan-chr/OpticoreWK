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

def noshutdown():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    arr = ['configure terminal','interface fastEthernet 0/3','no shutdown','exit','logout']
    ssh.send_config_set(arr)
def peek():
    ssh = ConnectHandler(**switch)
    ssh.enable()
    arr = ['configure terminal','interface fastEthernet 0/3','show running-config interface fastEthernet 0/3','exit','logout']
    ssh.send_config_set(arr)
    

while True:
    a = input()
    if a == 'on':
        noshutdown()
    elif a =='off':
        shutdown()
    elif a=='peek':
        peek()
    