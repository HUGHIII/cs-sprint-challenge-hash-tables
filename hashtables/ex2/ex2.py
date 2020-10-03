#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    route = [None] * length
    for tick in tickets:
        ht[tick.source] = tick.destination
        # l = list(ht.items())

    cur = ht['NONE']
    for i in range(length):
        route[i] = cur
        cur = ht[cur]




    return route


tickets = [
    Ticket("PIT","ORD"),
    Ticket("XNA","CID" ),
    Ticket("SFO","BHM" ),
    Ticket("FLG","XNA" ),
    Ticket("NONE","LAX" ),
    Ticket("LAX","SFO" ),
    Ticket("CID","SLC" ),
    Ticket("ORD","NONE" ),
    Ticket("SLC","PIT" ),
    Ticket("BHM","FLG" )
]

reconstruct_trip(tickets,len(tickets))