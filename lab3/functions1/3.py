def solve(numheads, numlegs):
    r = (numlegs - 2 * numheads) / 2
    c = numheads - r

    if r.is_integer() and c.is_integer() and r >= 0 and c >= 0:
        return int(c), int(r)
    else:
        return "No solution"

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(f"Number of chickens: {result[0]}, Number of rabbits: {result[1]}")