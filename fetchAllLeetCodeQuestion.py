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