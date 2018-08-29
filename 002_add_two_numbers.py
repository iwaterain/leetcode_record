# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode((l1.val + l2.val) % 10)
        current = head
        carry = (l1.val + l2.val) // 10
        while l1.next is not None or l2.next is not None:
            num1 = 0
            num2 = 0
            if l1.next is not None:
                l1 = l1.next
                num1 = l1.val
            if l2.next is not None:
                l2 = l2.next
                num2 = l2.val
            current.next = ListNode((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) // 10
            current = current.next
        if carry != 0:
            current.next = ListNode(carry)
        return head
