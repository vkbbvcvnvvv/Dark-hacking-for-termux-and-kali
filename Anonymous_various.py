import os
import time
os.system ("clear")
os.system ("termux-open https://youtube.com/channel/UCTGKeXpv8fBlI5C_aXiyZ_A")
#############################################################
os.system ("figlet Anonymous")
############################################################
print ("\033[1;31m[1] \033[1;34mteam Z\033[1;31m(termux)")
time.sleep(0.3)
#______________
name = input ("Chose Nuber : ")
if name == "1" :
    print ("\033[1;31m[1] \033[1;34m install kali_Nethunter")
    time.sleep(0.3)
#_____________
    print ("\033[1;31m[2] \033[1;34m install metasploit")
    time.sleep(0.3)
#_____________
    print ("\033[1;31m[3] \033[1;34m hammer_Dos attack")
    time.sleep(0.3)
#_____________
    print ("\033[1;31m[4] \033[1;34m install Programming Languages ")
    time.sleep(0.3)
#_____________
if name == "1" :
    os.system ("termux-setup-storage")
    os.system ("pkg install wget")
    os.system ("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
    os.system ("chmod +x install-nethunter-termux")
    os.system ("./install-nethunter-termux")
#____________
if name == "2" :
    os.system ("pkg install wget")
    os.system ("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
    os.system ("chmod +x metasploit.sh")
    os.system ("./metasploit.sh")
#____________
if name == "3" :
    print ("You need a group of people who do the attack with you")
    os.system ("apt update && apt upgrade -y")
    os.system ("apt install git -y")
    os.system ("git clone https://github.com/Jmeel/Doosip.git")
    os.system ("cd Doosip")
    os.system ("python3 Doosip.py")
#____________
if name == "4" :
    print ("\033[1;31m[1] \033[1;34m install python")
    time.sleep(0.3)
#____________
name = input ("Chose Nuber : ")
if name == "1" :
    print ("\033[1;31m[1] \033[1;34m install python1")
    time.sleep(0.3)
#____________
    print ("\033[1;31m[2] \033[1;34m install python2")
    time.sleep(0.3)
#____________
    print ("\033[1;31m[3] \033[1;34m install python3")
    time.sleep(0.3) 
#____________
name = input ("Chose Nuber : ")
if name == "1" :
    os.system ("apt install python -y")
#____________
if name == "2" :
    os.system("apt install python2 -y")
#____________
if name == "3" :
    os.system("apt install pytho3 -y")
#____________

