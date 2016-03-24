import os
#delete file in location with name
location = str(input(''))
name = str(input(''))
c = 'rm ~/'+location+'/'+name
os.system(c)

