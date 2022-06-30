import socket
import subprocess
import threading

from ping3 import ping

from model.Device import Device
from util.ConfigReader import ConfigReader
from util.Logger import Logger


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
        ipAddress = cls.getIpAddress()
        Logger.logGrey(f"- Found device IP Address: {ipAddress}")
        networkPortion = ".".join(ipAddress.split(".")[:3])
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
        ports = ConfigReader.get("network", "ports", asType=list)

        def __updateDevice(device_: Device, port_: int) -> None:
            if cls.portIsAlive(device_.ipAddress, port_):
                device_.openPorts.append(str(port_))

        aliveDevices = cls.getAllAliveDevices()
        Logger.logGrey(f"- Found {len(aliveDevices)} alive devices")
        Logger.logGrey(f"- Checking {len(ports)} ports on all devices")
        threads = list()
        for device in aliveDevices:
            for port in ports:
                thread = threading.Thread(target=__updateDevice, args=(device, int(port),))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
        Logger.logGrey(f"- Found {sum([len(device.openPorts) for device in aliveDevices])} vulnerable ports open")

        return aliveDevices
