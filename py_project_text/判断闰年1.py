year = 2000
while year <= 2020:
    (i, j) = divmod(year, 4)
    if j != 0:
        print("%d 不是闰年" % year, end=" ")
    else:
        (i, j) = divmod(year, 100)
        if j != 0:
            print("%d 是闰年" % year)
        else:
            (i, j) = divmod(year, 400)
            if j == 0:
                print("%d 是闰年" % year)
            else:
                print("%d 不是闰年" % year, end=" ")
                print("")
    year += 1

