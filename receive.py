import APC220 as apc220


def main():
    radio = apc220.ADC220()
    radio.receive()

    print("The end!")
    radio.close()


if __name__ == "__main__":
    main()
