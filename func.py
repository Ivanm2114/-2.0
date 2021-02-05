def delta(toponym):
    also = toponym['boundedBy']['Envelope']
    upper_corn = list(map(float, also['upperCorner'].split()))
    lower_corn = list(map(float, also['lowerCorner'].split()))
    delta = str((((upper_corn[0] - lower_corn[0]) ** 2 + ((upper_corn[0] - lower_corn[0]) ** 2)) ** 0.5)/4)
    return delta


def count_dist(address_ll, org_point):
    a = abs(float(address_ll.split(',')[0]) - float(org_point.split(',')[0]))
    b = abs(float(address_ll.split(',')[1]) - float(org_point.split(',')[1]))
    dist = int((((a**2 + b**2)**0.5)*100000))
    return dist