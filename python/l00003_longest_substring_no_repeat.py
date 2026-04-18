# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import deque


def solve(s: str) -> int:
    char_map = {}  # Stores: {character: last_seen_index}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If we've seen the char AND it's inside our current window
        if char in char_map and char_map[char] >= left:
            # Jump left pointer to the right of the previous occurrence
            left = char_map[char] + 1

        # Update/Record the character's latest position
        char_map[char] = right

        # Calculate current window size
        max_len = max(max_len, right - left + 1)

    return max_len


def solve2(s: str) -> int:
    queue = deque()
    left = 0
    maxSub = 0
    for right in range(len(s)):
        char = s[right]
        if char in queue:
            while True:
                left = left + 1
                if queue.popleft() == char:
                    break
        queue.append(char)
        maxSub = max(maxSub, right - left + 1)
    return maxSub
