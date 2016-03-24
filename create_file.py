import os
#create file in location with name
location = str(input(''))
name = str(input(''))
c = 'touch ~/'+location+'/'+name
os.system(c)

