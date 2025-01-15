def nextRound(k,scores):
    point = scores[k-1]
    count = 0
    for i in scores:
        if i >= point and i > 0:
            count += 1
    return count