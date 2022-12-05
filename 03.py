input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

def letter(c):
    if ord(c) >= 97:
        return ord(c) - 96
    else:
        return ord(c) - 38

packs = []
tot = 0
for line in input_list:
    packs.append([line[:len(line)//2] , line[len(line)//2:]])
    z = set(packs[-1][0]) & set(packs[-1][1])
    tot += letter(str(list(z)[0]))
print("Part 1: {}".format(tot))

tot = 0
for i in range(0,len(packs),3):
    z = (set(packs[i][0])|set(packs[i][1])) & (set(packs[i+1][0])|set(packs[i+1][1])) & (set(packs[i+2][0])|set(packs[i+2][1]))
    # print(z, packs[i])
    if len(z) > 0:
        tot += letter(str(list(z)[0]))
    else:
        print(i)
        print(packs[i])
        print(packs[i+1])
        print(packs[i+2])
print("Part 2: {}".format(tot))