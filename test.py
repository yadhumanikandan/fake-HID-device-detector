import usb.core

# Find USB devices
devices = usb.core.find(find_all=True)

# Print information about each device
for device in devices:
    print("Vendor ID: 0x{:04x}".format(device.idVendor))
    print("Product ID: 0x{:04x}".format(device.idProduct))
    print("Manufacturer:", usb.util.get_string(device, device.iManufacturer))
    print("Product:", usb.util.get_string(device, device.iProduct))
    print()
