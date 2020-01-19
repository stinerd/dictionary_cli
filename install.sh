#!/usr/bin/env bash 
echo "Startin install packages ..."
sleep 2


# install lib python 
pip install -r requirements.txt  --user

# Create alias 
if [ $SHELL = "/usr/bin/zsh" ];then
    mkdir $HOME/run_dict
    cp -r dict.py /$HOME/.run_dict
   echo alias dic='"python $HOME/.run_dict/dict.py"' >>  $HOME/.zshrc 
# Create alias 
elif [ $SHELL = "/usr/bin/bash" ];then
   mkdir $HOME/.run_dict
   cp -r dict.py /$HOME/run_dict
   echo alias dic='"python $HOME/.run_dict/dict.py"' >>  $HOME/.bashrc
fi
echo "Done install"