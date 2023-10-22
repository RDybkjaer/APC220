import APC220 as apc220
import spongebobcase


def main():
    radio = apc220.ADC220()
    res = radio.receive(timeout = 20)
    if(""!=res):
        print("Received something!")
        ReS = spongebobcase.tospongebob(res)
        radio.transmit(ReS)
    else:
        print("Timed out!")
    print("The end!")
    radio.close()


if __name__ == "__main__":
    main()
