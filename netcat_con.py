from telnetlib import Telnet
import sys
import binascii

HOST = 'skillz.baectf.com'
PORT = 31387
PASSWORD = "avenue"


def solve_challenge(host, port, password):
	tn = Telnet(host, port)
	# Password challenge/response
	data = tn.read_until(": ")
	print data
	tn.write(password + "\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	num1= int(tn.read_until(" "))
	print num1
	num2= int(tn.read_until(" "))
	print num2
	num3= int(tn.read_until(" "))
	print num3
	num4= int(tn.read_until(" "))
	print num4
	s=num1+num2+num3+num4
	print s
	tn.write(str(s)+ "\n")
	message=tn.read_until("\n")
	print message

	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")
	print tn.read_until("\n")

    
 	st=(tn.read_some())
 	print st
 	a1 = ord(st[0])+(ord(st[1])<<8)+(ord(st[2])<<16)+(ord(st[3])<<24)
 	print a1
	a2 = ord(st[4])+(ord(st[5])<<8)+(ord(st[6])<<16)+(ord(st[7])<<24)
	print a2	
	a3 = ord(st[8])+(ord(st[9])<<8)+(ord(st[10])<<16)+(ord(st[11])<<24)
	print a3
	a4 = ord(st[12])+(ord(st[13])<<8)+(ord(st[14])<<16)+(ord(st[15])<<24)
	print a4

	a=a1+a2+a3+a4
	print a

	r = chr(a&((1<<8)-1)) + chr((a>>8)&((1<<8)-1)) + chr((a>>16)&((1<<8)-1)) + chr((a>>24)&((1<<8)-1))
	print r

	tn.write(r)
 	print tn.read_some()
 	print tn.read_some()
 	print tn.read_some()


	print tn.read_until("")
	print tn.read_until("")
	print tn.read_until("")
	print tn.read_until("")

	





	tn.close()


if __name__ == "__main__":
    solve_challenge(HOST, PORT, PASSWORD)
        