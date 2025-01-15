def check_temperature(temperature, limit):
    fahrenheit = temperature * 9 / 5 + 32
    if limit > fahrenheit:
        return True
    else:
        return False