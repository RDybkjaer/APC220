import serial


class ADC220(serial.Serial):
    endchar: bytes

    def __init__(self, endchar: bytes = b"!#"):
        super().__init__()
        self.endchar = endchar
        # Til serial i linux benyttes portene /dev/ttyUSB0
        # "/dev/ttyUSB0"
        # self.s = serial.Serial()
        self.port = "/dev/ttyUSB0"
        # Godt nok er parity som standard sat til N, men for god ordens skyld
        self.parity = "N"
        # Her sættes en timeout for, da jeg havde problemer med at den læste for evigt
        self.timeout = 10
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
        msg = msg + self.endchar
        msg = msg.encode("utf-8")
        print(type(msg))
        print(msg)
        print("Sent: " + str(msg))
        j = self.write(msg)
        print("Has written: " + str(j))

    def receive(self) -> bytes:
        # Her sendes Hello World 5 gange
        print("Ready 2 read")
        # Læser 5 bytes
        r = self.read_until()
        print(type(r))
        print(r)
        b = r.decode("utf-8")
        print(type(b))
        print("Read: " + b)
        return b
