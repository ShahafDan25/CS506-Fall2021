def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x, y))

def jaccard_dist(x, y):
    if len(x) == 0:
        final = 1
    else:
        total = 0
        for i in range(len(x)):
            if x[i] == y[i]:
                total += 1
        final = total / len(x)
    return 1 - final
# ------------------ ATTEMPT #01 --------------------------------
#     if (x == [] or y == []):
#         return 1.0
#     c = list(set(x).intersection(set(y)))
#     return 1.0 - (float(len(c)) / float(len(x) + len(y) - len(c)))
# ------------------ ATTEMPT #02 --------------------------------
#     intersection = len(list(set(x).intersection(y)))
#     try:
#         union = (len(x) + len(y)) - intersection
#         return 1 - (float(intersection) / union) #try and error for division by zero
#     except:
#         print (" THERE IS AN ERROR IN JACCARD DISTANCE " + str(1 - (float(intersection) / union)))
#         return 0.0
    
def dot(x,y): # NEEDED FOR COSINE_SIM FUNCTION
    return (sum(a*b for a,b in zip(x, y)))

def cosine_sim(x, y):
    try:
        return float(dot(x,y)) / ((dot(x,x) **.5) * (dot(y,y) ** .5))
    except: 
        print (" THERE IS AN ERROR IN JACCARD DISTANCE ")
        return 0.0
    

# Feel free to add more
