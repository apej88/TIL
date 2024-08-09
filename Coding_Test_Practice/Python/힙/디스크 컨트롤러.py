import heapq
def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    total_time = 0
    current_time = 0
    completed_jobs = 0
    start_index = 0
    n = len(jobs)
    waiting_queue = []
    while completed_jobs < n:
        while start_index < n and jobs[start_index][0] <= current_time:
            heapq.heappush(waiting_queue, (jobs[start_index][1], jobs[start_index][0]))
            start_index += 1
        if waiting_queue:
            job_duration, job_request_time = heapq.heappop(waiting_queue)
            current_time += job_duration
            total_time += current_time - job_request_time
            completed_jobs += 1
        else:
            if start_index < n:
                current_time = jobs[start_index][0]
    return total_time // n