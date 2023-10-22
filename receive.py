import APC220 as apc220

def main():
    res: str
    ReS: str
    #Initialiserer serialforbindelsen til radioen
    radio = apc220.ADC220()
    #
    res = radio.receive(timeout = 20)
    if(""!=res):
        print("Received something!")
        ReS = res.capitalize()
        radio.transmit(ReS)
    else:
        print("Timed out!")
    print("The end!")
    radio.close()


if __name__ == "__main__":
    main()
