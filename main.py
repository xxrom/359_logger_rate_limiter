class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

my = Logger()
timestamp0 = 0
message0 = 'hello'


ans = my.shouldPrintMessage(timestamp0, message0)
print("ans", ans)
