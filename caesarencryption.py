text = raw_input()
str=""
for i in text:
	if i!=' ':
		if i=='y':
			str=str+'a'
		elif i=='z':
			str=str+'b'

		else:
			str=str+ chr( ord(i)+2 )
	else:
		str=str+' '

print str
