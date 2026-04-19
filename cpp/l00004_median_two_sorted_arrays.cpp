#include <vector>
#include <stdexcept>
#include <iostream>
using namespace std;

#include <vector>
#include <algorithm>
#include <climits>
#include <stdexcept>

using namespace std;

class IMedianSolution
{
public:
    virtual ~IMedianSolution() {} // Virtual destructor is important!
    virtual double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) = 0;
};

class Solution1 : public IMedianSolution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        // Optimization: Ensure nums1 is the shorter array
        if (nums1.size() > nums2.size())
        {
            return findMedianSortedArrays(nums2, nums1);
        }

        int n1 = nums1.size();
        int n2 = nums2.size();

        if (n1 == 0 && n2 == 0)
        {
            throw invalid_argument("Both arrays cannot be empty.");
        }

        int low = 0;
        int high = n1;

        while (low <= high)
        {
            // Partition positions
            int partition1 = low + (high - low) / 2;
            int partition2 = (n1 + n2 + 1) / 2 - partition1;

            // Values around partition 1 (nums1)
            int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
            int minRight1 = (partition1 == n1) ? INT_MAX : nums1[partition1];

            // Values around partition 2 (nums2)
            int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
            int minRight2 = (partition2 == n2) ? INT_MAX : nums2[partition2];

            // Check if we found the correct partition
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1)
            {
                // If total length is even
                if ((n1 + n2) % 2 == 0)
                {
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
                }
                // If total length is odd
                else
                {
                    return max(maxLeft1, maxLeft2);
                }
            }
            // Too far right in nums1, move left
            else if (maxLeft1 > minRight2)
            {
                high = partition1 - 1;
            }
            // Too far left in nums1, move right
            else
            {
                low = partition1 + 1;
            }
        }

        throw runtime_error("Input arrays are not sorted or contain invalid data.");
    }
};

class Solution2 : public IMedianSolution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int size1 = nums1.size();
        int size2 = nums2.size();
        if ((size1 == 0) && (size2 == 0))
        {
            throw invalid_argument("both lists cannot be empty");
        }
        else if (size1 == 0)
        {
            return singleMedian(nums2);
        }
        else if (size2 == 0)
        {
            return singleMedian(nums1);
        }
        isEven = (((size1 + size2) % 2) == 0);
        eliminate = ((size1 + size2 - 1) / 2);
        return findMedian(nums1, size1, size1 - 1, 0, nums2, size2, size2 - 1, 0);
    }

private:
    bool isEven = false;
    int eliminate = 0;
    double findMedian(vector<int> &nums1, int size1, int r1, int l1, vector<int> &nums2, int size2, int r2, int l2)
    {
        if (eliminate == 0)
        {
            if (isEven)
            {
                int second;
                if (l1 == (size1 - 1))
                {
                    second = nums2[l2];
                }
                else
                {
                    second = min(nums1[l1 + 1], nums2[l2]);
                }
                return (nums1[l1] + second) / 2.0;
            }
            else
            {
                return nums1[l1];
            }
        }
        int mid1 = l1 + (r1 - l1) / 2;
        int mid2 = l2 + (r2 - l2) / 2;
        if (nums1[mid1] < nums2[mid2])
        {
            return adjust(nums1, size1, r1, mid1, l1, nums2, size2, r2, mid2, l2);
        }
        else
        {
            return adjust(nums2, size2, r2, mid2, l2, nums1, size1, r1, mid1, l1);
        }
    }

    double adjust(vector<int> &nums1, int size1, int r1, int mid1, int l1, vector<int> &nums2, int size2, int r2, int mid2, int l2)
    {
        if ((mid1 == l1) && (mid2 > l2))
        {
            return findMedian(nums1, size1, r1, l1, nums2, size2, mid2, l2);
        }
        else if ((mid1 == l1) && (mid2 == l2))
        {
            eliminate -= 1;
            if (l1 == r1)
            {
                l2 = l2 + eliminate;
                if (isEven)
                {
                    return (nums2[l2] + nums2[l2 + 1]) / 2.0;
                }
                else
                {
                    return nums2[l2];
                }
            }
            else
            {
                if (nums1[l1 + 1] < nums2[l2])
                {
                    return findMedian(nums1, size1, r1, l1 + 1, nums2, size2, r2, l2);
                }
                else
                {
                    return findMedian(nums2, size2, r2, l2, nums1, size1, r1, l1 + 1);
                }
            }
        }
        else
        {
            int pel = mid1 - l1;
            int el = min(eliminate, pel);
            eliminate -= el;
            l1 += el;
            return findMedian(nums1, size1, r1, l1, nums2, size2, r2, l2);
        }
    }

    double singleMedian(vector<int> &nums)
    {
        if (nums.size() % 2 == 0)
        {
            int r = nums.size() / 2;
            return (nums[r - 1] + nums[r]) / 2.0;
        }
        else
        {
            return nums[nums.size() / 2];
        }
    }
};
