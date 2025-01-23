from telnetlib import Telnet
cmd = input('Enter your command: ')
tn = Telnet('192.168.0.100')   # Instantiate a telnet connection specifying the host we want to connect to.
tn.write(b'admin\n')   # The username we are sending
tn.write(b'test123\n')   # The password we are sending
tn.write(b'term length 0\n')   # Sending the cmd 'term length 0'
tn.write(cmd.encode('ascii') + b'\n')   # Prompting for the command we want to enter.
tn.write(b'exit\n')   # CLosing the session.
print(tn.read_all().decode('ascii'))   # Used to print the output and decode from bytes to human readable text.
