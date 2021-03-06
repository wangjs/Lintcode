'''
你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
写出一个函数将两个整数相加，用链表形式返回和。

思路：若两个链表均为空，返回False；若两个链表有一个为空时，直接返回另外一个不为空的链表即可；若两个均不为空，新链表的值为两链表对应结点的和，若和<10,则新链表生成下一结点将初始值置为0,代表无进位；否则ListNode(1),将初始值置为1,代表有进位。（当无进位且两个链表的next为空时，不产生新结点）
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addnode(self, node1, node2):
        if not node1 and not node2:
            return False
        elif not node1:
            return node2.val
        elif not node2:
            return node1.val
        else:
            return node1.val+node2.val
    
    def addLists(self, l1, l2):
        # write your code here
        ResultHead = ListNode(0)
        cur1 = l1
        cur2 = l2
        cur = ResultHead
        while(cur1 or cur2):
            cur.val = cur.val + self.addnode(cur1, cur2)
            if cur.val < 10:
                if cur1 and cur1.next or cur2 and cur2.next:
                    cur.next = ListNode(0)
            else:
                cur.val -= 10
                cur.next = ListNode(1)
            cur = cur.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        return ResultHead
