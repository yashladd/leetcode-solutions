
class BrowserHistory:
    def __init__(self, homepage: str):
        self.currIdx = 0
        self.history = [homepage]
        self.len = 1
        

    def visit(self, url: str) -> None:
        if self.currIdx + 2 > len(self.history):
            self.history.append(url)
        else:
            self.history[self.currIdx + 1] = url
        self.currIdx += 1
        self.len = self.currIdx + 1
        
    def back(self, steps: int) -> str:
        index = max(self.currIdx-steps, 0)
        self.currIdx = index
        return self.history[index]

    def forward(self, steps: int) -> str:
        index = min(self.currIdx+steps, self.len-1)
        self.currIdx = index
        return self.history[index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)