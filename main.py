def celsius_a_fahrenheit(c):
    if not isinstance(c, (int, float)):
        raise TypeError("La temperatura debe ser un número.")
    return (c * 9/5) + 32


if __name__ == "__main__":
    print("0°C =", celsius_a_fahrenheit(0), "°F")
