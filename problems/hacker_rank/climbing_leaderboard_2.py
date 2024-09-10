from collections import Counter
import operator

def climbingLeaderboard(ranked, player):
    output = []
    ranked = Counter(ranked)
    ranks = list(sorted(ranked.items(), key=lambda x: x[0], reverse=True))
    for indx, rank in enumerate(ranks):
        ranks[indx] = f'{rank[0]}_{indx+1}'

    for indx, _ in enumerate(player):
        counter = 0
        rank = ranks[counter].split('_')
        score = int(rank[0])
        ranking = int(rank[1])

        while player[indx] < score and counter < len(ranks) - 1:
            counter += 1
            rank = ranks[counter].split('_')
            score = int(rank[0])
            ranking = int(rank[1])

        if score != player[indx] and score > player[indx]:
            ranking += 1

        output.append(ranking)

    return output


print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]) == [4, 3, 1])