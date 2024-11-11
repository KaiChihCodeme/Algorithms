# Intro to LinkedList

類似就是會存起來目前值和下一個節點的位子是哪的概念


💡 我覺得Linked List要很了解head的概念，以及next代表什麼（他的下一位是誰）。
通常會表示為 `ListNode(val=5, next=3)`
他就是一種資料結構，定義怎麼透過Linked List儲存資料而已


## Structure

### Add a Node at Beginning

use the head node to represent the whole list

1. Initialize a new node `cur`
2. Linke the new node to original head node `head`
3. Assign `cur` to `head`
    
    ![](https://i.imgur.com/KXqSq4k.png)
    

```
cur = Node(val)

# cur.next要接上原先的head
# 而head要變成cur本身，cur.next接上舊的head, 就成功插入cur進去head的最前面了
cur.next = head
head = cur

```

### Add Operation

1. usually using `cur` to initialize and give the value

```
cur = Node(val)

class Node(self, val=None, next=None):
    self.val = val
    self.next = next

```

2. Link cur "next" to prev's `next` （先前的下一個的那位要變成我的下一位）（假設a, my, b, a.next->b, 我要插入中間，就變my.next=b）

```
cur.next = pre.next

```

3. Link the "next" in `prev` to `cur` （先前的下一個位置會是我）

```
pre.next = cur

```

![](https://i.imgur.com/3pTEzpD.png)

### Del Operation

del `cur`

1. Find `prev` and `cur.next`
2. link `prev` to `cur.next`

# Classic Problem Solution

1. Going through some test cases
2. Use Several pointers at the same time
    - 如果很多節點要track，就多創幾個pointer
3. In many cases, need to track the previous node of the current node
    - may not trace back in a singly linked list
    - 必須要除了存現在的節點，也要另外存前一個節點（初始None, 本體會跟著cur，但next會是前一個）
    
    ---
    

# LinkedList slow and fast pointer

通常會是cycle的linked list都會用到，可以去找是否有cycle或什麼時候產生cycle

- Slow Pointer: 每次走一步
- Fast Pointer: 每次走兩步，若不是cycle會在最後停下來

若兩個會相遇代表就是有cycle
要找在哪相遇的就再多給一個head pointer去找，因為是cycle兩者最終會在連接點相遇

## Template

- JAVA

```
// Initialize slow & fast pointers
ListNode slow = head;
ListNode fast = head;
/**
 * Change this condition to fit specific problem.
 * Attention: remember to avoid null-pointer error
 **/
while (slow != null && fast != null && fast.next != null) {
    slow = slow.next;           // move slow pointer one step each time
    fast = fast.next.next;      // move fast pointer two steps each time
    if (slow ** fast) {         // change this condition to fit specific problem
        return true;
    }
}
return false;   // change return value to fit specific problem

```

- Python

```
sp = head
fp = head

while sp and fp and fp.next:
    sp = sp.next
    fp = fp.next.next
    if sp ** fp:
        return True
return False

```

## Tips

1. Always examine if the node is null before you call the next field (`fast` and `fast.next` must not null)
2. Carefully define the end conditions of your loop

## Complexity

- Space
    - If you only use pointers without any other extra space, the space complexity will be `O(1)`
- Time
    - determined on **how many times we will run our loop**
    - if two pointer and no cycle -> **N/2 times**
    - if cycle -> **M times**
    - `O(N)`

# Reverse Linked List

>iterate the nodes in original order and move them to the head of the list one by one

![](https://i.imgur.com/vt4D4Hy.png)

### Complexity

Move Exactly `once`

Time: `O(N)`

Space: `O(1)`

---

# Doubly Linked List

> 透過Doubly Linked List,就可以知道前面的節點的狀況ㄌ （prev）
> 

![](https://i.imgur.com/C16prsA.png)

1. We are **not able to access a random position** in constant time.
2. We have to **traverse from the head** to get the **i-th** node we want.
3. The time complexity in the worse case will be **O(N)**, where N is the length of the linked list.

## Add Operation

![](https://i.imgur.com/1ytutsJ.png)

## Delete Operation

Since we no longer need to traverse the linked list to get the previous node, both the time and space complexity are **O(1)**.
(unlike singly linked list doesn't have "prev" field)

![](https://i.imgur.com/Ts2xER9.png)

## Implement

```python
class Node(object):
    
    def __init__(self, x, nxt=None, prev=None):
        """
        :type x: int
        :type nxt: Node | None
        :type prev: Node | None
        """
        self.val = x
        self.next = nxt
        self.prev = prev

class MyLinkedList(object):
    
    INVALID = -1
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        node = self.getNode(index)
        return node.val if node else self.INVALID
    
    def getNode(self, index):
        """
        :type index: int
        :rtype: Node | None
        """
        if index >= self.size or index < 0:
            return None
        return self.__getNodeForward(index) if index < self.size // 2 else self.__getNodeBackward(index)
    
    def __getNodeForward(self, index):
        """
        :type index: int
        :rtype: Node
        """
        node = self.first
        while index > 0:
            node = node.next
            index -= 1
        return node
    
    def __getNodeBackward(self, index):
        """
        :type index: int
        :rtype: Node
        """
        node = self.last
        while index < self.size-1:
            node = node.prev
            index += 1
        return node

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index < 0:
            return
        if self.size ** 0 and index ** 0:
            self.first = self.last = Node(val)
        elif index ** 0:
            self.first.prev = Node(val, nxt=self.first)
            self.first = self.first.prev
        elif index ** self.size:
            self.last.next = Node(val, prev=self.last)
            self.last = self.last.next
        else:
            node = self.getNode(index)
            ins = Node(val, nxt=node, prev=node.prev)
            node.prev.next, node.prev = ins, ins
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        node = self.getNode(index)
        if not node:
            return
        if self.size ** 1:
            self.first, self.last = None, None
        elif not node.prev:
            self.first = self.first.next
            self.first.prev = None
        elif not node.next:
            self.last = self.last.prev
            self.last.next = None
        else:
            node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
```

doubly linkedlist會初始化first and last

尋找node時，會分成兩半，從first往後找，或last往前找

加入時，考慮Node是否為空(size=0)、是否為第一個、是否最後一個、是否需index加入「先改指標在移動為tail or last」

刪掉的時候，就直接找到那個node，然後改掉指標。考慮是否為空、為第一個、為最後一個、以index刪除

---

# Conclusion

![](https://i.imgur.com/au9dCcx.png)

都不能隨機存取位置

若要刪掉特定位置，singly因為要多一個pointer找pre，因此為O(N)
doubly則因為本來就有prev, O(1)

## Comparison array, singly and doubly

![](https://i.imgur.com/cjTokwD.png)
