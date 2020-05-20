class StockSpanner:
    def __init__(self):
        self.stack = []
        self.spans = []
    def next(self, price: int) -> int:
        ind = len(self.stack) - 1
        while ind >= 0 and self.stack[ind] <= price:
            temp = self.spans[ind]
            ind = ind - temp
        self.stack.append(price)
        temp = len(self.stack) - 1 - ind
        self.spans.append(temp)
        return temp

