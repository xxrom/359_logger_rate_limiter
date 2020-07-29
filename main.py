class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logInterval = 10
        self.currentTime = 0
        self.allMessagesNextPrint = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        isShouldBePrinted = False

        if timestamp != self.currentTime:
            isMessagesCouldBeCleaned = timestamp - self.currentTime > self.logInterval
            if isMessagesCouldBeCleaned:
                self.allMessagesNextPrint = {}

            self.currentTime = timestamp

        isCouldBePrinted = message not in self.allMessagesNextPrint or timestamp >= self.allMessagesNextPrint[message]
        if isCouldBePrinted:
            isShouldBePrinted = True

        isTimeShouldUpdate = message not in self.allMessagesNextPrint or timestamp >= self.allMessagesNextPrint[message];
        if isTimeShouldUpdate:
            self.allMessagesNextPrint[message] = timestamp + self.logInterval

        return isShouldBePrinted

my = Logger()

print(my.shouldPrintMessage(0,"A"))
print(my.shouldPrintMessage(0,"B"))
print(my.shouldPrintMessage(0,"C"))
print(my.shouldPrintMessage(0,"A"))
print(my.shouldPrintMessage(0,"B"))
print(my.shouldPrintMessage(0,"C"))
print(my.shouldPrintMessage(11,"A"))
print(my.shouldPrintMessage(11,"B"))
print(my.shouldPrintMessage(11,"C"))
print(my.shouldPrintMessage(11,"A"))
print(my.shouldPrintMessage(12,"A"))
# true,true,true,false,false,false,true,true,true,false,false

# Runtime: 156 ms, faster than 72.85% of Python3 online submissions for Logger Rate Limiter.
# Memory Usage: 19.7 MB, less than 73.20% of Python3 online submissions for Logger Rate Limiter.