import socket
import sys 

iplist = sys.argv[1:] 
if len(iplist) == 0 :
    print("No IP adresses given")
    exit(0)

# Dictionary as seen at https://www.spamhaus.org/faq/section/DNSBL%2520Usage#200
zen_dict = {
    '127.0.0.2' : 'SBL - Spamhaus SBL Data'     ,
    '127.0.0.3' : 'SBL - Spamhaus SBL CSS Data' ,
    '127.0.0.4' : 'XBL - CBL Data'  ,
    '127.0.0.9' : 'Spamhaus DROP/EDROP Data (in addition to 127.0.0.2, since 01-Jun-2016)',
    '127.0.0.10': 'PBL - ISP Maintained',
    '127.0.0.11': 'PBL - Spamhaus Maintained'
}

blacklist = "zen.spamhaus.org"

for ip in iplist:
    try:
        ip_rev = '.'.join(ip.split('.')[::-1]) # turn 127.0.0.2 into 2.0.0.127
        query = ip_rev +'.'+ blacklist
        addr = socket.gethostbyname_ex(query) 
        
        for a in addr[2]:
            print("The IP address: "+ ip +" is found in the following Spamhaus public IP zone: \'" + a +" - "+ zen_dict[a] + "\'")
    except:
        print("The IP address: "+ ip +" is NOT found in the Spamhaus blacklists.")
