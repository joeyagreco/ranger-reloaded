from prettytable import PrettyTable

from service.NetworkService import NetworkService

if __name__ == "__main__":
    logo = "                                 \n"
    logo += " _ __ __ _ _ __   __ _  ___ _ __ \n"
    logo += "| '__/ _` | '_ \ / _` |/ _ \ '__|\n"
    logo += "| | | (_| | | | | (_| |  __/ |   \n"
    logo += "|_|  \__,_|_| |_|\__, |\___|_|   \n"
    logo += "          _       __/ |     _          _ \n"
    logo += "         | |     |___/     | |        | |\n"
    logo += " _ __ ___| | ___   __ _  __| | ___  __| |\n"
    logo += "| '__/ _ \ |/ _ \ / _` |/ _` |/ _ \/ _` |\n"
    logo += "| | |  __/ | (_) | (_| | (_| |  __/ (_| |\n"
    logo += "|_|  \___|_|\___/ \__,_|\__,_|\___|\__,_|\n"

    credits = "Created by joeyagreco"

    print(logo)
    print(credits)

    devices = NetworkService.getAllDevices()
    devices.sort(key=lambda x: int(x.ipAddress.split(".")[-1]))

    table = PrettyTable(["IP Address", "Open Ports"])
    for device in devices:
        # get all open ports
        table.add_row([device.ipAddress, ", ".join(device.openPorts)])
    print(table)
