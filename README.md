# OpticoreWK
environmental sustainability project
Access points can take like 15.4W of power, so leaving them on all the time can be very confusing.
The purpose of this project is to solve this problem, via the development of automatic commands.
I have used a Rasberry pi 3 which pretty much takes input from a motion sensor, and has the ability to send commands to the switch using the netmiko library.
The access point turns off if there is no motion for 10 minutes and its out of work hours. it can be turned on by the sensor or the command line.
type help to see a list of commands or read them below
n\noff\npeek\npower\nupt (uptime)\nhistory\nclear\ntotal


