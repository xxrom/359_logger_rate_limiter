class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logInterval = 10
        self.queue = [{}]
        self.allMessagesNextPrint = {}
        self.currentTime = 0

    def addToLastQueue(self, message: str):
        if message not in self.queue[0]:
            self.queue[0][message] = 1
        else:
            self.queue[0][message] += 1

    def addToAllMessages(self, message: str, timestamp: int):
        if (message not in self.allMessagesNextPrint
            or timestamp >= self.allMessagesNextPrint[message]):
            self.allMessagesNextPrint[message] = timestamp + self.logInterval

    def increaseQueue(self, timestamp):
        diff = timestamp - self.currentTime
        self.currentTime = timestamp

        if diff < self.logInterval:
            for i in range(diff):
                self.queue.insert(0,{})

            numberForDeletingItems = len(self.queue) - self.logInterval
            if numberForDeletingItems > 0:
                for i in range(numberForDeletingItems):
                    self.queue.pop()
        else:
            self.queue = [{}]
            self.allMessagesNextPrint = {}

    def missedMessageInAllMessages(self, message: str, timestamp: int):
        if message in self.allMessagesNextPrint:
            if timestamp < self.allMessagesNextPrint[message]:
                return False

        return True

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        isShouldBePrinted = False

        if timestamp != self.currentTime:
            self.increaseQueue(timestamp)

        if self.missedMessageInAllMessages(message, timestamp):
            isShouldBePrinted = True

        self.addToLastQueue(message)
        self.addToAllMessages(message, timestamp)

        return isShouldBePrinted



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

my = Logger()
timestamp0 = 0
message0 = '0 hello'
timestamp1 = 1
message1 = '1 tell a joke'
timestamp2 = 10
message2 = '0 hello'


# print(my.shouldPrintMessage(timestamp0, message0))
# print(my.shouldPrintMessage(timestamp0, message0))
# print(my.shouldPrintMessage(timestamp1, message1))
# print(my.shouldPrintMessage(timestamp1, message1))
# print(my.shouldPrintMessage(timestamp1, message1))
# print(my.shouldPrintMessage(timestamp2, message2))
# print(my.shouldPrintMessage(timestamp2, message2))
# print(my.shouldPrintMessage(timestamp2, message2))
# print(my.shouldPrintMessage(timestamp2, message2))

# -----------------------------
# # logging string "foo" at timestamp 1
# print(my.shouldPrintMessage(1, "foo"))

# # logging string "bar" at timestamp 2
# print(my.shouldPrintMessage(2,"bar")
# )
# # logging string "foo" at timestamp 3
# print(my.shouldPrintMessage(3,"foo"))

# # logging string "bar" at timestamp 8
# print(my.shouldPrintMessage(8,"bar"))

# # logging string "foo" at timestamp 10
# print(my.shouldPrintMessage(10,"foo"))

# # logging string "foo" at timestamp 11
# print(my.shouldPrintMessage(11,"foo"))

# ----------------
# # logging string "foo" at timestamp 1
# print(my.shouldPrintMessage(100, "bug"))

# # logging string "bar" at timestamp 2
# print(my.shouldPrintMessage(10002000,"the longest message ever!"))

#----------------
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
# true,true,true,false,false,false,true,true,true,false

# Runtime: 224 ms, faster than 24.23% of Python3 online submissions for Logger Rate Limiter.
# Memory Usage: 19.8 MB, less than 20.26% of Python3 online submissions for Logger Rate Limiter.