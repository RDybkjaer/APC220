import usb.core
import usb.util
import serial


vendor_id = 0x10C4
product_id = 0xEA60

test = False


def main():
    print("Bonjour world")
    #Vi starter initialiseringen af en Seriel forbindelse - Her benyttes pySerial biblioteket
    ser = serial.Serial()
    # Til serial i linux benyttes portene /dev/ttyUSB0
    # "/dev/ttyUSB0"
    ser.port = "/dev/ttyUSB0"
    #Godt nok er parity som standard sat til N, men for god ordens skyld
    ser.parity = "N"
    #Her sættes en timeout for, da jeg havde problemer med at den læste for evigt
    ser.timeout = 5
    ser.baudrate = 9600
    #Porten åbnes officielt
    ser.open()
    print("Serial data: " + str(ser))
    #Test om porten er åben
    sio = ser.is_open
    print("Is open: " + str(sio))
    #Test om porten kan skrives til
    swa = ser.writable()
    print("Is writeable: " + str(swa))
    #Test om porten kan læses fra
    sra = ser.readable()
    print("Is readable: " + str(sra))

    #Her sendes Hello World 5 gange
    print("Sent begin")
    msg = "A"
    print(type(msg))
    msg = msg.encode('utf-8')
    print(type(msg))
    print(msg)
    print("Sent: " +str(msg))
    j = ser.write(msg)
    print("Has written: " + str(j))

    sett = ser.get_settings()
    print(sett)

    print("The end!")


if __name__ == "__main__":
    main()

#USB bus data:
# Bus 001 Device 006: ID 10c4:ea60 Silicon Labs CP210x UART Bridge

"""
DEVICE ID 10c4:ea60 on Bus 001 Address 007 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x110 USB 1.1
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0x10c4
 idProduct              : 0xea60
 bcdDevice              :  0x100 Device 1.0
 iManufacturer          :    0x1 Error Accessing String
 iProduct               :    0x2 Error Accessing String
 iSerialNumber          :    0x3 Error Accessing String
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 100 mA ==================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x20 (32 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0x80 Bus Powered
   bMaxPower            :   0x32 (100 mA)
    INTERFACE 0: Vendor Specific ===========================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :   0xff Vendor Specific
     bInterfaceSubClass :    0x0
     bInterfaceProtocol :    0x0
     iInterface         :    0x2 Error Accessing String
      ENDPOINT 0x81: Bulk IN ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
      ENDPOINT 0x1: Bulk OUT ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x1 OUT
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
"""
