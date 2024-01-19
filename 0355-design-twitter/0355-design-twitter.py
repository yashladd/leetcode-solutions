class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.follwerMap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follwerMap[userId].add(userId)
        follwers = self.follwerMap[userId]
        heap = []
        for f in follwers:
            if len(self.tweetMap[f]):
                cnt, tweetId = self.tweetMap[f][-1]
                index = len(self.tweetMap[f]) - 1
                heap.append((cnt, tweetId, index, f))
        heapify(heap)
        res = []
        while heap and len(res) < 10:
            cnt, tweetId, index, follId = heappop(heap)
            res.append(tweetId)
            nexIdx = index - 1
            if nexIdx >= 0:
                cnt, tweetId = self.tweetMap[follId][nexIdx]
                heappush(heap, (cnt, tweetId, nexIdx, follId))
                
        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follwerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follwerMap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)