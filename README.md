# TEMPer
My repo for the TEMPer usb temperature sensor

The device shows up as 413d:2107 using lsusb.  This script is a modification of the try.py
script from python hidapi https://github.com/trezor/cython-hidapi

First install python hidapi:

```
sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
sudo pip install --upgrade setuptools
sudo pip install hidapi
```

Then connect the TEMPer and run the script.
