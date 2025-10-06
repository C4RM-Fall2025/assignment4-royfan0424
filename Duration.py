def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    c = face * couponRate / ppy
    r = y / ppy

    price = 0.0
    t_pv_sum = 0.0
    for t in range(1, n + 1):
        cf = c if t < n else (c + face)
        pv = cf / (1 + r)**t
        price += pv
        t_pv_sum += t * pv

    duration_years = (t_pv_sum / price) / ppy
    return duration_years

y = 0.03
face = 2_000_000
couponRate = 0.04
m = 10

print(getBondDuration(y, face, couponRate, m, ppy=1))

