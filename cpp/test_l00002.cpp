#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "l00002_add_two_numbers.cpp"
#include <vector>

// Helper to convert vector to linked list
ListNode *createList(std::vector<int> nums)
{
    ListNode dummy(0);
    ListNode *curr = &dummy;
    for (int x : nums)
    {
        curr->next = new ListNode(x);
        curr = curr->next;
    }
    return dummy.next;
}

// Helper to convert linked list to vector for easy comparison
std::vector<int> listToVec(ListNode *node)
{
    std::vector<int> res;
    while (node)
    {
        res.push_back(node->val);
        node = node->next;
    }
    return res;
}

TEST_CASE("Add Two Numbers - LeetCode Official Cases", "[leetcode]")
{
    Solution sol;

    SECTION("Example 1: Standard addition")
    {
        ListNode *l1 = createList({2, 4, 3});
        ListNode *l2 = createList({5, 6, 4});
        ListNode *result = sol.addTwoNumbers(l1, l2);
        CHECK(listToVec(result) == std::vector<int>{7, 0, 8});
    }

    SECTION("Example 2: Zero values")
    {
        ListNode *l1 = createList({0});
        ListNode *l2 = createList({0});
        ListNode *result = sol.addTwoNumbers(l1, l2);
        CHECK(listToVec(result) == std::vector<int>{0});
    }

    SECTION("Example 3: Different lengths and multiple carries")
    {
        ListNode *l1 = createList({9, 9, 9, 9, 9, 9, 9});
        ListNode *l2 = createList({9, 9, 9, 9});
        ListNode *result = sol.addTwoNumbers(l1, l2);
        // Result: 8,9,9,9,0,0,0,1
        CHECK(listToVec(result) == std::vector<int>{8, 9, 9, 9, 0, 0, 0, 1});
    }
}