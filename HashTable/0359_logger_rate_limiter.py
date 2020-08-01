"""
Leetcode Problem #359
"""

class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        # Message is not in hashmap
        if message not in self.hashmap:
            self.hashmap[message] = timestamp
            return True

        # Message is in hashmap
        else:
            diff = timestamp - self.hashmap[message]
            if diff >= 10:
                self.hashmap[message] = timestamp
                return True
            else:
                return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)