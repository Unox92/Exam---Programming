
class Device:
    """
    Represents a network device with basic online/offline status handling.
    """

    def __init__(self, name, ipaddress, hostname):
        """
        Sets the device name, IP address, and hostname.
        Initial device status is set to offline.
        """
        self.name = name
        self.ipaddress = ipaddress
        self.hostname = hostname
        self.status = "offline"

    def isOnline(self):
        """
        Toggles the device status between online and offline.
        Handles unknown states by resetting to offline.
        """
        if self.status == "offline":
            print("The device is currently offline setting status to online")
            self.status = "online"

        elif self.status == "online":
            print("The device is currently online setting status to offline")
            self.status = "offline"

        else:
            print("The device status unknown state, setting to offline")
            self.status = "offline"

    def device_properties(self):
        """
        Prints the device properties when the device is online.
        """
        if self.status == "online":
            print(
                "The device",
                self.name,
                "is currently online with ip address",
                self.ipaddress,
                "and hostname",
                self.hostname
            )
        else:
            print(
                "The device",
                self.name,
                "is currently online with ip address",
                self.ipaddress
            )