#!/usr/bin/env python

import subprocess
from optparse import OptionParser
import re


def current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Mac address")


def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change Mac.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New digits for Mac Address.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("Please write the new digits for mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
print_current_mac = current_mac(options.interface)
print("Current mac is: " + str(print_current_mac))
change_mac(options.interface, options.new_mac)
print_current_mac = current_mac(options.interface)
if print_current_mac == options.new_mac:
    print("[+] MAC Address ha sido cambiado correctamente a: " + print_current_mac)
else:
    print("[-] Mac Address no ha sido cambiado.")













