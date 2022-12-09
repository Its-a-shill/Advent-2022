from numpy import sign

input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

decode = {'R':(0,1),'U':(-1,0),'D':(1,0),'L':(0,-1)}

def move_link(front, back):
    newback = [0, 0]

    # Lazy way to check both horizontals and verticals
    for k in range(2):
        m = 1-k
        if front[k] == back[k]:

            # So if they're aligned in one axis and far apart in the other, move the tail
            if abs(front[m] - back[m]) > 1:
                s = sign(-front[m] + back[m])
                newback[k] = front[k]
                newback[m] = front[m] + s
                return newback

            # If they're aligned in one axis and close in the other, do nothing
            else:
                return back

    # If they're touching diagonally, do nothing
    if abs(-front[0] + back[0])+abs(-front[1] + back[1]) < 3:
        return back

    # If they're not touching and skew (only remaining option), move back diagonally
    s = (sign(-front[0] + back[0]), sign(-front[1] + back[1]))
    newback = [back[j] - s[j] for j in range(2)]

    # Oh what's this the original names before I retconned it post-finish to make it a little cleaner
    # print('\t',headpos,tailpos,newtailpos,s)
    return newback

# Function added later to combine the behavior of part 1 and part 2
def process(length):

    # For part 1 i had this as 2 variables, 'head' and 'tail'
    # Apparently i went from 443rd to 68th in part 2 so i guess this change was easier than what other ppl thought
    ropes = [[0,0] for i in range(length)]
    hits = set()

    for line in input_list:

        # Python split my beloved
        vals = line.split(' ')
        for i in range(int(vals[1])):
            ropes[0] = [ropes[0][j] + decode[vals[0]][j] for j in range(2)]
            for i in range(1,length):
                ropes[i] = move_link(ropes[i - 1], ropes[i])
            hits.add(tuple(ropes[-1]))

    return(len(hits))

print("Part 1: {}".format(process(2)))
print("Part 2: {}".format(process(10)))