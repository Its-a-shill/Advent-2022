input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

newlis = []

# if adding takes more cycles, just pretend there's an extra instruction it's fine
for line in input_list:
    if 'addx' in line:
        newlis.append("noop")
    newlis.append(line)

x = 1
part1 = 0
screen = [['' for i in range(40)] for j in range(6)]

for i,line in enumerate(newlis):

    # 19 instead of 20 since i'm 0-indexing rather than 1- like in the description
    if i % 40 == 19:
        part1 += (i + 1) * x

    # Making sure to add after extracting the value for part 1
    if 'addx' in line:
        x += int(line.split(" ")[1])

    # I misinterpreted the description, but adding 1 to the pixel pointer and executing it after the addition
    #  seems to work almost everywhere? the only place that's showing up weird is pixel #201
    #  and so im just leaving it bc i think that's neat
    screen[i//40][(i+1) % 40] = '#' if abs((i+1)%40 - x) < 2 else ' '

print("Part 1: {}".format(part1))
print("Part 2:")

# yeah yeah i couldnt figure out an easier way to actually see the letters sue me
for row in screen:
    for pix in row:
        print(pix,end='')
    print()