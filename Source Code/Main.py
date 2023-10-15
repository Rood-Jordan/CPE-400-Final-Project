import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found " + str(len(nearby_devices)) + " devices!")

# loop through connected devices printing address and name
for addr, name in nearby_devices:
    print(f"Address: {addr}, Name: {name}")

# create bluetooth socket to communicate via RFCOMM
socketConn = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

socketConn.bind(("", bluetooth.PORT_ANY))
socketConn.listen(1)

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")
data_received = client_socket.recv(1024)

client_socket.close()
server_socket.close()