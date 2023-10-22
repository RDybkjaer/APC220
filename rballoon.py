import APC220 as apc220
from spongebobcase import tospongebob


def main():
    radio = apc220.ADC220()
    print("Waiting for sync message!")
    radio.receive(timeout=None)
    print("Synced! - beginning cycle")
    while(1):
        res = radio.receive(timeout = 10)
        if(""!=res):
            print("Received something!")
            ReS = tospongebob(res)
            print("CMP: "+ str(res) +" - " +str(ReS))
            radio.transmit(ReS)
        else:
            print("Timed out - Sending telemetry!")
            radio.transmit("Tel!")
        print("The end!")
    radio.close()


if __name__ == "__main__":
    main()
