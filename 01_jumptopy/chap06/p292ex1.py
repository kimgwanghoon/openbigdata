s='aaabbccccca'
count=0
result=s[0]
for i in s:
    if i == result[-1]: #result의 끝문자와 i의 값 비교
        count += 1
    else:
        result += str(count) + i
        count = 1
result += str(count)

print(result)