# Level: ?
# Title: 신규 아이디 추천

import re
import sys
input = sys.stdin.readline

def charChk(s):
    b = ''
    for c in s:
        if c in '0123456789abcdefghijklmnopqrstuvwxyz-_.':
            b += c
    return b


def solution(new_id):
    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2. 허용 문자외 나머지는 제거
    new_id = charChk(new_id)
    # 3. ..이상 -> .
    new_id = re.sub(r'\.+', '.', new_id)
    # 4. 처음, 끝에 . 있으면 제거
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        # 5. 빈 문자열 -> a 대입
        new_id = 'a'
    if len(new_id) <= 2:
        # 7. new_id 길이가 2자 이하면 마지막 문자를 길이 3이 될 떄까지 반복
        return new_id + (new_id[-1]*(3-len(new_id)))
    elif len(new_id) > 15:
        # 6. 길이가 16자 이상이면 앞의 15자리만 남기기 -> 마침표로 끝나면 마침표 제거
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    return new_id

print(solution(input()))