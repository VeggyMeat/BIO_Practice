inpt = input()
on = ''
dim = ''
for item in inpt:
    if item.isupper():
        on += item.lower()
    else:
        dim += item

alph = 'abcdefghijklmnopqrstuvwxy'
grid = [list(alph[5 * x: 5 * (x + 1)]) for x in range(5)]

adjacent = [(1, 0), (0, 1), (0, -1), (-1, 0)]
connections = {}

for y, row in enumerate(grid):
    for x, item in enumerate(row):
        con = [item]
        for adj in adjacent:
            new = (x + adj[0], y + adj[1])
            if 0 <= new[0] <= 4 and 0 <= new[1] <= 4:
                con.append(grid[new[1]][new[0]])
        connections[grid[y][x]] = con

bfs = [('', dim, on)]
searched_out = set()
while True:
    item = bfs.pop(0)
    possibles = ''
    for letter in item[1] + item[2]:
        for connection in connections[letter]:
            if item[0].count(connection) < 2:
                if connection not in possibles:
                    possibles += connection
                    dim_c = item[1]
                    on_c = item[2]
                    n = 0
                    for con in connections[connection]:
                        if con in on_c:
                            on_c = on_c.replace(con, '')
                            n += 1
                        elif con in dim_c:
                            on_c += con
                            dim_c = dim_c.replace(con, '')
                        else:
                            dim_c += con
                            n -= 1
                    commands = item[0] + connection
                    commands = ''.join(sorted(commands))
                    if dim_c == '' and on_c == '':
                        output = ''
                        for item in commands:
                            if item.upper() not in output:
                                if commands.count(item) == 2:
                                    output += item.upper()
                                else:
                                    output += item.lower()
                        print(output)
                        exit()

                    if n >= 0:
                        if commands not in searched_out:
                            bfs.append((item[0] + connection, dim_c, on_c))
                            searched_out.add(commands)
