import APC220 as apc220


def main():
    res:str
    ReS:str

    radio = apc220.ADC220()
    print("Waiting for sync message!")
    radio.receive(timeout=None)
    print("Synced! - beginning cycle")
    while(1):
        res = radio.receive(timeout = 10)
        if(""!=res):
            print("Received: "+str(res))
            ReS = res.capitalize()
            radio.transmit(ReS)
        else:
            print("Timed out - Sending telemetry!")
            radio.transmit("telemetry")
        print("The end!")
    radio.close()


if __name__ == "__main__":
    main()
