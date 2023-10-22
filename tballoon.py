import APC220 as apc220


def main():
    # BUG: Det virker som om at den sender to gange - det forstår jeg ikke helt endnu
    print("|START|")
    msg: str
    # Opretter in instans af ADC220 klassen
    radio = apc220.ADC220()
    radio.transmit("Syncword")
    # Henter et input fra terminalen
    while 1:
        msg = None
        input = None
        input = radio.terminalInput()
        # Random matches for testing purposes
        match input:
            case "1":
                msg = "Gutentag welt"
            case "2":
                msg = "Bonjour World"
            case "3":
                msg = "Hej Verden"
            case "TO":
                msg = None
            case _:
                msg = "Hello world"
        #Kigger efter timeout:
        #Hvis ikke timeout, send data - Ellers bare lyt :D
        if None != msg:
            print("\tNot timed out!")
            radio.transmit(msg)
        # Venter på feedback
        radio.receive(timeout=3)


if __name__ == "__main__":
    main()
