# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        head = res

        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next

        if l1:
            res.next = l1
        elif l2:
            res.next = l2

        return head.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if len(lists) == 0:
            return None
        

        i = 0
        last = len(lists)-1
        j = last
        
        while last != 0 :
            i = 0
            j =last
            while i < j:
                lists[i] = self.mergeTwoLists(lists[i],lists[j])
                i += 1
                j -= 1
                last = j 
                
        return lists[0]
            
        
