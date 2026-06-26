def calculate_risk(vt, abuse, otx):

    score = 0

    if vt > 0:

        score += min(vt * 10, 50)

    if abuse > 0:

        score += min(abuse // 2, 30)

    if otx > 0:

        score += min(otx, 20)

    return min(score, 100)