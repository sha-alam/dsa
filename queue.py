class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
n = int(input("enter the number of elements for queue:"))
print("enter the elements:")
for i in range(n):
    q.push(int(input()))

print("Queue elements:")
q.display()
q.pop()
print("deque elements:")
q.display()
