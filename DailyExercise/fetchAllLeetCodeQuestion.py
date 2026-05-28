import requests
import random

# ==== CONFIGURATION ====
FAVORITE_SLUG = "vdgv82rh"  # your list id
LEETCODE_SESSION = "PASTE_YOUR_LEETCODE_SESSION_COOKIE_HERE"
CSRFTOKEN = "PASTE_YOUR_CSRFTOKEN_COOKIE_HERE"
# =======================

session = requests.Session()

session.cookies.update({
    "LEETCODE_SESSION": LEETCODE_SESSION,
    "csrftoken": CSRFTOKEN,
})

session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "Referer": f"https://leetcode.com/problem-list/{FAVORITE_SLUG}/",
    "x-csrftoken": CSRFTOKEN,
    "content-type": "application/json",
})

url = "https://leetcode.com/graphql/"

query = """
query favoriteQuestionList($favoriteSlug: String!) {
  favoriteQuestionList(
    favoriteSlug: $favoriteSlug
  ) {
    questions {
      questionFrontendId
      title
      titleSlug
      difficulty
      paidOnly
      status
    }
  }
}
"""

payload = {
    "operationName": "favoriteQuestionList",
    "query": query,
    "variables": {
        "favoriteSlug": FAVORITE_SLUG
    }
}

resp = session.post(url, json=payload)

if resp.status_code != 200:
    print("Request failed with status:", resp.status_code)
    print(resp.text)
    raise SystemExit

data = resp.json()

questions = data.get("data", {}) \
                .get("favoriteQuestionList", {}) \
                .get("questions", [])

print(f"Total questions in list '{FAVORITE_SLUG}': {len(questions)}")
print("-" * 80)

# for q in questions:
#     qid = q["questionFrontendId"]
#     title = q["title"]
#     slug = q["titleSlug"]
#     difficulty = q["difficulty"]
#     paid_only = q["paidOnly"]

#     url = f"https://leetcode.com/problems/{slug}/"

#     print(f"[{qid}] {title}")
#     print(f"  Difficulty: {difficulty} | Premium only: {paid_only}")
#     print(f"  URL: {url}")
#     print()

# Randomly pick up to 5 questions from the list
sample_size = min(5, len(questions))
sampled_questions = random.sample(questions, sample_size) if len(questions) > 0 else []

def make_link(text: str, url: str) -> str:
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

for q in sampled_questions:
    qid = q["questionFrontendId"]
    title = q["title"]
    slug = q["titleSlug"]
    url = f"https://leetcode.com/problems/{slug}/"

    clickable = make_link(title, url)

    print(f"[{qid}] {title}")
    #print(f"  URL: {url}")
    print(f"  URL: {clickable}")
    print()

"""
# LeetCode 核心题单 V5.0 — 肌肉记忆版

---
## 0. Arrays & Hashing
| 1 | Two Sum | Amazon #1，每家公司必考 |
| 49 | Group Anagrams | Microsoft / Meta top 5 |
| 128 | Longest Consecutive Sequence | Google / Meta 高频，Hash Set 模式 |
| 238 | Product of Array Except Self | Apple 高频，无除法技巧 |
# May 8 49, 128, 238

---
## 1. Linked List
| 206 | Reverse Linked List 
| 141 | Linked List Cycle 
| 21 | Merge Two Sorted Lists 
| 19 | Remove Nth Node From End 
| 138 | Copy List with Random Pointer 
| 142 | Linked List Cycle II 
| 143 | Reorder List 
| 23 | Merge K Sorted Lists | 结合 Heap |

# May 11 - 138, 23 

---
## 2. Two Pointers & Sliding Window

### 快慢 / 左右指针
| 977 | Squares of a Sorted Array
| 15 | 3Sum
| 11 | Container With Most Water | |
| 42 | Trapping Rain Water | 高阶必练 |

# May 13 - 11, 42

### 滑动窗口
| 209 | Minimum Size Subarray Sum | |
| 3 | Longest Substring Without Repeating Characters | |
| 424 | Longest Repeating Character Replacement | Microsoft top 5 |
| 567 | Permutation in String | 固定窗口模式 |
| 76 | Minimum Window Substring | Hard，但必会 |

---
# 1971, 143, 424, 752, 203 - May 28th
# 567, 76 - May 28th 

## 3. Stack & Queue

### 基础

| # | 题目 |
|---|------|
| 20 | Valid Parentheses |
| 155 | Min Stack |
| 150 | Evaluate Reverse Polish Notation |

### 单调栈

| # | 题目 | 说明 |
|---|------|------|
| 739 | Daily Temperatures | |
| 84 | Largest Rectangle in Histogram | Google / Amazon 高频 Hard |

### 单调队列

| # | 题目 | 说明 |
|---|------|------|
| 239 | Sliding Window Maximum | 肌肉记忆级别 |

---

## 4. Binary Search

### 基础二分

| # | 题目 |
|---|------|
| 704 | Binary Search |
| 34 | Find First and Last Position of Element |
| 33 | Search in Rotated Sorted Array |
| 153 | Find Minimum in Rotated Sorted Array |

### 二分答案

| # | 题目 | 说明 |
|---|------|------|
| 875 | Koko Eating Bananas | 2025–26 趋势模式，必掌握 |
| 1011 | Capacity To Ship Packages Within D Days | 同上 |

---

## 5. Priority Queue / Heap

| # | 题目 |
|---|------|
| 215 | Kth Largest Element in an Array |
| 347 | Top K Frequent Elements |
| 973 | K Closest Points to Origin |

---

## 6. Design

| # | 题目 | 说明 |
|---|------|------|
| 146 | LRU Cache | ⭐ 新增 — 全 FAANG 必考，Hash Map + 双向链表 |

> 这是唯一需要掌握的 Design 题。它直接考查你对数据结构组合的理解，是每家公司的标准考题。

---

## 7. DFS / BFS / Backtracking

### 树

| # | 题目 | 说明 |
|---|------|------|
| 104 | Maximum Depth of Binary Tree | |
| 226 | Invert Binary Tree | |
| 543 | Diameter of Binary Tree | ⭐ 新增 — Meta / Salesforce 高频，DFS 后序模式 |
| 110 | Balanced Binary Tree | |
| 98 | Validate Binary Search Tree | BST 基础，每家公司必考 |
| 236 | Lowest Common Ancestor of a Binary Tree | |
| 124 | Binary Tree Maximum Path Sum | Hard，但高频 |
| 297 | Serialize and Deserialize Binary Tree | Google 2024–25 top 3 |

### 岛屿 / 矩阵

| # | 题目 |
|---|------|
| 200 | Number of Islands |
| 994 | Rotting Oranges |
| 542 | 01 Matrix |

### 回溯

| # | 题目 |
|---|------|
| 46 | Permutations |
| 78 | Subsets |
| 39 | Combination Sum |
| 79 | Word Search |

---

## 8. Graph

| # | 题目 | 说明 |
|---|------|------|
| 207 | Course Schedule | 拓扑排序 |
| 210 | Course Schedule II | 拓扑排序 |
| 269 | Alien Dictionary | ⭐ 新增 — 全 FAANG 必考，拓扑排序 Hard |
| 547 | Number of Provinces | 并查集 |
| 743 | Network Delay Time | Dijkstra 模板 |
| 417 | Pacific Atlantic Water Flow | 多源 BFS，Google / Meta top 10 |

---

## 9. Dynamic Programming

### 入门

| # | 题目 |
|---|------|
| 70 | Climbing Stairs |
| 198 | House Robber |
| 213 | House Robber II |
| 121 | Best Time to Buy and Sell Stock |

### 经典

| # | 题目 |
|---|------|
| 322 | Coin Change |
| 139 | Word Break |
| 300 | Longest Increasing Subsequence |

### 二维

| # | 题目 | 说明 |
|---|------|------|
| 62 | Unique Paths | |
| 1143 | Longest Common Subsequence | |
| 72 | Edit Distance | 大厂常客，Google / Dropbox 高频 |

### 背包

| # | 题目 |
|---|------|
| 416 | Partition Equal Subset Sum |

---

## 10. Trie

| # | 题目 |
|---|------|
| 208 | Implement Trie (Prefix Tree) |
| 211 | Design Add and Search Words Data Structure |

---

## 11. Intervals & Greedy

| # | 题目 | 说明 |
|---|------|------|
| 56 | Merge Intervals | Amazon / Meta / Stripe 最高频 |
| 57 | Insert Interval | |
| 253 | Meeting Rooms II | 高频（Premium，可用 #1094 代替）|
| 435 | Non-overlapping Intervals | |

---

## V5.0 变更摘要

| 变更 | 题目 | 原因 |
|------|------|------|
| ⭐ 新增 | #138 Copy List with Random Pointer | 全公司高频，Hash Map + 链表组合模式 |
| ⭐ 新增 | #543 Diameter of Binary Tree | Meta / Salesforce 2025 高频，DFS 后序模式 |
| ⭐ 新增 | #146 LRU Cache（新 Design 章节） | 全 FAANG 必考，2025–26 报告一致验证 |
| ⭐ 新增 | #269 Alien Dictionary | 全 5 家 FAANG 考过，拓扑排序 Hard 代表题 |
| 📌 排序调整 | 滑动窗口题目按难度重排 | 学习曲线更合理 |
| 📌 章节重排 | Design 独立成章，树题补充 #543 | 结构更清晰 |
"""

# 232. 1091, 752!, 286 - Mar 2 
# mar 8 - 496/35? (搞混！) 362
# mar 11 - 83, 3
# mar 15 - 752
# nar 22 - 153, 111
# mar 29 - 695
# apr 1 -  79, 111, 994, 733, 752, 94, 110, 286, 1971, 33, 153