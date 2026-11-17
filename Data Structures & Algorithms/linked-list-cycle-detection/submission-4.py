# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head
        if not fast.next:
            return False
        fast = fast.next
        while fast:
            if fast.val != slow.val:
                if fast.next == None:
                    return False
                fast = fast.next
                slow = slow.next
                if fast.next == None:
                    return False
                fast = fast.next
            if fast.val == slow.val:
                return True
        return False
        
        