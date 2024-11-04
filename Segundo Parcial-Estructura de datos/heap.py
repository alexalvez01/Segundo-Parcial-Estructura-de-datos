class HeapMin:
    def __init__(self):
        self.elements = []

    def arrive(self, data, priority):
        self.elements.append((priority, data))
        self.elements.sort()  
    def atention(self):
        return self.elements.pop(0) if self.elements else None