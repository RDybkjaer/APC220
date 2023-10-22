import APC220 as apc220

def main():
    received: str
    toReturn: str
    #Initialiserer serialforbindelsen til radioen
    radio = apc220.ADC220()

    #Modtager en besked - timer out hvis den ikke kommer
    #indenfor 20 sekunder
    received = radio.receive(timeout = 20)
    
    #Hvis 
    if(""!=received):
        print("Received: "+str(received))
        #Capitaliser for at sende noget andet tilbage
        toReturn = received.capitalize()
        #Transmitter det capitalized resultat tilbage
        radio.transmit(toReturn)
    else:
        #Hvis received == "", er det FORMODENLIGT fordi den timer ud.
        #TODO: Vi skal lige være sikre på at det passer :P
        print("Timed out!")
    print("The end!")
    radio.close()


if __name__ == "__main__":
    main()
