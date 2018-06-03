from __future__ import print_function

import hid
import time

# enumerate USB devices

path = None

for d in hid.enumerate():
    keys = list(d.keys())
    keys.sort()
    if d["product_id"] == 8455 and d["interface_number"] == 1:
        print("Found the temper")
        path = d["path"]
        break
    #for key in keys:
    #print("%s : %s" % (key, d[key]))

print("path ", path)

# try opening a device, then perform write and read


if path:
 try:
    print("Opening the device")

    h = hid.device()
    #413d:2107
    #h.open(0x413d, 0x2107) # TREZOR VendorID/ProductID
    h.open_path(path)

    #print("Manufacturer: %s" % h.get_manufacturer_string())
    #print("Product: %s" % h.get_product_string())
    #print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    #h.set_nonblocking(1)

    # write some data to the device
    #print("Write the data")
    while True:
    
        h.write([0, 1, 0x80, 0x33, 0x1] + [0] * 4)

        # wait
        time.sleep(0.05)

        # read back the answer
        #print("Read the data")
        d = h.read(20, 4000)
        if not d:
            continue
            #print("no data")

        print(d)
        temp = ((int(d[2]) << 8) + int(d[3])) / 100.0
        temp = temp*9.0/5.0 + 32.0

        humidity = ((int(d[4]) << 8) + int(d[5])) / 100.0

        print("Temp is ", temp, " humidity is ", humidity)
        time.sleep(1)
    h.close()

 except IOError as ex:
    print(ex)
    print("You probably don't have the hard coded device. Update the hid.device line")
    print("in this script with one from the enumeration list output above and try again.")

print("Done")

