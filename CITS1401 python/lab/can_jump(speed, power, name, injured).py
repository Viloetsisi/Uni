def can_jump(speed, power, name, injured):
    if injured == False:
        distance = speed * power
    if injured == True:
        distance = speed * power * 0.8
    if distance < 1:
        return(name + ' made a false attempt!')
    else:
        return (name+' can jump '+ str('%.2f'%distance) + 'm!')
