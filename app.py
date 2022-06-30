from prettytable import PrettyTable

from service.NetworkService import NetworkService
from util.Logger import Logger

if __name__ == "__main__":

    logo = """
 _ __ __ _ _ __   __ _  ___ _ __ 
| '__/ _` | '_ \ / _` |/ _ \ '__|
| | | (_| | | | | (_| |  __/ |   
|_|  \__,_|_| |_|\__, |\___|_|   
          _       __/ |     _          _ 
         | |     |___/     | |        | |
 _ __ ___| | ___   __ _  __| | ___  __| |
| '__/ _ \ |/ _ \ / _` |/ _` |/ _ \/ _` |
| | |  __/ | (_) | (_| | (_| |  __/ (_| |
|_|  \___|_|\___/ \__,_|\__,_|\___|\__,_|
"""

    appCredits = "Created by joeyagreco"

    Logger.logRed(logo)
    Logger.logBlue(appCredits)
    Logger.logGrey("\n")

    devices = NetworkService.getAllDevices()
    devices.sort(key=lambda x: int(x.ipAddress.split(".")[-1]))

    table = PrettyTable(["IP Address", "Open Ports"])
    for device in devices:
        table.add_row([device.ipAddress, ", ".join(sorted(device.openPorts, key=lambda x: int(x)))])

    Logger.logGrey("\n")
    Logger.logYellow(table)
