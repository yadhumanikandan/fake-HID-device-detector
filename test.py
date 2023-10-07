import usb.core

busses = usb.core.busses()
for bus in busses:
    devices = bus.core.devices
    for dev in devices:
        #if "respberry" in dev.filename.lower():
        print(f"Device: {dev.filename}")
        print(f"idVendor: {dev.idVendor} (0x{dev.idVendor:x})")
        print(f"idProduct: {dev.idProduct} (0x{dev.idProduct:x})")
