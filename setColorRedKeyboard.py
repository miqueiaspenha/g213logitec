import os
import sys
import usb.core
import usb.util
import binascii

os.environ['PYUSB_DEBUG'] = 'debug'

standardColorhex = 'ff0000'
#idVendor = 0x046d
idVendor = 0x13fe
#idProduct = 0xc336
idProduct = 0x1d00
wIndex = 0x0000
colorCommand = '11ff0c3a{}01{}0200000000000000000000'
fieldHex  = format(0, '02x')

bEndpointAddress = 0x82
bmRequestType = 0x21
bmRequest = 0x09
wValue = 0x0211

device = usb.core.find(idVendor=idVendor, idProduct=idProduct)
if device is None:
    print('USB device not found!')
    sys.exit(1)

if device.is_kernel_driver_active(wIndex):
    device.detach_kernel_driver(wIndex)

commandhex = colorCommand.format(fieldHex, standardColorhex)
device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, binascii.unhexlify(commandhex))
device.read(bEndpointAddress, 20)

usb.util.dispose_resources(device)
device.attach_kernel_driver(wIndex)