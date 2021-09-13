class RecentCounter(object):

    def __init__(self):
        self.counter = []
        self.start = 0
        self.end = 0
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.counter.append(t)
        self.end+=1
        start_range = t - 3000
        while self.counter[self.start] < start_range:
            self.start+=1
        return self.end-self.start
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)