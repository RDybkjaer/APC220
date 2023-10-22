import ADC220 as adc


def main():
    print("Bonjour world")
    # Vi starter initialiseringen af en Seriel forbindelse - Her benyttes pySerial biblioteket
    radio = adc.ADC220()
    radio.send("Hello world! \nI am a test message")


if __name__ == "__main__":
    main()
