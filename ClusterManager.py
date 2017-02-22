import threading
import socket
import select

filename = "config.config"

#dummy for testing
class Connector:
    def __init__(self,ip, port):
        print("debug: ip {} : port {}".format(ip,port))

def main():
    #TODO: read config file and parse slice's ip and port
    connectorList = createConnectors()

def createConnectors():
    configfile = open(filename, "r")
    connectorList = []
    
    while True:
        sliceAddress = configfile.readline()
        if sliceAddress == "":
            break
        sliceIp, slicePort = sliceAddress.split(":")
        connectorList.append(Connector(sliceIp,int(slicePort)))
    return connectorList
        

    
main()
