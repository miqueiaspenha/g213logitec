import usb.core
import usb.util
import binascii
import re

def scan_text(data):
    lines = data.split('\n')
    for line in lines:
        temVendor = line.find('idVendor')
        temProduct = line.find('idProduct')
        if(temVendor > 0):
            print(line[26:])
        if(temProduct > 0):
            print(line[26:])

devices = usb.core.find(find_all=True)

#d1 = next(devices)
#d2 = next(devices)

for device in devices:
    scan_text(str(device))
    #print(device)
    #print(dir(device.iManufacturer))
    #print("-----------------------------------")
    #print("-----------------------------------")
    #print(usb.util.get_string(device, device.iManufacturer))
    #print(usb.util.hexversion(device, device.iManufacturer))
    #print("-----------------------------------")
    #print(usb.util.get_string(device, device.iProduct))
    #print("-----------------------------------")
    #idProduct = device.iProduct
    #print(ord(idProduct))
    #scan_text(device)