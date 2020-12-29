import heapq

li = [5, 7, 9, 1, 3] 
  
# using heapify to convert list into heap 
heapq.heapify(li)
heapq.heappush(li, 3)
print(len(li)) 