input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

heightmap = [[0 for x in input_list[0]] for y in input_list]
start = [0,0,0]
end = [0,0]

# Initializes the heightmap
for i,line in enumerate(input_list):
    for j,c in enumerate(line):
        if c == 'S':
            heightmap[i][j] = 1
            start = [i,j,0]
        elif c == 'E':
            heightmap[i][j] = 26
            end = [i,j,0]
        else:
            heightmap[i][j] = ord(c) - 96


dirs = ((0,-1,1),(-1,0,1),(1,0,1),(0,1,1))


# Does part 1, starting at the start and going until it hits the end
boundary = [start]
hits = set(tuple(start[2:]))
complete = False
while not complete:
    curr = boundary[0]
    boundary = boundary[1:]
    for d in dirs:
        next_loc = [curr[i] + d[i] for i in range(3)]

        # Makes sure we don't leave the grid
        if 0 <= next_loc[0] < len(heightmap) and 0 <= next_loc[1] < len(heightmap[0]):

            # Makes sure the next position isn't too high
            if tuple(next_loc[:2]) not in hits and heightmap[next_loc[0]][next_loc[1]] <= heightmap[curr[0]][curr[1]] + 1:
                if next_loc[:2] == end[:2]:
                    print("Part 1: {}".format(next_loc[2]))
                    complete = True
                boundary.append(next_loc)

                hits.add(tuple(next_loc[:2]))


# Does part 2, starting at the end and going backwards until it hits a height of 1
boundary = [end]
hits = set(tuple(end[2:]))
complete = False
while not complete:
    curr = boundary[0]
    # print(curr,boundary)
    boundary = boundary[1:]
    for d in dirs:
        next_loc = [curr[i] + d[i] for i in range(3)]
        if 0 <= next_loc[0] < len(heightmap) and 0 <= next_loc[1] < len(heightmap[0]):
            # print(heightmap[next_loc[0]][next_loc[1]])
            if tuple(next_loc[:2]) not in hits and heightmap[next_loc[0]][next_loc[1]] + 1>= heightmap[curr[0]][curr[1]]:
                if heightmap[next_loc[0]][next_loc[1]] == 1:
                    print("Part 2: {}".format(next_loc[2]))
                    complete = True
                boundary.append(next_loc)

                hits.add(tuple(next_loc[:2]))