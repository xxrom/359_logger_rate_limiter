class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxQueue = 10
        self.queue = [{}]
        self.allMessages = {}
        self.currentTime = 0

    def addToLastQueue(self, message: str):
        if message not in self.queue[0]:
            self.queue[0][message] = 1
        else:
            self.queue[0][message] += 1

    def addToAllMessages(self, message: str):
        if message not in self.allMessages:
            self.allMessages[message] = 1
        else:
            self.allMessages[message] += 1

    def removeMessagesFromAllMessage(self, messageDict: dict):
        for key in messageDict:
            # print('remove >> %s' % key)
            self.allMessages[key] -= messageDict[key]

            if self.allMessages[key] <= 0:
                del self.allMessages[key]


    def increaseQueue(self, timestamp):
        diff = timestamp - self.currentTime
        self.currentTime = timestamp

        for i in range(diff):
            self.queue.insert(0,{})

        numberForDeletingItems = len(self.queue) - self.maxQueue
        if numberForDeletingItems > 0:
            for i in range(numberForDeletingItems):
                # print(' >>> Pop =)')
                removeMessages = self.queue.pop()
                self.removeMessagesFromAllMessage(removeMessages)

    def missedMessageInAllMessages(self, message: str):
        if message in self.allMessages:
            return False

        return True

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        isShouldBePrinted = False

        if timestamp == self.currentTime:
            if self.missedMessageInAllMessages(message):
                isShouldBePrinted = True

            self.addToLastQueue(message)
            self.addToAllMessages(message)

        else:
            self.increaseQueue(timestamp)
            print('===========')
            print(self.queue)
            print(self.allMessages)

            if self.missedMessageInAllMessages(message):
                isShouldBePrinted = True

            self.addToLastQueue(message)
            self.addToAllMessages(message)

        print('----------')
        print(self.queue)
        print(self.allMessages)

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

# logging string "foo" at timestamp 1
print(my.shouldPrintMessage(1, "foo"))

# logging string "bar" at timestamp 2
print(my.shouldPrintMessage(2,"bar")
)
# logging string "foo" at timestamp 3
print(my.shouldPrintMessage(3,"foo"))

# logging string "bar" at timestamp 8
print(my.shouldPrintMessage(8,"bar"))

# logging string "foo" at timestamp 10
print(my.shouldPrintMessage(10,"foo"))

# logging string "foo" at timestamp 11
print(my.shouldPrintMessage(11,"foo"))
