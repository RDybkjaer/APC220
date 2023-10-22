import serial

# @TODO: Skriv kommentarer :P


class ADC220(serial.Serial):
    delim: str
    defaulttimeout: int

    def __init__(self, delim: str = "#!", defaulttimeout: int = 10):
        # Opsætter delimimiter, som er det/de tegn der skal læses til, før en læsning stoppes
        self.delim = delim

        # Kalder superklassens (serial.Serial) init metode
        super().__init__()

        # Til serial i linux benyttes portene /dev/ttyUSB0
        self.port = "/dev/ttyUSB0"
        # Godt nok er parity som standard sat til N, men for god ordens skyld
        self.parity = "N"
        # Her sættes en timeout for, da jeg havde problemer med at den læste for evigt
        self.baudrate = 19200
        # Disabler CTS/RTS flow control, da det ikke er nødvendigt
        self.rtscts = False
        self.defaulttimeout = defaulttimeout
        self.timeout = defaulttimeout

        # Porten åbnes officielt
        self.open()
        print("Port is open")

    def opendata(self):
        # @BREIF: Åbner porten
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
        # Udskriver et print af setting
        conf = self.get_settings()
        print("Settings: " + str(conf))

    def transmit(self, msg):
        # Sammanesætter msg med delimiteren
        msg = msg + self.delim
        ##Omskriver det til unicode
        msg = msg.encode("utf-8")
        print("Message: " + str(msg))
        j = self.write(msg)
        if len(msg) == j:
            print("Message sent")
        else:
            print("Message not sent")

    def receive(self, timeout=-1) -> bytes:
        if -1 == timeout:
            self.timeout = self.defaulttimeout
        else:
            self.timeout = timeout
        # Enkoder endString til byte
        endChar = bytes(self.delim, "utf-8")
        # Læser indtil endChar er fundet
        b = self.read_until(expected=endChar)
        # Dekoder det til unicode
        read = b.decode("utf-8")
        # fjerner delimiteren fra strengen
        read.replace("#!", "")
        print("Read: " + read)
        return read

    def terminalInput(self):
        # NOTE: Denne metode er kun til test - Den er noget garbage
        print("Select function")
        inp = input()
        return inp
