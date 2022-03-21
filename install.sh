#!/bin/bash

echo "This script will install the following softwares: Python and PHP Version Manager. Would you like to proceed?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) 
        
            echo -e 'Installing dependencies...\n'
            sudo apt-get install -y build-essential python3 python3-dev python3-pip python3-setuptools
            sudo pip3 install --upgrade pip
            sudo apt-get install -y curl libcurl4-gnutls-dev librtmp-dev aria2
            cd /home/$USER/zork/
            pip3 install -r requirements.txt

            echo -e 'Adding pvm alias...\n'
            alias pvm='python3 /home/$USER/pvm/src/main.py'
            echo "alias pvm='python3 /home/$USER/pvm/src/main.py'" >> ~/.bashrc
            echo "alias pvm='python3 /home/$USER/pvm/src/main.py'" >> ~/.zshrc

            echo -e '\nSetup finished...\n'
            echo -e '\nRestart your terminal and run pvm command to use it...\n'
            echo -e '\nExiting installer... Thanks for Using PHP Version Manager!!\n'

            break;;
        No ) 
            exit;;
    esac
done