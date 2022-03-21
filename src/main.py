#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a script to make it easier to switch between PHP versions on local environments.
"""
from gettext import install
from sys import stdout

try:
    import sys
    import subprocess
    from bullet import Bullet
    from bullet import colors
    from huepy import *
except ModuleNotFoundError as e:
    print(bad(red('There was an error importing one more more modules:')), e.name, '\n')
    print('Please run', yellow('pip3 install -r requirements.txt'), 'on PVM directory.')
    sys.exit(0)

__author__ = "Danton Mariano"
__copyright__ = "Copyright 2022, Zoocha"
__credits__ = ["Danton Mariano", "Gusta"]
__license__ = "TBD"
__version__ = "0.1.0"
__maintainer__ = "Danton Mariano"
__email__ = "danton@zoocha.com"
__status__ = "Development"

# Initialize constants.
PHP_LOGO = """
██████╗ ██╗  ██╗██████╗                                       
██╔══██╗██║  ██║██╔══██╗                                      
██████╔╝███████║██████╔╝                                      
██╔═══╝ ██╔══██║██╔═══╝                                       
██║     ██║  ██║██║                                           
╚═╝     ╚═╝  ╚═╝╚═╝                                           
"""
BLUE_LOGO = """
██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗       
██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║       
██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║       
╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║       
 ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║       
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝       
"""
YELLOW_LOGO = """
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def main_menu() -> str:
    question_main_menu = Bullet(
        prompt="\nSelect an option: ",
        choices=["[1] - See PHP Versions Installed",
                 "[2] - Change PHP Version",
                 "[3] - Install New PHP Version",
                 "[0] - Exit"],
        indent=0,
        align=2,
        margin=1,
        bullet="➤",
        bullet_color=colors.bright(colors.foreground["green"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=1
    )
    return str(question_main_menu.launch()).split('-')[1].strip()

def get_php_versions() -> list:
    output = subprocess.run(['update-alternatives --list php'], shell=True,stdout=subprocess.PIPE)
    list = str(output.stdout).split("b'")
    list = ''.join(list)
    list = list.split("\\n")
    list = ''.join(list)
    list = list.split("'")
    list = ''.join(list)
    list = list.split('/usr/bin/php')
    list.pop(0)
    return list

def now_running_php(version): 
    output = subprocess.run(['php -v | grep "PHP {}"'.format(version)], shell=True, stdout=subprocess.PIPE)
    php_version = str(output.stdout)
    if php_version == "b''":
        print(red("Version not available."))
    else:
        print(green("Now running PHP {}!".format(version)))

def change_php(version):
    print(run(red('We need your super user password to change the PHP version in use.\n')))
    subprocess.run(['sudo update-alternatives --set php /usr/bin/php{}'.format(version)], shell=True)
    now_running_php(version)

def install_php(version):
    subprocess.run('sudo apt install php{} -y'.format(version), shell=True)
    change_php(version)

def main(control = False):
    try: 

        if len(sys.argv) == 3 and (sys.argv[1] == "-cv" or sys.argv[1] == "--change-version"):
            change_php(sys.argv[2])
            sys.exit(0)
        elif len(sys.argv) == 3 and (sys.argv[1] == "-i" or sys.argv[1] == "--install"):
            install_php(sys.argv[2])
            sys.exit(0)
        elif len(sys.argv) > 2:
            print("Oops, too many arguments, by now you can run zork -h OR zork --help")
            sys.exit(0)
        elif sys.argv[0] == __file__ and len(sys.argv) > 1:
            print("Oops, type zork -h OR zork --help to see what zork can do")
            sys.exit(0)

        if(control == True):
            print(purple(PHP_LOGO)+blue(BLUE_LOGO)+yellow(YELLOW_LOGO)+blue("#STANDWITHUKRAINE"))

        answer = main_menu()

        if answer == "See PHP Versions Installed":
            list = get_php_versions()
            for phpv in list:
                print("    "+purple("PHP")+"-{}".format(phpv))
            question_go_back = Bullet(
                choices=['Go Back', 'Exit'],
                indent=0,
                align=2,
                margin=1,
                bullet="➤",
                bullet_color=colors.bright(colors.foreground["green"]),
                background_color=colors.background["black"],
                background_on_switch=colors.background["black"],
                pad_right=2
            )
            if question_go_back.launch() == "Go Back":
                main()
            else:
                print("\nExiting PVM, Bye!")

        if answer == "Change PHP Version":
            list = ["Go Back"] + get_php_versions()
            question_php_version = Bullet(
                prompt="\nWhich PHP Version would you like to change to? ",
                choices=list,
                indent=0,
                align=2,
                margin=1,
                bullet="➤",
                bullet_color=colors.bright(colors.foreground["green"]),
                background_color=colors.background["black"],
                background_on_switch=colors.background["black"],
                pad_right=2
            )
            answer = question_php_version.launch()
            if answer == "Go Back":
                main()
            else:
                change_php(answer)
        
        if answer == "Install New PHP Version":
            answer = input("Which version would you like to have installed? ")
            available_options = ['5.6', '7.0', '7.1', '7.3', '8.0', '8.1']
            if answer not in available_options:
                print(red("That's not an available version of PHP"))
                main()
            else:
                print(green('Installing PHP Version {}'.format(answer)))
                print(run(red('We need your super user password to change the PHP version in use.\n')))
                install_php(answer)
                
    except KeyboardInterrupt:answer

main(True)