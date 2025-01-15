def hunting_animals(weather, animal, n):
    if weather == 'sunny':
        if animal == 'rabbit':
            return n
        if animal == 'deer':
            return (n // 2)
    if weather == 'rainy':
        if animal == 'rabbit':
            return (n // 2)
        if animal == 'deer':
            return (n // 3)