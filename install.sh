#!/usr/bin/env bash 
echo "Startin install packages ..."
echo "Please Wait ..."

# install lib python 
pip install -r requirements.txt  --user

# Create alias 
if [ $SHELL = "/usr/bin/zsh" ];then
   echo alias dic='"python $PWD/dict.py"' >>  $HOME/.zshrc 
fi


# Create alias 
if [ $SHELL = "/usr/bin/bash" ];then
   echo alias dic='"python $PWD/dict.py"' >>  $HOME/.bashrc
fi

echo "Done install"