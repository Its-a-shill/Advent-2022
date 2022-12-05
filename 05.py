input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

def do_the_thing(reverse):
    flag = False
    stacks = [[] for i in range(10)]
    for line in input_list:
        if line != '' and not flag:
            for i in range(0,len(line),4):
                if line[i+1] == '1':
                    break
                if line[i+1] != ' ':
                    stacks[i//4].append(line[i+1])
        else:
            flag = True
            if len(line) > 0:
                stuff = line.split(' ')
                stacks[int(stuff[5])-1][0:0] = stacks[int(stuff[3])-1][:int(stuff[1])][::-1 if reverse else 1]
                stacks[int(stuff[3]) - 1][:int(stuff[1])] = []
            # print(stacks)

    output = ''
    for s in stacks:
        if len(s) > 0:
            output += s[0]

    return output

print("Part 1: {}".format(do_the_thing(True)))
print("Part 2: {}".format(do_the_thing(False)))