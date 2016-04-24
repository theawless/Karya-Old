import json
import os
import subprocess
import urllib


def local_search(search_keywords):
    """
    searches for a file by matching the file names in a directory tree while walking through the tree either top-down
    :type search_keywords: basestring
    :param search_keywords: text to search
    :return: list of tuple containing name and path of file
    """
    search_result_paths = ["" for x in range(2000)]
    search_result_names = ["" for x in range(2000)]
    l = []
    i = 0
    for root, dirs, files in os.walk('../../../../'):
        for file in files:
            if search_keywords in file:
                # Getting full path of the file
                path = os.path.join(root, file)
                search_result_names[i] = file
                tup = str(path), str(file)
                l.append(tup)
                print(search_result_names[i])
                search_result_paths[i] = path
                i += 1
    return l


def open_file_in_default_application(file_path):
    """
    opens file in default application
    :param file_path: path of the file to open
    :return:null
    """
    subprocess.call(["xdg-open", file_path])

def open_application(application):
    """
    open application
    :param application:
    :return:
    """
    os.system(application)

def google_search(text):
    """
    opens the URL and returns the JSON results from the google search api
    :param text: text to search
    :return: JSON data containing title, link, and snippet of 10 search results
    """
    url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDKXPuaXh84T_tVVQcxQdbQS8TzNk2uuuU" \
          + "%20&cx=017576662512468239146:omuauf_lfve&q="
    words_to_search = text.split()
    search_keywords = ""
    for word in words_to_search:
        search_keywords += word + '+'
        url = url + search_keywords
    print("URL is : " + url)
    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("utf8"))
    for i in data['items']:
        print(i['title'])
        print(i['link'])
        print(i['snippet'])
    return data

def music(action):
    """
    controls music player rhythm box
    :param action:
    :return: null
    """
    if action == 'play':
        os.system('rhythmbox-client --play-pause')
    elif action == 'pause':
        os.system('rhythmbox-client --play-pause')
    elif action == 'next song':
        os.system('rhythmbox-client --next')
    elif action =='previous song':
        os.system('rhythmbox-client --previous')
    elif action == 'increase volume':
        os.system('rhythmbox-client --volume-up')
    elif action == 'decrease volume':
        os.system('rhythmbox-client --volume-down')

def click(action):
    x_pos = str(action['click']['x'])
    y_pos = str(action['click']['y'])
    command = 'xdotool mousemove ' + x_pos + ' ' + y_pos + ' click 1'
    os.system(command)

def shutdown(action):
    os.system("shutdown 0")


