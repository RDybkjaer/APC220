import APC220 as apc220


def main():
    resceived:str
    toBeReturned:str

    #Initialiserer radioen
    radio = apc220.ADC220()

    #Vi starter med at lede for evigt efter en sync msg
    #For at synkronisere timeouts
    print("Waiting for sync message!")
    radio.receive(timeout=None)
    print("Synced! - beginning cycle")
    #Infitie loop :D til telemetry stuff
    while(1):
        # Venter på at modtage data
        resceived = radio.receive(timeout = 10)
        #Hvis data er modtaget indenfor 10 sekunder
        if(""!=resceived):
            print("Received: "+str(resceived))
            #Kapitaliserer for testing reasons
            toBeReturned = resceived.capitalize()
            #Transmitter resultatet tilbage
            radio.transmit(toBeReturned)
        else:
            #Sender telemetry efter 10 sekunder
            print("Timed out - Sending telemetry!")
            radio.transmit("telemetry")
        print("The end!")
    #Skulle aldrig nå her
    radio.close()


if __name__ == "__main__":
    main()
