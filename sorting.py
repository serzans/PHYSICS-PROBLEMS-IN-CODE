from telnetlib import Telnet
import sys
import binascii
import numpy as np

HOST = 'skillz.baectf.com'
PORT = 31393
PASSWORD = "ilikenumbers"


boolean_matrix=np.zeros((16,16),dtype=bool)

sort_structure=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def solve_challenge(host, port, password):
	tn = Telnet(host, port)
	# Password challenge/response
	data = tn.read_until(": ")
	print data
	tn.write(password + "\n")

	for m in range(0,10000):
		# Spacer
		print tn.read_until("\n")
		# Number of correct answers
		print tn.read_until("\n")
		# Which is lareger?
		tn.read_until("\n")
		# Number one
		num1= tn.read_until("\n")
		num1=(num1.split(" "))[1]
		print num1
		# Number two
		num2= tn.read_until("\n")
		num2=(num2.split(" "))[1]
		print num2

		for i in range(len(num1)):
			if num1[i]!=num2[i]:
				tn.write('1')
				temp1=num1[i]
				temp2=num2[i]
				break

		print temp1
		print temp2
		
		# Boolean

		# Is value 1 bigger than value 2?
		boolean_value=tn.read_until("\n") == "Enter 1 or 2: Correct"

		# Indices
		j=sort_structure.index(temp1)
		k=sort_structure.index(temp2)

		if boolean_value:
			boolean_matrix[j,k]=True
			boolean_matrix[k,j]=False
		else:
			boolean_matrix[j,k]=False
			boolean_matrix[k,j]=True

	for l in range(0,100):
		# Spacer
		print tn.read_until("\n")
		# Number of correct answers
		print tn.read_until("\n")
		# Which is lareger?
		tn.read_until("\n")
		# Number one
		num1= tn.read_until("\n")
		num1=(num1.split(" "))[1]
		print num1
		# Number two
		num2= tn.read_until("\n")
		num2=(num2.split(" "))[1]
		print num2

		for i in range(len(num1)):
			if num1[i]!=num2[i]:
				temp1=num1[i]
				temp2=num2[i]
				j=sort_structure.index(temp1)
				k=sort_structure.index(temp2)

				if boolean_matrix[j,k]:
					tn.write('1')
				else:
					tn.write('2')
				break

		print temp1
		print temp2

		tn.read_until("\n")

	tn.close()


if __name__ == "__main__":
    solve_challenge(HOST, PORT, PASSWORD)
        