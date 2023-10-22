import serial


class ADC220(serial.Serial):
    endString: str
    timeout = 10

    def __init__(self, endString: str = "!#"):
        super().__init__()
        self.endString = endString
        # Til serial i linux benyttes portene /dev/ttyUSB0
        self.port = "/dev/ttyUSB0"
        # Godt nok er parity som standard sat til N, men for god ordens skyld
        self.parity = "N"
        # Her sættes en timeout for, da jeg havde problemer med at den læste for evigt
        self.baudrate = 9600
        self.rtscts = False
        # Porten åbnes officielt
        self.open()
        print("Serial data: " + str(self))
        # Test om porten er åben
        sio = self.is_open
        print("Is open: " + str(sio))
        # Test om porten kan skrives t
        swa = self.writable()
        print("Is writeable: " + str(swa))
        # Test om porten kan læses fra
        sra = self.readable()
        print("Is readable: " + str(sra))

    def send(self, msg):
        print(type(msg))
        msg = msg + self.endString
        msg = msg.encode("utf-8")
        print(type(msg))
        print(msg)
        print("Sent: " + str(msg))
        j = self.write(msg)
        print("Has written: " + str(j))

    def receive(self, to=timeout) -> bytes:
        # Her sendes Hello World 5 gange
        endChar = bytes(self.endString, "utf-8")
        print("Ready 2 read")
        print("Endchar: " + str(endChar))
        # Læser indtil endChar er fundet
        r = self.read_until(expected=endChar)
        print(type(r))
        print(r)
        b = r.decode("utf-8")
        print(type(b))
        print("Read: " + b)
        return b
