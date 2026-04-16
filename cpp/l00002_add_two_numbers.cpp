
// https://leetcode.com/problems/add-two-numbers/

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *c1 = l1, *c2 = l2;
        ListNode *result = nullptr, *cr = nullptr;
        int sum, carry = 0;
        while ((c1 != nullptr) || (c2 != nullptr))
        {
            sum = carry;
            if (c1 != nullptr)
            {
                sum = sum + c1->val;
                c1 = c1->next;
            }
            if (c2 != nullptr)
            {
                sum = sum + c2->val;
                c2 = c2->next;
            }
            int digit = sum % 10;
            carry = sum / 10;
            ListNode *resultNode = new ListNode(digit, nullptr);
            if (result == nullptr)
            {
                result = resultNode;
            }
            else
            {
                cr->next = resultNode;
            }
            cr = resultNode;
        }
        if (carry > 0)
        {
            ListNode *resultNode = new ListNode(carry, nullptr);
            cr->next = resultNode;
        }
        return result;
    }
};