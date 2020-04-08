import socket
import socketserver
import time
import datetime
import ipaddress
import subprocess
import threading
import socket
from queue import Queue
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from ipaddress import IPv4Interface, IPv6Interface
 
class NetworkCardFinder:
        # This class queries the OS to return the systems network card
    def __init__(self):
        self.nic=[]
    def getNics(self):
 
        self.cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,MACAddress,IPSubnet,DNSHostName,Caption,DefaultIPGateway /format:rawxml'
            # runs the systems cmd.exe and returns all the details of NIC's that are IP Enabled 
        self.xml_text = check_output(self.cmd, creationflags=8) #False positive flag on check_output

        self.xml_root = fromstring(self.xml_text)
 
        self.nics = []
            # Links returned information to Dictonary headings

        self.keyslookup = {
            'DNSHostName' : 'hostname',
            'IPAddress' : 'ip',
            'IPSubnet' : '_mask',
            'Caption' : 'hardware',
            'MACAddress' : 'mac',
            'DefaultIPGateway' : 'gateway',
        }
             # creates a Dictonary from xml.text
            
        for self.nic in self.xml_root.findall("./RESULTS/CIM/INSTANCE") :
        # Itterates the NIC list and stores nic info
            self.n = {
                'hostname':'',
                'ip':[],
                '_mask':[],
                'hardware':'',
                'mac':'',
                'gateway':[],
            }
            for prop in self.nic :
                self.name = self.keyslookup[prop.attrib['NAME']]
                if prop.tag == 'PROPERTY':
                    if len(prop):
                        for v in prop:
                            self.n[self.name] = v.text
                elif prop.tag == 'PROPERTY.ARRAY':
                    for v in prop.findall("./VALUE.ARRAY/VALUE") :
                        self.n[self.name].append(v.text)
            self.nics.append(self.n)
 
            # creates python ipaddress objects from ips and masks
            for i in range(len(self.n['ip'])) :
                arg = '%s/%s'%(self.n['ip'][i],self.n['_mask'][i])
                if ':' in self.n['ip'][i] : self.n['ip'][i] = IPv6Interface(arg)
                else : self.n['ip'][i] = IPv4Interface(arg)
            del self.n['_mask']
 
        self.myNics = str(self.nics[0]['ip'])
        self.myIPs = str(self.myNics[16:30])
        return self.myIPs

# Test for the NIC Class and pass through for ipScanner
#cardfinder = NetworkCardFinder()
#card = cardfinder.getNics()
#print(card)
#target = card[0]

class ipScanner:

    def __init__(self):
        print('scanning network for devices')


    def scanner(self,card):
        self.print_lock = threading.Lock() # sets the threading lock function to a veriable
        self.net_addr = card # set's the current machines IP address to a veriable as a bassis to scan from
        self.ip_net = ipaddress.ip_network(self.net_addr, strict= False) # 
        self.all_hosts = list(self.ip_net.hosts())
        self.info = subprocess.STARTUPINFO()
        self.info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self.info.wShowWindow = subprocess.SW_HIDE
        self.ipList = []

        def pingsweep(ip):

            # for windows:   -n is ping count, -w is wait (ms)
            # for linux: -c is ping count, -w is wait (ms)
            # I didn't test subprocess in linux, but know the ping count must change if OS changes
 
            self.output = subprocess.Popen(['ping', '-n', '1', '-w', '150', str(self.all_hosts[ip])], stdout=subprocess.PIPE, startupinfo=self.info).communicate()[0]
 
            with self.print_lock:
 
                if "Reply" in self.output.decode('utf-8'):
                    #print(str(self.all_hosts[ip]) + " is Online")
                    self.ipList.append(str(self.all_hosts[ip]))
                    return self.ipList
                elif "Destination host unreachable" in self.output.decode('utf-8'):
                    pass
                elif "Request timed out" in self.output.decode('utf-8'):
                    pass
                else:
                    print("UNKNOWN")
            #print(self.ipList)

        def threader():
            while True:
                self.worker = self.q.get()
                pingsweep(self.worker)
                self.q.task_done()

      
        self.q = Queue()
 
        for x in range(100):
            self.t = threading.Thread(target = threader)
            self.t.daemon = True
            self.t.start()
 

        for self.worker in range(len(self.all_hosts)):
            self.q.put(self.worker)
 
            self.q.join()
        #print(self.ipList)
        return self.ipList

# Tests for ipScan class

#ipScan = ipScanner()
#ipScan.scanner(card)
#print(ipScan)

class PortScanner():
    def __init__(self):
        print("Scanning for open Ports")

    def startScan(self): #Function to scan the specified ip address for open ports
        
        r = 1
        for x in range(1,100): #Creates 100 threads to search for open ports
     
            t = threading.Thread(target=self.portscan,kwargs={'port':r}) 
    
            r += 1     
            t.start()

    def portscan(self,port): #Function that does the scanning


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)# 
        self.portList = []
            # Opens a network socket

        try:
            con = s.connect((target,port))
            print('Port :',port,"is open.")
            self.portList.append(int(port))
            con.close()
                # tries to connect to each port on a target ip then closes the port when done
        except: 
            pass
            # passes if there are not more ports

        #print(portList)


# Test for the portScanner class
#scan = PortScanner()
#scan.startScan()
#print(scan)



# prototype network send function

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(), 6666))
soc.listen(5)
while True:
    clientsocket, address = soc.accept()
    print(f"Connection established with {address}")
    clientsocket.send(bytes("connected", "utf-8"))
    clientsocket.close()

