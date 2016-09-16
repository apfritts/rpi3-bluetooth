from bluetooth import *

server_sock=BluetoothSocket(L2CAP)
server_sock.bind(("", 17))

with open(sys.path[0] + "/sdp_record.xml", "r") as fh:
        service_record = fh.read()
self.bus = dbus.SystemBus()
self.manager = dbus.Interface(self.bus.get_object("org.bluez", "/"),"org.bluez.Manager")
adapter_path = self.manager.DefaultAdapter()
self.service = dbus.Interface(self.bus.get_object("org.bluez",adapter_path),
                                                       "org.bluez.Service")
service_handle = service.AddRecord(service_record)
print "Service record added"
server_sock.listen(1)

print("Waiting for connection on L2CAP")

try:
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    while True:
        data = client_sock.recv(1024)
        if len(data) == 0:
                break
        print("received [%s]" % data)
except IOError:
    pass
except KeyboardInterrupt:
    print "Stopping..."
    stop_advertising(server_sock)
    sys.exit()

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
