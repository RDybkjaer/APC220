import APC220 as apc220


def main():
    print("|START|")
    msg: str
    # Opretter in instans af ADC220 klassen
    radio = apc220.ADC220()
    # Henter et input fra terminalen
    msg = radio.terminalInput(timeout=None)
    # Random matches for testing purposes
    if "TO" != msg:
        radio.transmit(msg)
    radio.receive(timeout=20)


if __name__ == "__main__":
    main()
