input_list = [l.rstrip('\n') for l in open("input.txt","r")]
# input_list = [l.rstrip('\n') for l in open("testinput.txt","r")]

parent = {}
data = {"/":[]}
sizes = {}
curr = "/"
# curr_str = ""

def parse(line):
    global curr
    if line[:2] == "$ ":
        if line[2:4] == "cd":
            if line[5:] == "..":
                curr = parent[curr]
                return
            curr = build_str(line[5:])
            return
    elif line != "":
        dat = line.split(" ")
        filestr = build_str(dat[1])
        # print(filestr)
        if dat[0] == "dir":
            data[curr].append(filestr)
            parent[filestr] = curr
            if filestr not in data:
                data[filestr] = []
            return
        else:
            sizes[filestr] = int(dat[0])
            data[curr].append(filestr)
    return

def calc_size(dir):
    if dir in sizes:
        return sizes[dir]

    s = sum(calc_size(child) for child in data[dir])
    sizes[dir] = s
    return s

def build_str(dir):
    if dir == '/':
        return '/'
    return curr[1:] + '/' + dir

for line in input_list:
    parse(line)
    # print(curr)
print(data)

output = 0
for dir in data:
    size = calc_size(dir)
    if size < 1e5:
        output += size

print(output)

minsize = 1e8
mindir = '/'
for d in sizes:
    if calc_size('/') - 4e7 - calc_size(d) < 0 and calc_size(d) < minsize:
        minsize = calc_size(d)
        mindir = d
print(minsize)