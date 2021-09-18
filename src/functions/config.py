import re


def get_network_command():
    with open('control-center.conf', 'r') as file:
        data = file.read()

        network_command_regex = re.compile(r'(?<=network-command=)[a-z\-\_]+')
        network_command = network_command_regex.search(data).group()

        return network_command


def get_bluetooth_command():
    with open('control-center.conf', 'r') as file:
        data = file.read()

        network_command_regex = re.compile(r'(?<=bluetooth-command=)[a-z\-\_]+')
        network_command = network_command_regex.search(data).group()

        return network_command
