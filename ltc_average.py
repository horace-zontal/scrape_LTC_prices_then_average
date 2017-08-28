with open('ltcscraped.txt') as fh:
    sum = 0
    count = 0
    for line in fh:
        count += 1
        sum += float(line.split()[1])
    average = sum / count

    print average

    fh = open("average.txt", "a")
    av_price = average
    fh.write(str(av_price))
    fh.close()


