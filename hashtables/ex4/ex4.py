def has_negatives(a):
    """
    YOUR CODE HERE

    pseudo -
    # may have to use items() method like in lecture to make tuple
    # can determine if pos int has a corresponding neg int by doubling the pos int and subtracting that value from itself


    """
    # Your code here
    # cache = {}
    # a.sort(reverse=True)
    # negs = []
    # result = []
    # for x in a:
        
    #     if x > 0 and x not in cache:
    #         cache[x] = 0
    #         detNeg = x - x * 2
    #         cache[x] = detNeg
    #         l = list(cache.items())
    #     elif x < 0:
            
    #         negs.append(x)
    # for x in l:
    #     if x[1] in negs:
            
    #         result.append(x[0])



    cache = {}
    result = []

    for e in a:
        if e not in cache and e < 0:
            negToPos = e * -1
            cache[e] = negToPos
    for key in cache:
        if cache[key] in a:
            result.append(cache[key])



    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
