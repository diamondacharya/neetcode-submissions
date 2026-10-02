class Twitter:

    def __init__(self):
        self.followeeMap = collections.defaultdict(set) # map of userId to all followeees (including the user themselves)
        self.tweetMap = collections.defaultdict(list) # map of userId to tweetIds 
        self.timer = 0 # global timer 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followeeMap[userId]
        followees.add(userId) # we should consider the user's posts too
        heap = []
        res = []
        for person in followees: 
            tweets = self.tweetMap[person]
            if len(tweets) > 0: 
                heap.append((-1 * tweets[-1][0], tweets[-1][1], len(tweets) - 1, person)) # also append the last accessed index and the person in the heap
        heapq.heapify(heap)
        while heap and len(res) < 10: 
            tweetTime, tweet, lastIndex, followee = heapq.heappop(heap)
            res.append(tweet)
            tweets = self.tweetMap[followee]
            if lastIndex - 1 >= 0: 
                tweetForHeap = tweets[lastIndex - 1]
                heapq.heappush(heap, (-1 * tweetForHeap[0], tweetForHeap[1], lastIndex - 1, followee))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.followeeMap[followerId]
        if followeeId in followees: 
            followees.remove(followeeId)
        