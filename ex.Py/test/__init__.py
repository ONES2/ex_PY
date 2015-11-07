import socket
#import errno
#from time import time as now
#from _socket import getservbyport
#DEFAULT_TIMEOUT = 120
#DEFAULT_TIMEOUT = 'localhost'
#DEFAULT_TIMEOUT = 80

def find_service_name():
    protocolname = 'tcp'
    for port in range (20,40):
        try:
            print "Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))
        except socket.error, err_msg:
            print "%s: %s" %(port, err_msg) 
        #print "Port: %s => service name: %s" %(53, socket.getservbyport(53,'udp'))
        




def print_machine_info():
    host_name = socket.gethostname()
    ip_addr = socket.gethostbyname(host_name)
    
    
    print"%s" %host_name
    print"%s" %ip_addr


def get_remote_machine_info():
    remote_host = 'www.naver.com'
    try:
        print "IP = %s:%s" %(remote_host, socket.gethostbyname(remote_host))
        
    except socket.error, err_msg:
            print "%s: %s" %(remote_host, err_msg)

if __name__ == '__main__':
    #print_machine_info()
    #get_remote_machine_info()
    find_service_name()