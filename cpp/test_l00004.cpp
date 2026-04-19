#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "l00004_median_two_sorted_arrays.cpp"

// Single reusable test suite
void runMedianTestSuite(IMedianSolution &sol)
{
    SECTION("LeetCode Example 1: Odd total length")
    {
        vector<int> n1 = {1, 3}, n2 = {2};
        CHECK(sol.findMedianSortedArrays(n1, n2) == Approx(2.0));
    }
    SECTION("LeetCode Example 2: Even total length")
    {
        vector<int> n1 = {1, 2}, n2 = {3, 4};
        CHECK(sol.findMedianSortedArrays(n1, n2) == Approx(2.5));
    }
    SECTION("Additional: One empty array")
    {
        vector<int> n1 = {}, n2 = {1};
        CHECK(sol.findMedianSortedArrays(n1, n2) == Approx(1.0));
    }
    SECTION("Additional: Different lengths")
    {
        vector<int> n1 = {1, 2}, n2 = {3, 4, 5, 6};
        CHECK(sol.findMedianSortedArrays(n1, n2) == Approx(3.5));
    }
    SECTION("Additional: Alternates")
    {
        vector<int> n1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        vector<int> n2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        CHECK(sol.findMedianSortedArrays(n1, n2) == Approx(10.5));
    }
    SECTION("Additional: Offset")
    {
        vector<int> n1 = {1, 2, 3, 4, 6, 8, 10};
        vector<int> n2 = {5, 7, 9, 11, 12, 13};
        CHECK(sol.findMedianSortedArrays(n1, n2) == Approx(7.0));
    }
    SECTION("Additional: Negative numbers")
    {
        vector<int> n1 = {-5, -3}, n2 = {-2, -1};
        CHECK(sol.findMedianSortedArrays(n1, n2) == Approx(-2.5));
    }
    SECTION("Error Handling: Both arrays empty")
    {
        vector<int> n1 = {}, n2 = {};
        CHECK_THROWS_AS(sol.findMedianSortedArrays(n1, n2), std::invalid_argument);
    }
}

TEST_CASE("Iterative Solution Performance", "[solution1]")
{
    Solution1 sol;
    runMedianTestSuite(sol);
}

TEST_CASE("Recursive Solution Performance", "[solution2]")
{
    Solution2 sol;
    runMedianTestSuite(sol);
}