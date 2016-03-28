import os
#create folder at location with name
location = str(input(''))
name = str(input(''))
list1 = str.split(location)
c = '~/'
l = len(list1)
i=0
while i<l :
	c = ''.join([c,list1[i],'/'])
	i = i+1
com = 'mkdir '+c+name
os.system(com)

