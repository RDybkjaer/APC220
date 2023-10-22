import APC220 as apc220
import spongebobcase


def main():
    radio = apc220.ADC220()
    res = radio.receive()
    ReS = spongebobcase.tospongebob(res)
    radio.transmit(ReS)

    print("The end!")
    radio.close()


if __name__ == "__main__":
    main()
