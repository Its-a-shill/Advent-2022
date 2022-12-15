from numpy import sign

input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

# def testpacket(lis):
#     if isinstance(lis[0],int) and isinstance(lis[1],int):
#         return sign(lis[0] - lis[1])
#     elif isinstance(lis[0],list) and isinstance(lis[1],list):
#         for i in range(min(len(lis[0]),len(lis[1]))):
#             x = testpacket([lis[0][i],lis[1][i]])
#             if x != 0:
#                 return x
#             else:
#                 return testpacket([lis[]])
#     elif isinstance(lis[0],int):
#         return testpacket([[lis[0]],lis[1]])
#     else:
#         return testpacket([lis[0],lis[1]])

def attempt(a, b,depth=0):
    if a == b:
        return 0

    # print(a,b)
    if isinstance(a,int) and isinstance(b,int):
        return sign(a - b)

    if isinstance(a,list) and isinstance(b,list):
        # if depth > 25:
        #     print(a, b, "AAAA")
        #     return 0
        for i in range(min(len(a),len(b))):
            x = attempt(a[i], b[i],depth+1)
            if x != 0:
                return x
        return sign(len(a)-len(b))

    elif isinstance(a,int):
        return attempt([a], b,depth+1)
    else:
        return attempt(a, [b],depth+1)

count = 0
things = [0,0]
for i,line in enumerate(input_list):
    if i % 3 == 2:
        count -= min(attempt(things[0], things[1]), 0)*(i//3+1)
        # print(things)
        # print(attempt(things[0], things[1]))
        continue

    things[i % 3] = eval(line)

print("Part 1: {}".format(count))

full_dat = [[[2]],[[6]]]
for line in input_list:
    if line != '':
        full_dat.append(eval(line))

def quicksort(dat,start,end):
    if start >= end:
        return

    pivot = dat[(start+end)//2]
    pointers = [start,end]

    while pointers[0] < pointers[1]:
        while attempt(dat[pointers[0]],pivot) < 0:
            pointers[0] += 1
        while attempt(dat[pointers[1]],pivot) > 0:
            pointers[1] -= 1

        temp = dat[pointers[0]]
        dat[pointers[0]] = dat[pointers[1]]
        dat[pointers[1]] = temp

    if start >= pointers[0] or end <= pointers[1]:
        return

    quicksort(dat,start,pointers[1])
    quicksort(dat,pointers[0],end)

# print(attempt([], []))

quicksort(full_dat,0,len(full_dat)-1)
# for d in full_dat:
#     print(d)
print("Part 2: {}".format((full_dat.index([[2]])+1)*(full_dat.index([[6]])+1)))