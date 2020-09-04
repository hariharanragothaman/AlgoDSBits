low = 5
high = 15
q = 2


def find_count(low, high, q):
    count = 0
    while low <= high:
        prod = low * q
        lp = [c for c in str(prod)]
        ll = [c for c in str(low)]
        nn = [c for c in ll if c not in lp]
        if prod != low and len(nn) == len(ll):
            count += 1
        low += 1
    return count

result = find_count(low, high, q)
print(result)