import APC220 as apc220


def main():
    print("Bonjour world")
    # Vi starter initialiseringen af en Seriel forbindelse - Her benyttes pySerial biblioteket
    radio = apc220.ADC220()
    msg = radio.terminalInput()
    radio.transmit(msg)
    radio.receive()


if __name__ == "__main__":
    main()
