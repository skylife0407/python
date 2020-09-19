from itertools

f = open('output.txt','a')
in = input()

s='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result= list(product(s, repeat=2))
result=[''.join(elem) for elem in result]

for i in range(len(result)):
	f.write(str(result[i])+in+'_admin')
	f.write("\n")
	
f.close()