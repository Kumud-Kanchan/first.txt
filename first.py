i=0
flag=False
while i<3:
	x=raw_input("Guess the number: ")
	if x=='9':
		 print('you win')
		 break
	elif i==2:
		 print('you lose')
	else:
		 print('try again')
	i+=1 
