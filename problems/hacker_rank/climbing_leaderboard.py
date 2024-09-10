from collections import Counter

# Below is pass 1, let's increase the performance
# def climbingLeaderboard(ranked, player):
#     ranked = Counter(ranked)
#     currentRankings = {}
#     playerRankings = []
#     numRank = 1

#     # Using the counter, generate rankings from 1 to the lowest in a dict 
#     for playerScore in ranked:
#         currentRankings[playerScore] = {'rank': numRank}   
#         numRank += 1
    
#     # Start at the lowest rank for the new player data to ensure can increase rank
#     # if score(s) are equal to or greater than other players
#     currentRank = max(list(map(lambda k: k[1]['rank'], currentRankings.items()))) + 1
#     for playerScore in player:
#         for rankedScores in ranked:
#             if playerScore >= rankedScores:
#                 currentRank = min([rank['rank'] if score == rankedScores else currentRank for score, rank in currentRankings.items()])
#         playerRankings.append(currentRank)
#         # Reset to lowest rank, and find new rank on next loop
#         currentRank = max(currentRankings) + 1
    
#     return playerRankings

# v2 - this should be O(n)
# unclear if min is adding another O(n)
# def climbingLeaderboard(ranked, player):
#     ranked = Counter(ranked)
#     currentRankings = {}
#     playerRankings = []
#     numRank = 1

#     # Using the counter, generate rankings from 1 to the lowest in a dict 
#     for playerScore in ranked:
#         currentRankings[playerScore] = {'rank': numRank}   
#         numRank += 1

#     for playerScore in player:
#         closestScore = min(ranked, key=lambda x:abs(x-playerScore))
#         # import pdb; pdb.set_trace()
#         if playerScore >= closestScore:
#             # If larger than closest score than they take their rank
#             # If same score then they are the same rank
#             playerRankings.append(currentRankings[closestScore]['rank'])
#         else:
#             # If smaller than closest score than they are a rank behind
#             playerRankings.append(currentRankings[closestScore]['rank'] + 1)

#     return playerRankings

# V3 - Big O(N+M)
# def climbingLeaderboard(ranked, player):
#     # Remove duplicates
#     ranked = list(set(ranked))
#     ranked.sort(reverse=True)
#     # import pdb; pdb.set_trace()
#     i = 0
#     playerRankings = []

#     for score in player:
#         # While the other players score is less than the other players
#         # iterate, we don't need to reset i because the player scores are 
#         # guranteed to be in ascending order 
#         while i < len(ranked) and ranked[i] <= score:
#             i += 1
#         # import pdb; pdb.set_trace()
#         # We use the length of the ranked scores and decrement by the current
#         # indx as larger values in the ranked scores appear towards the tail
#         # end of the ranked list and larger scores have a higher - that is a lower
#         # number - rank, and we add 1 as we are using a zero based indx and need
#         # to adjust accordingly
#         import pdb; pdb.set_trace()
#         playerRankings.append(len(ranked) - i + 1)
#     import pdb; pdb.set_trace()
#     return playerRankings




# def climbingLeaderboard(ranked, player):
#     ranked = list(set(ranked))
#     ranked.sort(reverse=True)
#     output = []
#     counter = 0
#     for indx, score in enumerate(player):
#         # import pdb; pdb.set_trace()
#         while counter < len(ranked) and ranked[counter] <= score:
#             counter += 1
#         # Add 1 for 0 based indx
#         output.append(len(ranked) - counter + 1)
#         print(output)
#     return output


from collections import Counter

def climbingLeaderboard(ranked, player):
    output = []
    ranked = list(set(ranked))
    ranked.sort()
    counter = 0
    for p_game in player:
        while counter < len(ranked) and ranked[counter] <= p_game:
            counter += 1
        output.append(len(ranked) - counter + 1)
    return output


print(climbingLeaderboard(
    [100, 100, 50, 40, 40, 20, 10],
    [5, 25, 50, 120]
) == [6, 4, 2, 1])

print(climbingLeaderboard(
    [100, 90, 90, 80, 75, 60],
    [50, 65, 77, 90, 102]
) == [6, 5, 4, 2, 1])

