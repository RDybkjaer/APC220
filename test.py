def main():
    # En int er 32 bit (4 byte) - en float er 64 byte
    # Benyttes en byte til skalar, kan en int benyttes som encoding af float - Sketch IK meeen
    # kan virke op til værdier af 16777216

    flat: float = 1677.123456789
    Skub = 4
    inte: int = 0
    mult = 10**Skub
    print(mult)

    flatint = int(flat * mult)
    print(bin(flatint))
    flatint = flatint | (Skub << 24)

    multback = 10 ** (flatint >> 24)
    print(multback)
    flatback = float((flatint & 0x00FFFFFF) / multback)

    print(flatback)


if __name__ == "__main__":
    main()
