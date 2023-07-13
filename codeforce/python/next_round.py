# A. Next Round
# https://codeforces.com/problemset/problem/158/A
# Input
# 8 5
# 10 9 8 7 7 7 5 5
# Output 6

n, k = map(int, input().split())
scores = list(map(int, input().split()))

kth_place_score = scores[k - 1]

count = 0
for score in scores:
    if score > 0 and score >= kth_place_score:
        count += 1

print(count)
