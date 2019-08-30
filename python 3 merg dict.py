nummer = 10
hai1 = {}
hai2 = {2:3,4:5}
hai3 = {3:4,5:6}

for key in range(nummer):
    hai1[key] = key^2

nieuw = {**hai1, **hai2, **hai3}

print(nieuw)
