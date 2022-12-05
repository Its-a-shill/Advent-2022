input_list = [l.rstrip('\n') for l in open("input.txt","r")]

elves = [0]
for line in input_list:
    if line == '':
        elves.append(0)
    else:
        elves[-1] += int(line)

print("Part 1: {}".format(max(elves)))
print("Part 2: {}".format(sum(sorted(elves)[-3:])))