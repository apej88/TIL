import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + min2*2
        heapq.heappush(scoville, new_scoville)
        answer += 1
    return -1 if scoville[0] < K else answer