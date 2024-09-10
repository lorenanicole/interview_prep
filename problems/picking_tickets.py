"""
Consider an array of n ticket prices, tickets. A number, m, is defined as the size of some subsequence of tickets, s, where each element
covers an unbroken range of integers. That is, if the elements in s are sorted, the absolute difference between any elements j and j + 1 is
either 0 or 1. Determine the maximum length of a subsequence chosen from the tickets array.
"""
from collections import Counter
# def pick_tickets(ticket_prices):
#     ticket_prices.sort()
#     start = min(ticket_prices)
#     end = max(ticket_prices)
#     max_length = []
    
#     # 1, 3, 3, 4, 5, 6
#     for n in range(start, end + 1):
#         counter = 0
#         for num in ticket_prices:
#             if n == num or num == n + 1:
#                 counter += 1
#         max_length.append(counter)
#     return(max(max_length))

    # ticket_prices = Counter(ticket_prices)
    # max_price = 0
    # for counter in range(100):
    #     max_price = max(max_price, ticket_prices[counter]+ticket_prices[counter+1])
    # print(max_price)

# def pick_tickets(tickets: list) -> int:
#     tickets = sorted(tickets)
#     tickets = Counter(tickets)
#     max_length = 0

#     for i in range(100):
#         print(i, i+1)
#         max_length = max(max_length, tickets[i] + tickets[i+1])
#         print(max_length, tickets[i], tickets[i+1])
#         print("----")
#     return max_length





# def pick_tickets(tickets):
#     frequency = [0] * 8
#     max_value = 0
#     for number in tickets:
#         # use the val of the elem as the index
#         frequency[number] += 1
#     print(frequency)
#     for i in range(1, 8):
        # Looking at the frequency arr to determine if an element within the arr next to it is
        # within 0 or 1
        # import pdb; pdb.set_trace()
        # Here we look at the val of the current item + the previous item and compare to the
        # max_value remember between any 2 vals should be a diff of 0 or 1 for it to count
        # max_value = max(max_value, frequency[i] + frequency[i - 1])
        # print(f"max - {max_value}, freq i - {frequency[i]}, freq i - 1 - {frequency[i - 1]}, i - {i}")
        # import pdb; pdb.set_trace()
        # print(f"{tickets[i]}")
        # max value keeps a pointer of the max chain! so if e.g. have 3 items in max chain and then 
        # more values come in like a 1, then we'll keep the max_value
    # return max_value


def pick_tickets(tickets):
    tickets = sorted(tickets)
    tickets_freq = [0] * 100
    max_chain = 0

    for indx, ticket in enumerate(tickets):
        tickets_freq[ticket] += 1
    
    for i in range(100 - 1):
        max_chain = max(max_chain, tickets_freq[i] + tickets_freq[i + 1])
    
    return max_chain


# def pick_tickets(tickets):
#     tickets = sorted(tickets)
#     max_chain = 1
#     max_chains = []
#     vals_in_chain = []

#     for indx in range(1, len(tickets) - 1):

#         if indx < 1:
#             continue
#         # print(indx)
#         #     print("haiiii")
#         # elif ticket == 4:
#         #     print("BOOOO")
#         if abs(tickets[indx] - tickets[indx - 1]) in [0,1]:
#             # import pdb; pdb.set_trace()
#             # print(f"Here is ticket {tickets[indx]}, {tickets[indx -1]}, {tickets[indx+1]} and {max_chain}")
#             max_chain += 1
#             vals_in_chain.append(tickets[indx])
#         else:
#             # import pdb; pdb.set_trace()
#             # print(f"Here is tickeeeeet {tickets[indx]}, {tickets[indx -1]}, {tickets[indx+1]} and {max_chain}")
#             max_chains.append(max_chain)
#             max_chain = 0
#             vals_in_chain = []
#     # # import pdb; pdb.set_trace()

#     if abs(tickets[len(tickets) - 1] - tickets[len(tickets) - 2]) in [0,1]: 
#         vals_in_chain.append(tickets[len(tickets) - 1])
#         max_chain += 1
#         # print(f"Here is tiiiiiiicket {tickets[len(tickets) - 1]} and {max_chain}")

#     # import pdb; pdb.set_trace()
#     return max_chain


from collections import defaultdict

# def pick_tickets(a):
#     d = defaultdict(int)
#     r_val = 0
#     a = sorted(a)
#     for val in a:
#         d[val] += 1
#         # import pdb; pdb.set_trace()
#         # print(r_val, d[val] + d[val+1], d[val]+ d[val-1])
#         r_val = max(r_val, d[val]+d[val+1], d[val]+d[val-1])

#     return r_val


print(pick_tickets([1, 1, 2, 2, 4, 4, 5, 5, 6]))# == 5))
print(pick_tickets([4, 6, 5, 3, 3, 1])) #  == 3)  
print(pick_tickets([1, 1, 1, 4, 5, 6])) #== 3)        
print(pick_tickets([1, 2, 2, 3, 1, 2])) #== 5) #=