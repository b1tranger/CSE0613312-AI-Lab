import heapq 

li = [10, 5, 3, 6, 2, 1]

heapq.heapify(li)
print(li)

heapq.heappush(li, 100)

print(li)

# [1, 2, 3, 6, 5, 10]
# [1, 2, 3, 6, 5, 10, 100]