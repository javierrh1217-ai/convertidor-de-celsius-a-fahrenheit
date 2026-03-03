def celsius_a_fahrenheit(c):
    """
    Convierte grados Celsius a Fahrenheit.

    Parámetros:
    c (int o float): temperatura en grados Celsius.

    Retorna:
    float: temperatura convertida a Fahrenheit.

    Lanza:
    TypeError: si el valor no es numérico.
    """

    if not isinstance(c, (int, float)):
        raise TypeError("La temperatura debe ser un número.")

    return (c * 9/5) + 32