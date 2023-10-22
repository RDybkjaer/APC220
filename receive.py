import APC220


def main():
    adc = ADC220.ADC220()
    adc.receive()

    print("The end!")
    adc.close()


if __name__ == "__main__":
    main()
