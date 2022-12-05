input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

scores = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}
scores2 = [3,1,2]
wins = ('A Y','B Z','C X')
draws = ('A X','B Y','C Z')

tot_score = 0
for line in input_list:
    tot_score += scores[line[-1]]
    if line in wins:
        tot_score += 6
    if line in draws:
        tot_score += 3

print("Part 1: {}".format(tot_score))

tot_score = 0
for line in input_list:
    if line[-1] == 'X':
        tot_score += (scores2[(scores[line[0]] - 1) % 3])
    if line[-1] == 'Y':
        tot_score += (scores2[(scores[line[0]]) % 3]) + 3
    if line[-1] == 'Z':
        tot_score += (scores2[(scores[line[0]]+1) % 3]) + 6
print("Part 2: {}".format(tot_score))