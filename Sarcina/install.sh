#!/bin/sh

echo "Updating System"
sudo apt-get update
sudo apt-get upgrade

echo "Install Dependencies"
sudo apt-get install python-all-dev python3-all-dev
sudo apt-get install python3-pip
sudo apt-get install swig
sudo apt-get install portaudio19-dev
sudo pip3 install pyaudio
sudo pip3 install SpeechRecognition
sudo pip3 install pocketsphinx
sudo pip3 install word2number

echo "Moving Icon"
sudo cp sarcina.svg /usr/share/icons/hicolor/scalable/apps/

echo "Finished"
