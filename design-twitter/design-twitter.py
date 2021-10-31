class Twitter:

    def __init__(self):
        self.newsfeeds = []
        self.users = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId].append(userId)
        self.newsfeeds.insert(0,[userId,tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        #print(self.newsfeeds,self.users[userId])
        for ids in self.newsfeeds:
            if ids[0] in self.users[userId]:
                news.append(ids[1])
            if len(news) == 10:
                return news
        return news
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId].append(followerId)
        self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)