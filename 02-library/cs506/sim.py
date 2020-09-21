import math
import decimal


def euclidean_dist(x, y):
    return (p_root(sum(pow(abs(a - b), 2)for a, b in zip(x, y)), 2))

def manhattan_dist(x, y):
    return (p_root(sum(pow(abs(a - b), 1)for a, b in zip(x, y)), 1))

def jaccard_dist(x, y):
    if not x and not y:
        return 1
    return 1 - jaccard_sim(x,y)

def cosine_sim(x, y):
    if (len(x) != len(y)):
        return 'vectors not same size'
    
    dotProd = dot(x, y)
    normX = mag(x)
    normY = mag(y)

    if (normX * normY) != 0:
        return dotProd / (normX * normY)
    else:
        return float('inf')
    
# Feel free to add more
#Root value function for Minkowski distance
def p_root(val, r):
    root = 1 / float(r)
    return round(decimal.Decimal(val) ** decimal.Decimal(root), 3)

#Jaccard Similarity function
def jaccard_sim(x, y):
    s1 = set(x)
    s2 = set(y)
    return len(s1.intersection(s2)) / len(s1.union(s2))

#magnitude func in place of np.linalg.norm
def mag(x):
    res = 0

    for i in x:
        res += i **2
    
    return math.sqrt(res)

#dot product function
def dot(x, y):
    return sum([i*j for (i, j) in zip(x, y)])