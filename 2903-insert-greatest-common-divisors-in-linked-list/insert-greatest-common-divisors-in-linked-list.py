# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root=head
        while root.next:
            node=ListNode(math.gcd(root.val,root.next.val))
            node.next=root.next
            root.next=node
            root=root.next.next
        return head
