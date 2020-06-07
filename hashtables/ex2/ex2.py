#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# tickets is an array of string variable names
# length is the number of tickets
def reconstruct_trip(tickets, length):

    dict = {}
    route = []

    # for each ticket in the tickets array
    for ticket in tickets:
        # store the source as the key and the destination 
        # as the value in the dict
        dict[ticket.source] = ticket.destination
    # the first source is "NONE", so the pointer begins
    # at the key whose value is "NONE"
    pointer = dict["NONE"]
    # this needs to run until all tickets have been arranged:
    # length = number of tickets
    while len(route) < length:
        # append the pointer to the array
        route.append(pointer)
        # change the pointer to the value of the key:value pair,
        # which is the destination of the ticket instead of the source
        pointer = dict[pointer]
    return route
    

