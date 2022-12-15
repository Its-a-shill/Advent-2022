from numpy import sign

input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

filled = set()

# Every way the sand will try to drop, in order
movements = ((0,1),(-1,1),(1,1))
tot_count = 0

def drop_sand():
    global tot_count, floor
    pos = [500,0]

    # Exit condition for part 2
    if tuple(pos) in filled:
        return False

    rest = False
    while pos[1] < floor and not rest:
        rest = True

        # Drops to a valid location, or says we're stuck if there are no valid locations
        for m in movements:
            nextpos = [pos[i] + m[i] for i in range(2)]
            if tuple(nextpos) not in filled:
                pos = nextpos
                rest = False
                break

    if rest:
        filled.add(tuple(pos))
        tot_count += 1

    # Only returns false if we exited the loop for a non-rest reason, i.e. falling below where the floor would be to finish part 1
    return rest

floor = 0

for line in input_list:
    path = [eval(x) for x in line.split(' -> ')]
    for pt in path:
        floor = max(2 + pt[1], floor)

    for i in range(len(path)-1):
        if path[i][0] == path[i+1][0]:
            s = sign(path[i+1][1]-path[i][1])
            for j in range(path[i][1],path[i+1][1]+s,s):
                filled.add((path[i][0],j))
                # print((path[i][0],j))
        else:
            s = sign(path[i + 1][0] - path[i][0])
            for j in range(path[i][0],path[i+1][0]+s,s):
                filled.add((j,path[i][1]))
                # print((j,path[i][1]))


while drop_sand():
    continue
print("Part 1: {}".format(tot_count))

# Adds in the floor
# A better bound would be [500-floor, 500+floor] but this also works for any floor < 500 so we're fine
for i in range(1000):
    filled.add((i,floor))

while drop_sand():
    continue
print("Part 2: {}".format(tot_count))