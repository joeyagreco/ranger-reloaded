import socket
import subprocess
import threading

from ping3 import ping

from model.Device import Device


class NetworkService:

    @classmethod
    def getSubnetMaskOfNetwork(cls) -> str:
        """
        Will return something like: "255.255.255.0"
        """
        process = subprocess.Popen("ipconfig", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in process.stdout.readlines():
            line = line.decode("utf-8")
            parts = line.split()
            if len(parts) >= 3 and parts[0] == "Subnet" and parts[1] == "Mask":
                return parts[-1]

    @classmethod
    def getIpAddress(cls) -> str:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]

    @classmethod
    def getAllIpAddressesOnNetwork(cls) -> list[str]:
        networkPortion = ".".join(cls.getIpAddress().split(".")[:3])
        return [f"{networkPortion}.{clientPortion}" for clientPortion in range(0, 256)]

    @classmethod
    def portIsAlive(cls, ipAddress: str, port: int, timeout: float = 0.5) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ipAddress, port))
        except:
            return False
        return True

    @classmethod
    def hostIsAlive(cls, hostname: str, timeout: int = 1) -> bool:
        return isinstance(ping(hostname, timeout=timeout), float)

    @classmethod
    def getAllAliveDevices(cls) -> list[Device]:

        def __addToListIfAlive(ip: str, l: list) -> None:
            if cls.hostIsAlive(ip):
                l.append(Device(ipAddress=ip))

        allAliveDevices = list()
        threads = list()
        for ipAddress in cls.getAllIpAddressesOnNetwork():
            thread = threading.Thread(target=__addToListIfAlive, args=(ipAddress, allAliveDevices,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        return allAliveDevices

    @classmethod
    def getAllDevices(cls) -> list[Device]:
        ports = [20,
                 21,
                 22,
                 23,
                 25,
                 53,
                 69,
                 80,
                 81,
                 110,
                 135,
                 137,
                 139,
                 145,
                 443,
                 445,
                 1433,
                 1434,
                 1443,
                 3306,
                 3386,
                 3389,
                 5900,
                 8080,
                 8443,
                 52106]

        def __updateDevice(device_: Device, port_: int) -> None:
            if cls.portIsAlive(device_.ipAddress, port_):
                device_.openPorts.append(str(port_))

        aliveDevices = cls.getAllAliveDevices()
        threads = list()
        for device in aliveDevices:
            for port in ports:
                thread = threading.Thread(target=__updateDevice, args=(device, port,))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
        return aliveDevices
