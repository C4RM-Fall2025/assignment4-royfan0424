def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    coupon = face * couponRate
    for t, y in enumerate(yc, start=1):
        CF = coupon + face if t == m else coupon
        bondPrice += CF / ((1 + y) ** t)
    return bondPrice

yc = [0.010, 0.015, 0.020, 0.025, 0.030]
face = 2000000
couponRate = 0.04
m = 5

print(getBondPrice_E(face, couponRate, m, yc))

