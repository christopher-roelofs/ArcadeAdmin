#!/usr/bin/env bash

#MAME
echo "Intalling MAME dependencies"
sudo apt-get install git build-essential libgtk2.0-dev libgnome2-dev libsdl1.2-dev libsdl-ttf2.0-dev libsdl2-ttf-dev qt5-default


#EmulationStation
echo "Installing EmulationStation dependencies"
sudo apt-get install libsdl2-dev libboost-system-dev libboost-filesystem-dev libboost-date-time-dev libboost-locale-dev libfreeimage-dev libfreetype6-dev libeigen3-dev libcurl4-openssl-dev libasound2-dev libgl1-mesa-dev build-essential cmake fonts-droid-fallback


#ArcadeAdmin
echo "Installing ArcadeAdmin dependencies"
sudo apt-get install pip
pip install flask_admin
pip install flask_sqlalchemy


#Retroarch
echo "Installing Retroarch"
sudo add-apt-repository ppa:libretro/stable
sudo apt-get update
sudo apt-get install retroarch retroarch-* libretro-*


