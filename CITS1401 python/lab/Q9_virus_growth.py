def virus_growth(num,rate,hour,time):
    times = time / hour
    factor = rate ** times
    return num * factor