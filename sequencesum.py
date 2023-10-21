nums = [4681,6466,9411,-5130,6047]
k=2
import heapq   
heap = [(-nums[0], 0)]
ans = nums[0]

for i in range(1, len(nums)):
    while i - heap[0][1] > k:
        heapq.heappop(heap)

    curr = max(0, -heap[0][0]) + nums[i]
    ans = max(ans, curr)
    heapq.heappush(heap, (-curr, i))
    
print(ans)