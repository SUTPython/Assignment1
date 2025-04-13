soldiers = int(input())
p1, p2, d1, d2 = 0, 0, 0, 0
subsoldier = 1
cnt = 0
while soldiers > 0:
    if (subsoldier >= soldiers):
        cnt += soldiers
        if (soldiers % 2 == 0):
            p1, p2 = p1 + (soldiers // 2), p2 + (soldiers // 2)
        else:
            if cnt % 2 == 0:
                p1, p2 = p1 + (soldiers // 2), p2 + (soldiers // 2) + 1
            else:
                p1, p2 = p1 + (soldiers // 2) + 1, p2 + (soldiers // 2)
        break
    else:
        cnt += subsoldier

        if (subsoldier % 2 == 0):
            p1, p2 = p1 + (subsoldier // 2), p2 + (subsoldier // 2)
        else:
            if cnt % 2 == 0:
                p1, p2 = p1 + (subsoldier // 2), p2 + (subsoldier // 2) + 1
            else:
                p1, p2 = p1 + (subsoldier // 2) + 1, p2 + (subsoldier // 2)

    soldiers -= subsoldier
    subsoldier += 4
    if (subsoldier >= soldiers):
        cnt += soldiers
        if (soldiers % 2 == 0):
            d1, d2 = d1 + (soldiers // 2), d2 + (soldiers // 2)
        else:
            if cnt % 2 == 0:
                d1, d2 = d1 + (soldiers // 2), d2 + (soldiers // 2) + 1
            else:
                d1, d2 = d1 + (soldiers // 2) + 1, d2 + (soldiers // 2)
        break
    else:
        cnt += subsoldier
        if (subsoldier % 2 == 0):
            d1, d2 = d1 + (subsoldier // 2), d2 + (subsoldier // 2)
        else:
            if cnt % 2 == 0:
                d1, d2 = d1 + (subsoldier // 2), d2 + (subsoldier // 2) + 1
            else:
                d1, d2 = d1 + (subsoldier // 2) + 1, d2 + (subsoldier // 2)

    soldiers -= subsoldier
    subsoldier += 4

print(p1, p2, d1, d2, sep="\t")