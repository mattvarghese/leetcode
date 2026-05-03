# 212 https://leetcode.com/problems/word-search-ii/

from collections import defaultdict
from typing import List, Set, Tuple


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class NeighborTracker:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.up = False
        self.down = False
        self.left = False
        self.right = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.triePath: List[TrieNode] = []
        self.path: List[NeighborTracker] = []
        self.visited: Set[Tuple[int, int]] = set()
        self.prefixes: List[str] = []
        self.m = 0
        self.n = 0
        self.results: List[str] = []
        self.depth = -1

    def insertWord(self, word: str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWord = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.__init__()
        if len(words) == 0:
            return []
        # First create the trie
        for word in words:
            self.insertWord(word)
        # Now search the board
        self.m = len(board)  # rows
        self.n = len(board[0])  # columns
        if self.m == 0 or self.n == 0:
            return []
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(board, i, j)
        return self.results

    def dfs(self, board: List[List[str]], row: int, col: int):

        char = board[row][col]
        if char not in self.root.children:
            return

        self.depth = -1  # We're doing depth as starting at 0 to match list indices
        self.checkAndAddStackEntry(board, row, col, self.root.children[char])

        while self.depth > -1:
            cur = self.path[self.depth]
            trieCur = self.triePath[self.depth]
            curChar = self.prefixes[self.depth]

            if trieCur.isWord:
                self.results.append("".join(self.prefixes))
                trieCur.isWord = False  # We found this word, so don't find it again

            if cur.left and cur.right and cur.up and cur.down:
                self.path.pop()  # Remove current
                self.visited.remove((cur.row, cur.col))
                self.prefixes.pop()
                trieCur = self.triePath.pop()
                if (not trieCur.isWord) and (len(trieCur.children) == 0):
                    trieParent = (
                        self.root if self.depth == 0 else self.triePath[self.depth - 1]
                    )
                    del trieParent.children[curChar]
                self.depth = self.depth - 1
                continue

            if not cur.up:
                cur.up = True  # Mark as processed
                if cur.row != 0:
                    newRow = cur.row - 1
                    newCol = cur.col
                    newChar = board[newRow][newCol]
                    if newChar in trieCur.children:
                        self.checkAndAddStackEntry(
                            board, newRow, newCol, trieCur.children[newChar]
                        )
                continue

            if not cur.down:
                cur.down = True  # Mark as processed
                if cur.row != (self.m - 1):
                    newRow = cur.row + 1
                    newCol = cur.col
                    newChar = board[newRow][newCol]
                    if newChar in trieCur.children:
                        self.checkAndAddStackEntry(
                            board, newRow, newCol, trieCur.children[newChar]
                        )
                continue

            if not cur.left:
                cur.left = True  # Mark as processed
                if cur.col != 0:
                    newRow = cur.row
                    newCol = cur.col - 1
                    newChar = board[newRow][newCol]
                    if newChar in trieCur.children:
                        self.checkAndAddStackEntry(
                            board, newRow, newCol, trieCur.children[newChar]
                        )
                continue

            if not cur.right:
                cur.right = True  # Mark as processed
                if cur.col != (self.n - 1):
                    newRow = cur.row
                    newCol = cur.col + 1
                    newChar = board[newRow][newCol]
                    if newChar in trieCur.children:
                        self.checkAndAddStackEntry(
                            board, newRow, newCol, trieCur.children[newChar]
                        )
                continue

    def checkAndAddStackEntry(
        self, board: List[List[str]], row: int, col: int, trieNode: TrieNode
    ):
        if (row, col) not in self.visited:
            char = board[row][col]
            self.triePath.append(trieNode)
            self.path.append(NeighborTracker(row, col))
            self.visited.add((row, col))
            self.prefixes.append(char)
            self.depth = self.depth + 1


class TrieNode2:
    def __init__(self):
        self.children = defaultdict(TrieNode2)
        self.word = None  # Store the whole word at the end node


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode2()
        for w in words:
            curr = root
            for char in w:
                curr = curr.children[char]
            curr.word = w

        rows, cols = len(board), len(board[0])
        results = []

        def dfs(r, c, node):
            char = board[r][c]
            next_node = node.children.get(char)

            if not next_node:
                return

            # Check if we found a word
            if next_node.word:
                results.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            # Backtracking: Mark as visited
            board[r][c] = "#"

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            # Backtracking: Restore the character
            board[r][c] = char

            # Optimization: Prune the Trie (remove leaf nodes with no children)
            if not next_node.children:
                del node.children[char]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return results
