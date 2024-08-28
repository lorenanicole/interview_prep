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

def pick_tickets(tickets: list) -> int:
    tickets = sorted(tickets)
    tickets = Counter(tickets)
    max_length = 0

    for i in range(100):
        # print(i, i+1)
        max_length = max(max_length, tickets[i] + tickets[i+1])
        # print(max_length, tickets[i], tickets[i+1])
        # print("----")
    return max_length

print(pick_tickets([1, 1, 2, 2, 4, 4, 5, 5, 5] == 5))
print(pick_tickets([4, 6, 5, 3, 3, 1])) #  == 3)  
# print(pick_tickets([1, 1, 1, 4, 5, 6]) == 3)        
# print(pick_tickets([1, 2, 2, 3, 1, 2]) == 5)
