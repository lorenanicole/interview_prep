import operator

class GoGame:
    def __init__(self, size):
        self.player_one = "W"
        self.player_two = "B"
        self.board = {}
        self.size = size
        # Represent as 1D arr, as can access board by board[coord]
        self.board_spots = "-"  * (self.size * self.size) 
    
    def flatten(self, coord):
        # e.g. (0,1) -> 19 * 0 + 1 -> 1st 
        # e.g. (5,1) -> 19 * 5 + 1
        # size of row * row * number elem in the row
        return self.size * coord[0] + coord[1]

    def unflatten(self, flattened_coord):
        # e.g. (6,1) -> 19 * 5 + 1 -> 96
        # e.g. divmod(5, 1) -> 96 % 5 == 1, 19 * 5 = 95
        return divmod(flattened_coord, self.size)
    
    def is_on_board(self, coord):
        # calculate the row
        # calculate the col
        # e.g. (5,1)
        return coord[0] % self.size == coord[0] and coord[1] % self.size == coord[1]
    
    def get_valid_neighbors(self, fc):
        # f_coord = self.flatten(coord)
        # x, y = coord[0], coord[1]

        x, y = self.unflatten(fc)

        # neighbors = []
        # if not (x < (self.size * self.size) and y < (self.size * self.size)):
        #     return neighbors
    
        # neighbor_computation = {
        #     "LEFT": (1, operator.sub),
        #     "RIGHT": (1, operator.add),
        #     "TOP": (0, operator.sub),
        #     "BOTTOM": (0, operator.add)
        # }
        # neighbors_to_compute = ['LEFT', 'RIGHT', 'TOP', 'BOTTOM']
        # # is it on left or right edge?
        # if y == 0:
        #     neighbors_to_compute.pop(neighbors_to_compute.index('LEFT'))
        # elif y == (self.size - 1):
        #     neighbors_to_compute.pop(neighbors_to_compute.index('RIGHT'))
        # # is it on top or bottom edge?
        # elif x == 0:
        #     neighbors_to_compute.pop(neighbors_to_compute.index('TOP'))
        # elif x == (self.size - 1):
        #     neighbors_to_compute.pop(neighbors_to_compute.index('BOTTOM'))


        # for neighbor in neighbors_to_compute:
        #     operation = neighbor_computation[neighbor]
        #     coord_to_mutuate, operator_to_apply = operation[0], operation[1]
        #     new_x, new_y = None, None

        #     if coord_to_mutuate == 0: 
        #         new_x = operator_to_apply(x,1)
        #         neighbors.append((new_x, y))
                    
        #     else:
        #         new_y = operator_to_apply(y,1)
        #         neighbors.append((x, new_y))
        
        # print(neighbors)

        neighbors = [(x+1, y), (x, y-1), (x, y+1), (x-1, y)]
        neighbors = list(filter(lambda c: self.is_on_board(c), neighbors))
        neighbors = list(map(lambda c: self.flatten(c), neighbors))
        return sorted(neighbors)
    
    def find_reached(self, fc):
        color = self.board[fc]
        frontier = [fc]
        chain = set([fc])
        reached = set()

        neighbors = self.get_valid_neighbors(fc)
        while frontier:
            current_fc = frontier.pop()
            chain.add(current_fc)
            for f_neighbor in neighbors:
                flattened = self.flatten(f_neighbor)
                if self.board[flattened] == color and flattened not in chain:
                    chain.append(flattened)
                elif self.board[flattened] != color:
                    reached.add(flattened)
        
        return chain, reached

    def place_stone(self, color, fc):
        # Representing as a str
        self.board = self.board[:fc] + color + self.board[fc+1:]
    


# go_game = GoGame(5)
# go_game.get_valid_neighbors((1,1))
# go_game.get_valid_neighbors((0,1))  # [(1,1), (0,2), [0,1]]
"""
extend type Query
    - me: User

type Mutation
    - setBoard: boardID, id body str -> Board

type User
    - id
    - account - Account
    - boards - List of Boards

type User @key(fields: id)
    - id: ID! <-- cannot be null
    - account: Account

type Account @key(fields: id)
    - id: ID

type Board
    - id
    - body (str)

enum BoardMutationErrors
    - DEADLOCK
    - STALE_BOARD
    - UNKNOWN
    - INVALID_STATE
    - INVALID_PERMISSION

federated schema
Federation is our flagship concept/product
"""


# from graphene_federation import ObjectType, Field, List, Int, String, build_schema, key, external, LATEST_VERSION 

# class Query(ObjectType):
#     me = Field(User, id=Int(required=True))

#     def resolve_me(self, id, **kwargs):
#         return User(id)

# class User(ObjectType):
#     id = Int(required=True, external=True)
#     boards = List(Board)
#     account = Field(Account)

#     def resolve_boards(self, board_ids):
#         return Board.where(ids=board_ids)

#     def resolve_account(self, id):
#         return Account(id=id)

# class Account(ObjectType):
#     id = Int(external=True)

#     @key
#     def key(self):
#         return self.id

# class Board(ObjectType):
#     id = Int()
#     board = String()

#     def resolve_board(self):
#         return self.board

# schema = build_schema(query=Query, federation_version=LATEST_VERSION, types=[User, Account, Board, Mutation])

class GoGame():
    def __init__(self, size):
        self.p1 = 'black'
        self.p2 = 'white'
        self.size = size
        self.board = self.size * self.size * "-"
    
    def flatten(self, coord):
        # (4,1) -> 21
        x, y = coord[0], coord[1]
        x_val = self.size * x
        return x_val + y
    
    def unflatten(self, fc):
        return divmod(fc, self.size)
    
    def is_in_board(self, coord, is_flat):
        try:
            if not is_flat:
                flattened = self.flatten(coord)
            return 0 <= flattened <= len(self.board)
        except IndexError:
            return False
    
    def get_valid_neighbors(self, coord, is_flat):
        if not is_flat:
            x, y = self.unflatten(coord)
        else:
            x,y = coord[0], coord[1]

        neighbors = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1)
        ]

        neighbors_to_keep = []
        for neighbor in neighbors:
            if self.is_in_board(neighbor, is_flat=False):
                neighbors_to_keep.append(neighbor)
        
        return sorted(neighbors_to_keep)

    def reach(self, coord):
        

go_game = GoGame(5)
print(go_game.get_valid_neighbors((1,1), is_flat=True))
print(go_game.get_valid_neighbors((0,1), is_flat=True))  # [(1,1), (0,2), (0,0)]

