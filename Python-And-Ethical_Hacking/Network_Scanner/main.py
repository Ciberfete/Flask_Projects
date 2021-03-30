#!/usr/bin/env python

import scapy.all as scapy
import argparse


def get_ip():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ipTarget", dest="ip_target", help="The ip target to scan / Ip range to scan.")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=True)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_ip()
scan_result = scan(options.ip_target)
print_result(scan_result)
