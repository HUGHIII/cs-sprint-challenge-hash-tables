def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE

    store each weight from list [weights] as key in hash table
    make indices of each weight the value in ht
    iterate through list if limit - weight = key 
    
    return indices
    """
    cache = {}
    res = []
    # Your code here
    for i in range(len(weights)):
        cache[weights[i]] = i
        # tpl = list(cache.items())
    
    for i in range(len(weights)):
        if limit - weights[i] in cache:
            lMinusW = limit - weights[i]
            res.append(cache[lMinusW])
            res.append(i)
            return res
        
    return None


wts = [4, 6, 10, 15, 16]
length = len(wts)
lmt = 25

print(get_indices_of_item_weights(wts,length,lmt))
