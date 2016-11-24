text=raw_input()
t=""
for i in text:
	if i!= ' ':
		t=t+ chr(ord(i)-2)


	else:
		t=t+' '

print t
 
