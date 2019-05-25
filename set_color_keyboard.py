import usb.core
import usb.util
import binascii
import time

standardColorhex = 'ff0000'
idVendor = 0x046d
idProduct = 0xc336
initialCommand = '11ff0c0d00000000000000000000000000000000'
colorRedCommand = '11ff0c3d0001ff00000200000000000000000000'


bmRequestType = 0x21
bmRequest = 0x09
wValue = 0x0211
wIndex = 0x0001

device = usb.core.find(idVendor=idVendor, idProduct=idProduct)

if device.is_kernel_driver_active(wIndex):
    device.detach_kernel_driver(wIndex)

if device is None:
    print('USB device not found!')
    exit(0)

device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, binascii.unhexlify(initialCommand))
time.sleep(0.1)
retorno = device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, binascii.unhexlify(colorRedCommand))
time.sleep(0.1)
retorno = device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, 20)

#endpoint = device[0][(0,0)][0]
#print(endpoint)

usb.util.dispose_resources(device)
device.attach_kernel_driver(wIndex)