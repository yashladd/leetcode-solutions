class Logger:

    def __init__(self):
        # self.currTime = 0
        self.nextAvailable = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.nextAvailable or self.nextAvailable[message] <= timestamp:
            self.nextAvailable[message] = timestamp + 10
            return True

        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)