import threading
import socket
import select
#connectorList
#MemShare
serverPort = 80

#placeholder for testing
class Connector():
    def __init__(self,a1,a2,a3):
        print("conn: {}\nip: {}\nport: {}".format(a1,a2,a3))

def main():
    #Await Signal from Window
    #THREAD
    threading.Thread(target=listen_and_accept()).start()
    #REPEAT
    #Check for updated memshare
    #divide updated memshare and send along connector_list
    #retrieve work and put back into memshare

def listen_and_accept():
    # create a TCP socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), serverPort))
                 
    #REPEAT
    while True:
    #Accept connection requests from Slices
        print("listening for slices")
        if serversocket in select.select([serversocket],[],[],0.1)[0]:
            #Create new Connector
            (conn, (ip, port)) = serversocket.accept()
            connector = Connector(conn, ip, port)
            connector.start()
            connectorList.append(connector)
            del connector
    print("Shutting down server socket")
    serversocket.close()

main()
