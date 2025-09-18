class RecentCounter:
    def __init__(self):
        from collections import deque
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

recentCounter = RecentCounter()

while True:
    print("Введите значение t или выход для выхода:")
    input_str = input()
    if input_str == 'выход':
        break
    
    t = int(input_str)
    result = recentCounter.ping(t)
    print(f"Количество запросов за последние 3000 мс: {result}")
    print()