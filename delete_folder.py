import os
#delete folder in location with name
location = str(input(''))
name = str(input(''))
c = 'rm -R ~/'+location+'/'+name
os.system(c)

