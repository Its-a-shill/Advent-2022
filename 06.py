input_list = [l.rstrip('\n') for l in open("input.txt","r")]

for line in input_list:
    for part,k in enumerate((4,14)):
        for i in range(len(line)):
            if len(set(line[i:i+k])) == k:
                print("Part {}: {}".format(part+1,i+k))
                break