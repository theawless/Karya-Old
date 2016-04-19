import os
count = 0
while (count < 9):
    os.system('xdotool mousemove 146 39 click 1 && sleep 3')
    count = count + 1
#Image viewer must be in full screen and current tab is also image viewer
#Here Sleep 3 for wait for some time and count for number of times we want to click next.
