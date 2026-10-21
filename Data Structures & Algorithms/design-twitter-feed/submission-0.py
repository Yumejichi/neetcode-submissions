from collections import defaultdict
from heapq import heappop, heappush
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) #user: tweets
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # check if there is follower:
        minheap = []

        for user in self.follows[userId] | {userId}:
            for time, tweet in self.tweets[user]:
                heappush(minheap, (time, tweet))
                if len(minheap) > 10:
                    heappop(minheap)
        return [tweet for time, tweet in sorted(minheap, reverse = True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
