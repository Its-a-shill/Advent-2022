input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

class Monkey:
    def __init__(self,it,pow,times,plus,test,tthrow,fthrow):
        self.items = it
        self.plu = plus
        self.tim = times
        self.pow = pow
        self.test = test
        self.tthrow = tthrow
        self.fthrow = fthrow
        self.inspects = 0

    def process_items(self,part1):
        output = []

        for item in self.items:
            self.inspects += 1
            newval = item**self.pow*self.tim + self.plu

            newval //= 3 if part1 else 1

            newval %= space
            if newval % self.test == 0:
                output.append([newval,self.tthrow])
            else:
                output.append([newval,self.fthrow])
        self.items = []
        return output

    def add_item(self,newitem):
        self.items.append(newitem)

def create_monkeys():
    return [Monkey([52,60,85,69,75,75],1,17,0,13,6,7),
           Monkey([96,82,61,99,82,84,85],1, 1, 8, 7, 0, 7),
           Monkey([95, 79],1, 1, 6, 19, 5, 3),
           Monkey([88, 50, 82, 65, 77],1, 19, 0, 2, 4, 1),
           Monkey([66, 90, 59, 90, 87, 63, 53, 88],1, 1, 7, 5, 1, 0),
           Monkey([92,75,62],2,1,0,3,3,4),
           Monkey([94,86,76,67],1,1,1,11,5,2),
           Monkey([57],1,1,2,17,6,2),
           ]


    # return [Monkey([79,98],1,19,0,23,2,3),
    #            Monkey([54,65,75,74],1,1,6,19,2,0),
    #            Monkey([79,60,97],2,1,0,13,1,3),
    #            Monkey([74],1,1,3,17,0,1)]

monkeys = create_monkeys()

space = 1
for m in monkeys:
    space *= m.test

for round in range(20):
    for m in monkeys:
        throws = m.process_items(True)
        for item in throws:
            monkeys[item[1]].add_item(item[0])

vals = sorted([m.inspects for m in monkeys])
print("Part 1: {}".format(vals[-1]*vals[-2]))

monkeys = create_monkeys()

for round in range(10**4):
    for m in monkeys:
        throws = m.process_items(False)
        for item in throws:
            monkeys[item[1]].add_item(item[0])
        # print(throws)

vals = sorted([m.inspects for m in monkeys])
print("Part 2: {}".format(vals[-1]*vals[-2]))


