import socket
from server import PORT

if __name__ == '__main__':
    comp_id = input("Enter comp ID: ").strip()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',PORT))
    sock.sendall(f"JOINCLUSTER_{comp_id}".encode('utf-8'))
    data = sock.recv(1024).decode()
    print(data)
    print(data == f"ACK JOINCLUSTER_{comp_id}")
    data = sock.recv(1024).decode()
    order,comp_id,level,style,dance = data.split("_")
    print(f"order:{order}\n,comp_id:{comp_id}\n,level:{level}\n,style:{style}\n,dance:{dance}")
    sock.close()
