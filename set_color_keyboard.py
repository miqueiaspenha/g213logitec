#!/usr/bin/env python3

import sys
import usb.core
import usb.util
import binascii

idVendor = 0x046d
idProduct = 0xc336
colorCommand = '11ff0c3a{}01{}0200000000000000000000'

bmRequestType = 0x21
bmRequest = 0x09
wValue = 0x0211
wIndex = 0x0001

bEndpointAddress = 0x82

isDetached = False
device = None

def connect():
    global device, isDetached
    
    device = usb.core.find(idVendor=idVendor, idProduct=idProduct)

    if device is None:
        print('USB device not found!')
        sys.exit(1)

    if device.is_kernel_driver_active(wIndex):
        device.detach_kernel_driver(wIndex)
        isDetached = True

def disconnect():
    usb.util.dispose_resources(device)
    if isDetached:
        device.attach_kernel_driver(wIndex)

def sendData(dataHex):
    device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, binascii.unhexlify(dataHex))
    device.read(bEndpointAddress, 20)

def sendColorCommand(colorHex, field = 0):
    fieldHex = format(field, '02x')
    commandHex = colorCommand.format(fieldHex, colorHex)    
    sendData(commandHex)

connect()
sendColorCommand('ff0000')
disconnect()
