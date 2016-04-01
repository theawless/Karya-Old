import os
#create folder at location with name
def music(action):
	if action == 'play':
		os.system('rhythmbox-client --paly-pause')
	elif action == 'pause':
		os.system('rhythmbox-client --paly-pause')
	elif action == 'next song':
		os.system('rhythmbox-client --next')
	elif action =='previous song':
		os.system('rhythmbox-client --previous')
	elif action == 'increase volume':
		os.system('rhythmbox-client --volume-up')
	elif action == 'decrease volume':
		os.system('rhythmbox-client --volume-down')