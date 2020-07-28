0 - foo

0-4 - object with messages (t0 - t1) = diff - diff seconds ()
prevQueue = [{},{},{},{}] - (size of array - interval between current time and previous messages)
  prevQueue = [{
    foo: 1
  }]

global object with all messages:
  allMessages = {
      foo: 1
    }

2 - ttt
  prevQueue = [{
      ttt: 1
    },
    {},
    {
      foo: 1
    }]
  allMessages = {
      foo: 1,
      ttt: 1
    }

3 - bbb
  prevQueue = [
    {
      bbb: 1
    },
    {
      ttt: 1
    },
    {},
    {
      foo: 1
    }]
  allMessages = {
      foo: 1,
      ttt: 1,
      bbb: 1
    }

3 - foo
  prevQueue = [
    {
      bbb: 1,
      foo: 1
    },
    {
      ttt: 1
    },
    {},
    {
      foo: 1
    }]
  allMessages = {
      foo: 2,
      ttt: 1,
      bbb: 1
    }

5 - ttt
  prevQueue = [
    {
      ttt: 1
    }
    {},
    {
      bbb: 1,
      foo: 1
    },
    {
      ttt: 1
    },
    {},
    // { foo: 1 }
    ]
  allMessages = {
      foo: 1, // 2 - 1 = 1 , because of deleting object from array
      ttt: 2,
      bbb: 1
    }

8 - bbb
    prevQueue = [
    {
      bbb: 1
    }
    {},
    {},
    {
      ttt: 1
    }
    {},
    // {
    //  bbb: 1,
    //  foo: 1
    // },
    // { ttt: 1 },
    // {},
    // { foo: 1 }
    ]

  // After deleting all unnecessary objects from "prevQueue"
  allMessages = {
      foo: 0, // 1 - 1 = 0 - delete key ?
      ttt: 2, // 2 - 1 = 1
      bbb: 0, // 1 - 1 = 0 - delete key ?
    }

  // then check new message 'bbb'
  allMessages = {
      foo: 0,
      ttt: 2,
      bbb: 1, // 0 + 1 - print new message - return true
    }
