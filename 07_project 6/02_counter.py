class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
print(f"Number of objects created: {Counter.get_count()}")