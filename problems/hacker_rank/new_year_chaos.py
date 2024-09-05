import math

# def minimumBribes(queue):
#     # Write your code here
#     bribes = {}

#     # 
#     for person in range(int(math.ceil(len(queue) / 2)), 0, -1):
#         start_indx = (person * 2) - 2
#         end_indx = (person * 2) - 3
#         # import pdb; pdb.set_trace()
#         print(f"starting index {start_indx}, ending index {end_indx}")
#         if not bribes.get(person) and bribes.get(person, -1) < 2:
#             # import pdb; pdb.set_trace()
#             bribes[person] = 1
#             # import pdb; pdb.set_trace()
            

#             temp, temp2 = queue[start_indx], queue[end_indx]
#             queue[end_indx] = temp
#             queue[start_indx]= temp2 
#             print("HAIII")
#             # import pdb; pdb.set_trace()
#         elif bribes.get(person) and not bribes[person] > 2:
#             bribes[person] += 1
#             # import pdb; pdb.set_trace()
#             temp, temp2 = queue[start_indx], queue[end_indx]
#             queue[end_indx] = temp
#             queue[start_indx]= temp2 

#         print(queue)       
        
# def minimumBribes(queue):
#     bribes = 0
#     for indx, p in enumerate(queue[::-1]):
#         if p > 2:
#             resp = 'too chaotic'
#             # return "Too chaotic"
#         for j in range(max(p-1,0),indx):
#             print(max(p-1, 0))
#             if queue[j] > p:
#                 bribes += 1
#     print(queue, resp, bribes)


def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - (i + 1) > 2:
            return 'Too chaotic'
        # import pdb; pdb.set_trace()
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    return bribes
# [1,3,2,5,4]
# print(minimumBribes([2, 1, 5, 3, 4]))
print(minimumBribes([2, 5, 1, 3, 4]))# == 3)