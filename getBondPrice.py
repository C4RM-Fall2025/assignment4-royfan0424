def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    c = face * couponRate / ppy
    discount_rate = y / ppy

    pv_coupons = 0
    for t in range(1, n + 1):
        pv_coupons += c / (1 + discount_rate)**t

    pv_face = face / (1 + discount_rate)**n

    bondPrice = pv_coupons + pv_face
    return bondPrice
print(getBondPrice(0.03, 2000000, 0.04, 10, 1))
print(getBondPrice(0.03, 2000000, 0.04, 10, 2))


