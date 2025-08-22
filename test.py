import csv
#This is my only comment in this whole project.
#This file test.py was used to test functions in a safe environment. 
#Pretty much every function or module in the folder once was materialized in this place
import netmiko
from netmiko import ConnectHandler
from dotenv import load_dotenv
import os
import time
load_dotenv()
username = os.getenv('USERNAME')


class switch():
    def __init__(self):
        self.switch = {
        'device_type':'cisco_ios',
        'host':os.getenv('ADDRESS'),
        'username':os.getenv('USERNAME'),
        'password':os.getenv('PASSWORD'),
        'port':22,
        'secret':os.getenv('SECRET')
        }
        ssh = ConnectHandler(**self.switch)
        ssh.enable()
        for i in range(12):
            ssh.send_config_set(['configure terminal','interface fastEthernet0/'+str(i),'no shutdown','exit'])
            ssh.send_command('no shutdown')
        power= ssh.send_command('show power inline  | include on')
        self.port1 = power[4:6]
  
        self.port2 = power[72:74]
        ssh.disconnect


    def shutdown(self):
        ssh = ConnectHandler(**self.switch)
        ssh.enable()
        arr = ['configure terminal','interface fastEthernet 0/'+self.port1,'shutdown','exit','interface fastEthernet 0/'+self.port2,'shutdown','exit','logout']
        ssh.send_config_set(arr)
        ssh.disconnect


    def noshutdown(self):
        ssh = ConnectHandler(**self.switch)
        ssh.enable()
        arr = ['configure terminal','interface fastEthernet 0/'+self.port1,'no shutdown','exit','interface fastEthernet 0/'+self.port2,'no shutdown','exit','logout']
        ssh.send_config_set(arr)
        ssh.disconnect()


    def peek(self): 
        ssh = ConnectHandler(**self.switch)
        ssh.enable()
        output = ssh.send_command('show running-config interface fastEthernet 0/'+self.port1)
        output2 = ssh.send_command('show running-config interface fastEthernet 0/'+self.port2)
        ssh.disconnect()
        if 'shutdown' in output and 'shutdown' in output2:
            return False
        elif 'shutdown' in output2 or 'shutdown' in output:
            if round(time.time())/2 == round(round(time.time())/2):
                print('Warning, only one Access point online. Please reboot')
            return True
        else:
            return True


    def power(self):
 
        ssh = ConnectHandler(**self.switch)
        ssh.enable()
        output = ssh.send_command('show power inline fa0/'+str(self.port1)+' | include auto')
        output2 = ssh.send_command('show power inline fa0/'+str(self.port2)+' | include auto')
        ssh.disconnect
 
        return(float(output[28:32].replace(' ',''))+float(output2[28:32].replace(' ','')))

    

a = switch()
a.power()
a.shutdown()