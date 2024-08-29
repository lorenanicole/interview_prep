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
def climbingLeaderboard(ranked, player):
    ranked = Counter(ranked)
    currentRankings = {}
    playerRankings = []
    numRank = 1

    # Using the counter, generate rankings from 1 to the lowest in a dict 
    for playerScore in ranked:
        currentRankings[playerScore] = {'rank': numRank}   
        numRank += 1

    for playerScore in player:
        closestScore = min(ranked, key=lambda x:abs(x-playerScore))
        # import pdb; pdb.set_trace()
        if playerScore >= closestScore:
            # If larger than closest score than they take their rank
            # If same score then they are the same rank
            playerRankings.append(currentRankings[closestScore]['rank'])
        else:
            # If smaller than closest score than they are a rank behind
            playerRankings.append(currentRankings[closestScore]['rank'] + 1)

    return playerRankings

print(climbingLeaderboard(
    [100, 100, 50, 40, 40, 20, 10],
    [5, 25, 50, 120]
) == [6, 4, 2, 1])

print(climbingLeaderboard(
    [100, 90, 90, 80, 75, 60],
    [50, 65, 77, 90, 102]
) == [6, 5, 4, 2, 1])

