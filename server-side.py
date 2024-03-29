import socket
"""
desc:
This program is used for sending "small letters string" from the client and getting "capital letters" from the server
https://stackoverflow.com/questions/11352855/communication-between-two-computers-using-python-socket
"""


def Main():
   
    host = '192.168.1.28' # Server ip
    port = 4000 # Musi byt povoleny port, v linux base systemu to neni problem, ve Windows muze jebat firewall!!!
                # linux: iptables -L would show you the firewall rules

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), addr)
    c.close()

if __name__=='__main__':
    Main()