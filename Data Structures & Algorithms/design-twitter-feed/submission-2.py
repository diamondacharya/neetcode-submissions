import collections
class Twitter:
    def __init__(self):
        self.followMap = collections.defaultdict(set) # maps userId --> set of followeeIds
        self.tweetMap = collections.defaultdict(list) # maps userId --> list of their (count, tweet) tuple
        self.time = 0 # global counter for time

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        followees = self.followMap[userId]
        followees.add(userId)
        for followeeId in followees: 
            tweets = self.tweetMap[followeeId]
            lastIndex = len(tweets) - 1
            if lastIndex >= 0: 
                time, tweetId = tweets[lastIndex]
                heapq.heappush(maxHeap, [-1 * time, tweetId, followeeId, lastIndex - 1])
        while maxHeap and len(res) < 10: 
            time, tweetId, followeeId, index = heapq.heappop(maxHeap) # can use the followeeId and index that were pushed before
            res.append(tweetId)
            tweets = self.tweetMap[followeeId]
            if index >= 0: 
                time, tweetId = tweets[index]
                heapq.heappush(maxHeap, [-1 * time, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: 
            self.followMap[followerId].remove(followeeId)
        
