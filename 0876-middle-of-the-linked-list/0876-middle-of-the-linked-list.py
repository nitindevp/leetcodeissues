# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            
class Solution():
    def middleNode(self,head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 

#create nodes         
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

# connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

solution = Solution()
result = solution.middleNode(node1)

if result:
    print("middle node:", result.val)
else:
    print("nothing")
