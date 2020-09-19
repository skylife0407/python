bmw=raw_input("input number \n:").split(",")

for line in range(len(bmw)):
	bmw[line]=int(bmw[line])

url=''

for i in bmw[0:-1]:
	c=chr(int(hex(i-bmw[-1]),16))
	url=url+c

print(url)