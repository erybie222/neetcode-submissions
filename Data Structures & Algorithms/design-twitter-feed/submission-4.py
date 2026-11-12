class Twitter:

    def __init__(self):
        self.posts = []
        self.users = defaultdict(set)
        self.curId = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, [-self.curId, tweetId, userId])
        self.curId += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followed = self.users[userId]
        feed = self.posts.copy()
        res = []
        n = 10
        while n > 0 and feed:
            curId, tweetId, postUserId = heapq.heappop(feed)
            if postUserId in followed or postUserId == userId:
                res.append(tweetId)
                n -= 1
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
