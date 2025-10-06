def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    coupon = face * couponRate
    for t, y in zip(times, yc):
        CF = coupon + face if t == max(times) else coupon
        bondPrice += CF / ((1 + y) ** t)
    return bondPrice

yc = [0.010, 0.015, 0.020, 0.025, 0.030]
times = [1, 1.5, 3, 4, 7]
face = 2000000
couponRate = 0.04

print(getBondPrice_Z(face, couponRate, times, yc))
