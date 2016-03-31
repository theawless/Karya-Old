#!/bin/sh

echo "Updating"
apt-get update
apt-get upgrade

echo "Install Dependencies"
apt-get install python3-pip
apt-get install swig
apt-get install portaudio-dev puthon-all-dev python3-all-dev
pip3 install pyaudio
pip3 install SpeechRecognition
pip3 install pocketsphinx

echo "Making Directory"
mkdir ~/.local/share/gedit/plugins/

echo "Moving Files"
cp pyDictator.plugin ~/.local/share/gedit/plugins/
cp pyDictator.py ~/.local/share/gedit/plugins/
cp recogSpeech.py ~/.local/share/gedit/plugins/
cp setlog.py ~/.local/share/gedit/plugins/
cp statesMod.py ~/.local/share/gedit/plugins/

echo "Finished"
