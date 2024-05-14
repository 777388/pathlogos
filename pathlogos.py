import os
g = []
with open("aaa.txt", "r") as f:
    for line in f:
        g.append(line.rstrip())
i = lambda i: os.popen("wsl dig +trace +noidnin +noidnout "+i)
list(map(i, g))