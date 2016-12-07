def safe_pawns(pawns):
	pawns=list(pawns)
	safe=0
	for i in range(len(pawns)):
		flag=False
		for j in range(len(pawns)):
			if abs(ord(pawns[i][0])-ord(pawns[j][0]))==1 and (int(pawns[i][1])-int(pawns[j][1]))==1:
				flag=True
		if flag:
			safe+=1
	return safe

print safe_pawns({"b4", "d4", "f4", "c3", "e3", "e5", "d2"})
print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
    