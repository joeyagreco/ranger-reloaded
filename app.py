# We need to create regular expressions to ensure that the input is correctly formatted.

from service.NetworkService import NetworkService

if __name__ == "__main__":
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(("8.8.8.8", 80))
    # ip = s.getsockname()[0]
    # s.close()
    # print(ip)

    # devices = []
    # for device in os.popen('arp -a'): devices.append(device)
    # print(devices)

    # nds = NetworkService.getAllNetworkDevicesOnNetwork()
    # print()

    # print(NetworkService.getSubnetMaskOfNetwork())

    # ip = ipaddress.ip_network('192.0.2.0/255.255.255.0')
    # print(ip)

    # print(NetworkService.hostIsAlive("192.168.1.17"))
    # print(NetworkService.getIpAddress())
    ds = NetworkService.getAllDevices()
    for d in ds:
        print(d)
    #
    # print(NetworkService.portIsAlive("192.168.1.17", 21))
