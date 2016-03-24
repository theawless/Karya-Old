import os
#create folder at location with name
location = str(input(''))
name = str(input(''))
c = 'mkdir ~/'+location+'/'+name
os.system(c)

