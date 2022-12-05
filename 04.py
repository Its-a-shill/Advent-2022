input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

count1 = 0
count2 = 0
for line in input_list:
    assigns = line.split(',')
    dat = []
    for a in assigns:
        x = a.split('-')
        dat.append([int(y) for y in x])

    if dat[0][0] <= dat[1][1] and dat[1][0] <= dat[0][1]:
        count2 += 1

    if dat[0][0] <= dat[1][0] and dat[0][1] >= dat[1][1]:
        count1 += 1
        continue
    if dat[0][0] >= dat[1][0] and dat[0][1] <= dat[1][1]:
        count1 += 1

print("Part 1: {}".format(count1))
print("Part 2: {}".format(count2))