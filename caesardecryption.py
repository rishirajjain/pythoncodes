text=raw_input()
c=""
print "hello"
for i in text:
	if i!= ' ':
		c=c+ chr(ord(i)-2)


	else:
		c=c+' '

print c
print "bye!"
 
