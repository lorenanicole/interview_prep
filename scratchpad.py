"""
An airplane has N rows and it has 10 seats numbered from A to K as A,B,C,D,E,F,G,H,J,K, such that ABC form one column, DEFG form second column and HJK form third column

A B C   D E F G   H J K
A B C   D E F G   H J K
A B C   D E F G   H J K


1A 1D 1K 1C 1D 1G 1H
2A 2D 2K 2C 2D 2G 2H

Given a string S and S represents the reserved seats. S is represented as 1A 1B etc. Seats allocated are represented in S as 1A 1E 1K separated by space.
Given the number of rows as N and S represents the seats reserved in the above mentioned format, find the max number of ways a family of 3 members can be allocated. Family members should be allocated consecutively. C and D are not consecutive seats, same for G and H. S can be empty also (no seats are reserved).

S="1A 2A 3A", N=3; the answer should be 9
S="1A 1D 1K 2C 2D 2G 2H", N = 2; the answer should be 1

"""

def airline_seats(seats, rows):
    seat_letters = ['A', 'D', 'K', 'C', 'C', 'G', 'H']
    plane_seats = [[0] * 7 for row in range(rows)]
    seats = [seat for seat in seats.split(" ")]
    print(seats)
    # row
    for indx, row_seats in enumerate(plane_seats):
    # col
        for col_indx, col in enumerate(1,row_seats+1):
            for seat in seat_letters:
                # index which spot is full
                seat_map = seat_letters.index(seat) - 1 
                
                
                
            



print(airline_seats("1A 2A 3A", 3) == 9)