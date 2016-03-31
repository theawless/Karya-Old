import os
#lists content of a folder in location
location = str(input(''))
list1 = str.split(location)
c = '~/'
l = len(list1)
i=0
while i<l :
	c = ''.join([c,list1[i],'/'])
	i = i+1
com = 'ls '+c
os.system(com)

