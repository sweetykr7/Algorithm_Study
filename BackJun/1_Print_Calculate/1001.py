

#a=int(input("첫번째 수를 입력하세요."))
#b=int(input("두번째 수를 입력하세요."))

#이 문제는 한번에 두개를 받아서 처리를 하라고 하는 문제였다.
#그런데 위와 같이 풀어서 런타임에러가 난것이다.
#아래와 같은 형태로 맵으로 받아서 처리를 해주면 된다.
a, b = map(int, input().split())
print(a-b)