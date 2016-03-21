#OWRIVTWRQ6THEF5EOF6TV4EHN4J3NSO4
#A3OGNVOCVIMZVWBWLHSV2WLNO5ASS43J
import os, sys, subprocess
import gi
import urllib.parse
import urllib.request
import json
import threading
from text_analyser import text_analyser
from srecog import SpeechRecogniser
from functions import *
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


Sr = SpeechRecogniser()
settings = {'Main'   : {'recogniser':'WITAI'},
            'Google' : {'api_key':'OWRIVTWRQ6THEF5EOF6TV4EHN4J3NSO4'},
            'WITAI'  : {'api_key':''} }
Sr.fix_ambient_noise()
text = Sr.recog(settings)
print(text)

suraj = {'entities' : text['outcomes'][0]['entities'],
         'action'                : text['outcomes'][0]['intent'] }












