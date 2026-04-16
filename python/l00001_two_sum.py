# https://leetcode.com/problems/two-sum/description/


def solve(nums, target):
    """
    Finds two numbers in an array that sum to a specific target using a one-pass hash map.

    This is the most time-efficient approach as it resolves the complement
    and the self-matching constraint in a single traversal.

    Args:
        nums (list[int]): A list of integers.
        target (int): The integer sum to search for.

    Returns:
        tuple[int, int] | tuple[]: The indices of the two numbers that add up to target,
                                   or an empty tuple if no solution exists.
    """
    seen = {}  # val : index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return ()


def solve2(nums, target):
    """
    Finds two numbers that sum to target using a two-pass grouping strategy.

    Maps each unique value to a list of its indices to handle duplicate
    values explicitly.

    Args:
        nums (list[int]): A list of integers.
        target (int): The integer sum to search for.

    Returns:
        tuple[int, int] | tuple[]: The indices of the two numbers,
                                   or an empty tuple if not found.
    """
    # Using 'index_map' instead of 'map' to avoid shadowing built-in functions
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map:
            index_map[num].append(i)
        else:
            index_map[num] = [i]

    for num, indices in index_map.items():
        diff = target - num
        if (diff == num) and (len(index_map[num]) > 1):
            return (indices[0], indices[1])
        elif (diff != num) and (diff in index_map):
            return (indices[0], index_map[diff][0])
    return ()
