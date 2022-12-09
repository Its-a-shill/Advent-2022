input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

grid = []
for line in input_list:
    grid.append([int(x) for x in line])

count = 0
best = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        sad = [True,True,True,True]
        # views = [max(i,1),max(len(grid)-i-1,1),max(j,1),max(len(grid[i])-j-1,1)]
        views = [i,len(grid)-i-1,j,len(grid[i])-1-j]
        for k in range(i-1,-1,-1):
            if grid[k][j] >= grid[i][j]:
                sad[0] = False
                views[0] = i-k
                break
        for k in range(i+1,len(grid)):
            if grid[k][j] >= grid[i][j]:
                sad[1] = False
                views[1] = k-i
                break
        for k in range(j-1,-1,-1):
            if grid[i][k] >= grid[i][j]:
                sad[2] = False
                views[2] = j-k
                break
        for k in range(j+1,len(grid[i])):
            if grid[i][k] >= grid[i][j]:
                sad[3] = False
                views[3] = k-j
                break
        if sad[0] or sad[1] or sad[2] or sad[3]:
            count += 1
        if views[0] * views[1] * views[2] * views[3] > best:
            best = views[0] * views[1] * views[2] * views[3]
print("Part 1: {}".format(count))
print("Part 2: {}".format(best))