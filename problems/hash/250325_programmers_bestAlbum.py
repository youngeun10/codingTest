# Level: 3
# Title: 베스트 앨범

# 1. 속한 노래가 많이 재생된 장르 수록
# 2. 장르 내 많이 재생된 노래
# 3. 장르 내 재생 횟수가 같으면 고유 번호가 낮은 노래

from sortedcontainers import SortedDict

def solution(genres, plays):
    answer = []

    n = 0
    tot = SortedDict()

    for g, p in zip(genres, plays):
        if g not in tot:
            tot[g] = p
        else:
            tot[g] += p
        print(tot)
    #     if g not in m:
    #         m[g] = [(n, p)]
    #     else:
    #         m[g].append((n, p))
    #     n += 1
    #
    # print(m)

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
