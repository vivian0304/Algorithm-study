# 10808번 알파벳 세기

# 1. input으로 문자열 받아옴
# 2. 알파벳 크기만큼의 요소 0인 리스트 선언
# 3. 아스키코드 사용해서 문자열의 i문자와 매칭
# 4. 리스트에 있는 값 print
# a = 97 (소문자만) -> list[0]
# ord() : 문자 -> 아스키코드 숫자

x = input()
li = [0] * 26

for i in x:
    li[ord(i)-97] += 1

for i in li:
    print( i, end=" ")

