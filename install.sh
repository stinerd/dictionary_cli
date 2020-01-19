#!/usr/bin/env bash 
echo "Startin install packages ..."
sleep 2

# Create alias 
if [ $SHELL = "/usr/bin/zsh" ];then
    mkdir $HOME/.rundict
    cp -r dict.py /$HOME/.rundict
   echo alias dic='"python $HOME/.rundict/dict.py"' >>  $HOME/.zshrc 
# Create alias 
else [ $SHELL = "/usr/bin/bash" ];then
   mkdir $HOME/.rundictbash
   cp -r dict.py /$HOME/.rundictbash
   echo alias dic='"python $HOME/.rundictbash/dict.py"' >>  $HOME/.bashrc
fi
echo "Done install"
