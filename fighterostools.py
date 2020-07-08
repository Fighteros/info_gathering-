from time import sleep
import random
from urllib3 import *
from urllib.request import urlopen
from platform import system
import sys
import os

os.system('cls')
os.system('color a')
    
def byte_to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes): # Check if it's in bytes
       with open("resutls.txt","w") as xc:
           xc.write(bytes_or_str.decode('utf-8'))
    else:
        print("Object not of byte type")
def splitor():
        b=[]
        mylist=[]
        myip=[]
        sy=""
        cmk=""
        with open("resutls.txt","r") as c:
                b=c.readlines()
        for i in b:
                i=(i.split(",")[0])
                mylist.append(i)
        for i in b:
                i=(i.split(",")[1])
                myip.append(i)
        for i in range(len(mylist)):
                sy+=str(mylist[i]+"\n")
                cmk+=str(myip[i])
                with open("domains.txt","w") as tsy:
                        tsy.write(sy)
                with open("ips.txt","w") as ips:
                        ips.write(cmk)
        print("done splitting and parsing ")


        
banner="""
   ___  _         _      _                   ___  __    
  / __\(_)  __ _ | |__  | |_   ___  _ __    /___\/ _\   
 / _\  | | / _` || '_ \ | __| / _ \| '__|  //  //\ \    
/ /    | || (_| || | | || |_ |  __/| |    / \_// _\ \   
\/     |_| \__, ||_| |_| \__| \___||_|    \___/  \__/   
           |___/                             v2 tools
           """
print(banner)
about="""
    Ahmed M.Abd El-Ghany
    fb/AhmedAbdElGhany
    contact me for any problem on
    yandobendo111@gmail.com
    i'm on github as fighteros
                  """
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def menu():
    print("""
    1-Dns lookup
    2-Whois Lookup
    3-Reverse IP Lookup
    4-GeoIP Lookup
    5-Subnet Lookup
    6-Port Scanner
    7-Extract Links 
    8-Zone Transfer
    9-HTTP Header
    10-Host Finder
    11-About
    12-split results to ips and domains
    13- HTTP HEADERS CHECKER
    0-Exit
    """)
menu()

        
def ext():
    ex=input("Continue/Exit [C/E]: ")
    c=ex[0].upper()
    if c == " E ":
        print ("Exiting")
        exit()
    else:
        clear()
        print (banner)
        menu()
        select()
def  select():
    try:
        jo=input("Enter number of tool pls: ")
        ina=(int(jo))
        if ina ==1 :
             dz =input("enter Domain: ")
             dns = "http://api.hackertarget.com/dnslookup/?q=" + dz
             qx=urlopen(dns).read()
             byte_to_str(qx)
             print(qx)
             ext()
        elif ina ==2:
            dz=input("Enter an IP address: ")
            whois = "http://api.hackertarget.com/whois/?q=" + dz
            url=urlopen(whois).read()
            byte_to_str(url)
            print(url)
            ext()
        elif ina==3:
            dz=input("Enter Ip address: ")
            ril="http://api.hackertarget.com/reverseiplookup/?q=" + dz
            rq=urlopen(ril).read()
            byte_to_str(rq)
            print(rq)
            ext()
        elif ina==4:
            dz=input("Enter IP address: ")
            geo= "http://api.hackertarget.com/geoip/?q=" + dz
            ip = urlopen(geo).read()
            byte_to_str(ip)
            print (ip)
            ext()
        elif ina ==5:
            dz = input("Enter IP Address : ")
            sub = "http://api.hackertarget.com/subnetcalc/?q=" + dz
            net = urlopen(sub).read()
            byte_to_str(net)
            print (net)
            ext()
        elif ina ==6:
            dz=input("Enter IP Address : ")
            port = "http://api.hackertarget.com/nmap/?q=" + dz
            scan = urlopen(port).read()
            byte_to_str(scan)
            print (scan)
            ext()
        elif ina ==7:
            dz=input("enter Domain: ")
            get = "https://api.hackertarget.com/pagelinks/?q=" + dz
            page = urlopen(get).read()
            byte_to_str(page)
            print(page)
            ext()
        elif ina ==8:
            dz=input("enter Domain: ")
            zon = "http://api.hackertarget.com/zonetransfer/?q=" + dz
            tran = urlopen(zon).read()
            byte_to_str(tran)
            print (tran)
            ext()
        elif ina ==9:
            dz=input("enter Domain: ")
            hea = "http://api.hackertarget.com/httpheaders/?q=" + dz
            der =  urlopen(hea).read()
            byte_to_str(der)
            print (der)
            ext()
        elif ina ==10:
            dz=input("enter Domain: ")
            host = "http://api.hackertarget.com/hostsearch/?q=" + dz
            finder = urlopen(host).read()
            byte_to_str(finder)
            print (finder)
            ext()
        elif ina ==11:
           print(about)
           ext()
        elif ina ==13:
            nvb=input('input domain : ')
            pi='https://api.hackertarget.com/httpheaders/?q='
            xxc=pi+nvb
            mnvb=urlopen(xxc).read()
            byte_to_str(mnvb)
            print(mnvb)
            ext()
        elif ina==12:
            splitor()
            ext()
        elif ina == 0:
            print ("Exiting!!")
            ext()
    except(KeyboardInterrupt):
        print ("\nCtrl + C -> Exiting")
select()
