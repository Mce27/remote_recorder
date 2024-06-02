import socket,threading,time
PORT = 2223
CLIENT_DATA = {}

def handle_socket(socket:socket.socket):
    global CLIENT_DATA
    data = socket.recv(1024)
    data = data.decode('utf-8')
    print(data)
    comp_id = data.split("_")[1]
    socket.send(f"ACK {data}".encode())
    if comp_id not in CLIENT_DATA:
        CLIENT_DATA[comp_id] = []
    CLIENT_DATA[comp_id].append(socket)
    #socket.send(f"BEGINRECORDING_{comp_id}".encode())

    #socket.close()

def collect_sockets():
    global CLIENT_DATA
    while True:
        incoming_socket, _ = serv_socket.accept()
        threading.Thread(target=handle_socket,args=(incoming_socket,)).start()       


if __name__ == '__main__':
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(('127.0.0.1',PORT))
    serv_socket.listen(5)
    print(f"main thread: {threading.get_ident()}")
    threading.Thread(target=collect_sockets).start()
    input("press enter to send recording order")
    comp_id = "abc12"
    event = "BEGINNER_SMOOTH_WALTZ" #level_style_dance
    for sock in CLIENT_DATA[comp_id]:
        sock.send(f"BEGINRECORDING_{comp_id}_{event}".encode())
        sock.close()