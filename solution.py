

def solve(value):
    return [(x-min(value))/(max(value)-min(value)) for x in value] if value and max(value) != min(value) else [0 for x in value]
