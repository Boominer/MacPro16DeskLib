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
LeetCode 核心题单 (优化版 - 肌肉记忆级别)
以下是经过深思熟虑后的 LeetCode 终极核心题单 (V3.0)。
V3.0 终极核心题单：肌肉记忆版

1. Linked List (指针操作基石)
基础： 206 (反转), 141 (环), 21 (合并), 160 (相交)
进阶： 19 (删除倒数N), 23 (合并K个- 结合Heap), 142 (环形入口), 143 (重排链表)
2. Two Pointers & Sliding Window (线性最优解)
快慢/左右指针： 977 (平方数组), 15 (三数之和), 11 (盛水最多), 42 (接雨水 - 高阶必练)
滑动窗口： 209 (最小长度), 3 (无重复最长子串), 76 (最小覆盖子串 - Hard，但必会)
3. Stack & Queue (单调性与模拟)
基础： 20 (括号), 155 (最小栈), 150 (逆波兰)
单调栈 (核心)： 739 (每日温度), 84 (柱状图中最大矩形 - 选练)
单调队列： 239 (滑动窗口最大值 - 肌肉记忆级别)
4. Binary Search (不仅是在数组里找数)
基础二分： 704, 34 (范围查找), 33 & 153 (旋转数组)
二分答案 (高频)： 875 (爱吃香蕉的珂珂), 1011 (送货能力) —— 这类题面试极多，必须掌握逻辑
5. Priority Queue (Heap - 动态最值)
Top K： 215 (第K大), 347 (高频元素), 973 (最接近原点)
多路归并/动态： 23 (合并K个链表), 295 (数据流中位数)
6. DFS / BFS / Backtracking (搜索与穷举)
树： 104, 226, 110, 236 (最近公共祖先), 124 (最大路径和 - Hard但高频)
岛屿/矩阵： 200 (岛屿数量), 994 (腐烂橘子), 542 (01矩阵)
回溯 (模板)： 46 (全排列), 78 (子集), 39 (组合总和), 79 (单词搜索)
7. Graph (图论核心)
入度/拓扑排序： 207 (课程表), 210 (课程表II)
并查集 (Union-Find)： 547 (省份数量), 200 (也可用UF解)
最短路： 743 (Dijkstra 模板 - 属于 PQ 应用)
8. Dynamic Programming (决策与空间优化)
入门： 70, 198, 121
经典： 322 (零钱兑换), 139 (单词拆分), 300 (最长递增子序列)
二维： 62, 1143 (最长公共子序列), 72 (编辑距离 - 大厂常客)
背包： 416 (分割等和子集)
9. Trie (前缀树 - 字典类问题)
208 (实现 Trie), 211 (添加与搜索单词) —— 只需这两道，肌肉记忆就够了
10. Intervals & Greedy (区间与贪心)
56 (合并区间), 57 (插入区间), 253 (会议室II - 高频), 435 (无重叠区间)

"""

# 232. 1091, 752!, 286 - Mar 2 
# mar 8 - 496/35? (搞混！) 362
# mar 11 - 83, 3
# mar 15 - 752
# nar 22 - 153, 111
# mar 29 - 695
# apr 1 -  79, 111, 994, 733, 752, 94, 110, 286, 1971, 33