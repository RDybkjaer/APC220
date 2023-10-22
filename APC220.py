import serial
import sys, select

# Import the libraries inputimeout, TimeoutOccurred
from inputimeout import inputimeout


class ADC220(serial.Serial):
    delim: str
    defaulttimeout: int
    callsign: str

    def __init__(
        self, delim: str = "#!", defaulttimeout: int = 10, callsign: str = "ABCDEF"
    ):
        # Opsætter delimimiter, som er det/de tegn der skal læses til, før en læsning stoppes
        self.delim = delim
        self.callsign = callsign

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
        j = self.write(msg)
        if len(msg) == j:
            print("\tMessage sent: " + str(msg))
        else:
            print("\tMessage not sent")

    def receive(self, timeout=-1) -> bytes:
        # Sætter en costum timeout
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
        read = read.removesuffix("#!")
        print("\tRead: " + read)
        return read

    def terminalInput(self, timeout: int = 9):
        # NOTE: input() fungerer fint, men jeg vil gerne have en timeout på den
        #      så vi kan receive telemetry fra tid til anden

        # Tyv stjålet fra https://www.geeksforgeeks.org/how-to-set-an-input-time-limit-in-python/
        # Try block of code
        # and handle errors
        try:
            # Take timed input using inputimeout() function
            time_over = inputimeout(prompt="Choose a function:", timeout=timeout)

        # Catch the timeout error
        except Exception:
            # Declare the timeout statement
            time_over = "TO"

        # Print the statement on timeoutprint(time_over)
        print(time_over)
        return time_over

    # treceive og ttransmit er test metoder, som ikke er i brug
    # Det er for at teste floats til bytes :D
    def treceive(self, timeout=-1) -> bytes:
        # Sætter en costum timeout
        if -1 == timeout:
            self.timeout = self.defaulttimeout
        else:
            self.timeout = timeout
        # Enkoder endString til byte
        endChar = bytes(self.delim, "utf-8")
        # Læser indtil endChar er fundet
        b = self.read_until(expected=endChar)
        # Dekoder det til unicode
        # fjerner delimiteren fra strengen
        print(b)
        read = read.removesuffix("#!")
        print("\tRead: " + read)
        return read

    def ttransmit(self, msg):
        # Sammanesætter msg med delimiterent
        testahest = 0.55
        print("Type of testahest: " + str(type(testahest)))
        # test = bytes.
        print("Type of test: " + test)
        msg = self.delim
        ##Omskriver det til unicode
        msg = msg.encode("utf-8")
        msg = test + msg
        j = self.write(msg)
        if len(msg) == j:
            print("\tMessage sent: " + str(msg))
        else:
            print("\tMessage not sent")
