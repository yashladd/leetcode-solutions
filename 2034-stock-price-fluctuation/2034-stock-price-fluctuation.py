class StockPrice:

    def __init__(self):        
        self.price_map = {}
        self.max_prices = []
        self.min_prices = []
        self.current_ts = 0

    def update(self, timestamp: int, price: int) -> None:
        self.current_ts = max(self.current_ts, timestamp)
        self.price_map[timestamp] = price
        heappush(self.max_prices, (-price, timestamp))        
        heappush(self.min_prices, (price, timestamp))        


    def current(self) -> int:
        return self.price_map[self.current_ts]
        

    def maximum(self) -> int:
        while self.max_prices and -self.max_prices[0][0] != self.price_map[self.max_prices[0][1]]:
            heappop(self.max_prices)

        return self.max_prices and -self.max_prices[0][0]

    def minimum(self) -> int:
        while self.min_prices and self.min_prices[0][0] != self.price_map[self.min_prices[0][1]]:
            heappop(self.min_prices)

        return self.min_prices and self.min_prices[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()