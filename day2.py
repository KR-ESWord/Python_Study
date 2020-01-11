#실습 part 1
#1번
'''
print('%d' % 123)
print('%5d' % 123)
print('%05d' % 123)

print('%f' % 123.45)
print('%7.1f' % 123.45)
print('%7.3f' % 123.45)
'''
#2번
'''
print('%d %5d %05d' % (123, 123, 123))
print('{0:d} {1:5d} {2:05d}'.format(123, 123, 123))
print('{2:d} {1:d} {0:d}'.format(100, 200, 300))

print('\n줄바꿈\n연습')
print('\t탭키\t연습')
print('글자가 \"강조\"되는 효과1')
print('글자가 \'강조\'되는 효과2')
print('\\\\\\역슬래쉬 세 개 출력')
'''
#3번
'''
print('%5s' % ('*' *1))
print('%5s' % ('*' *2))
print('%5s' % ('*' *3))
print('%5s' % ('*' *4))
print('%5s' % ('*' *5))

print('%10s' % 'hi' + 'Dave')
print('%-10s' % 'hi' + 'Dave')
'''
#4번
'''
star = int(input('Input a number : '))
line = int(input('Input a line : '))
cnt = 0

while cnt < line :
    cnt += 1
    print((('*' * cnt) + (' ' * (line - cnt))) * star)
'''
#5번
'''
r = int(input('Input a number : '))
pi = 3.14
circleference = 2 * pi * r
Area = pi * r**2

print('Circleference = {0:3.1f}'.format(circleference))
print('Area          = {0:3.1f}'.format(Area))
'''
#6번
'''
a = 10
a += 5; print(a)
a -= 5; print(a)
a *= 5; print(a)
a /= 5; print(a)
a //= 5; print(a)
a %= 5; print(a)
a **= 5; print(a)
'''
#7번
'''
money = int(input('지폐로 교환할 돈은 얼마? '))

print('50000원 지폐 ==> {}장'.format(money//50000))
print('10000원 지폐 ==> {}장'.format((money%50000)//10000))
print('5000원 지폐 ==> {}장'.format((money%10000)//5000))
print('1000원 지폐 ==> {}장'.format((money%5000)//1000))
print('지폐로 바꾸지 못한 돈 ==> {}원'.format(money%1000))
print('지폐로 바꾸기 위해 추가로 필요한 돈 ==> {}원'.format(1000-(money%1000)))
'''
#8번
'''
w = float(input('몸무게를 kg 단위로 입력 : '))
h = float(input('키를 미터 단위로 입력 : '))
bmi = w / h**2
print('당신의 BMI = {}'.format(bmi))
'''
#9번
'''
i = int(input('투입한 돈 : '))
p = int(input('물건 값 : '))
c = i - p
print('거스름돈 : {}'.format(c))
print('500원 동전의 개수 : {}'.format(c//500))
print('100원 동전의 개수 : {}'.format((c%500)//100))
print('거스르지 못한 잔액 : {}원'.format(c%100))
'''
#실습 part 2
#1번
'''
print('Input number')
i = int(input())
print('*' * 15 + '{}dan'.format(i) + '*' * 15)
cnt = 1
while cnt < 10 :
    print('{}'.format(i) + ' X ' + '{}'.format(cnt) + ' = ' + '{}'.format(i*cnt))
    cnt += 1
print('*' * 34)
'''
#2번
'''
while True :
    print('Input number')
    i = int(input())
    if i == 99 :
        break
    if i < 1:
        continue    
    print('*' * 15 + '{}dan'.format(i) + '*' * 15)
    cnt = 1
    while cnt < 10 :
        print('{}'.format(i) + ' X ' + '{}'.format(cnt) + ' = ' + '{}'.format(i*cnt))
        cnt += 1
    print('*' * 34)
'''
#3번
'''
while True :
    year = int(input('연도를 입력하세요 : '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
        print('{}년은 윤년입니다.'.format(year))
    else :
        print('{}년은 윤년이 아닙니다.'.format(year))
'''
#실습1
'''
jumsu = 55
res = ' '
if jumsu >= 60 :
    res = 'Pass'
else :
    res ='Fail'
print(res)
'''
#실습2
'''
g = int(input('점수를 입력하세요 : '))
if g >=95 :
    print('A+')
elif g < 95 and g >= 90 :
    print('A')
elif g < 90 and g >= 80 :
    print('B+')
elif g < 80 and g >= 70 :
    print('B')
elif g < 70 and g >= 60 :
    print('C+')
elif g < 60 and g >= 50 :
    print('C')
elif g < 50 and g >= 40 :
    print('D+')
elif g < 40 and g >= 30 :
    print('D')
else :
    print('F')
print('학점입니다. ^^')
'''
#실습 part 3
#1번
'''
a = 'Python World'
print(a[0])
print(a[11])
print(a[-1])
print(a[-12])

a = 'Hello world'
print(a[0:11])
print(a[:5])
print(a[3:])
print(a[:])
'''
#2번
'''
a = 'Python world'
print(a.upper())
print(a.replace('o', 'a'))

a = 'What a wonderful Python'
print(a.split('w'))

year = 2018
rank = 12
gdp = '1조6194억'

a = '{}년 한국의 GDP는 {}로 세계 {}위 입니다.'.format(year, gdp, rank)
print(a)
'''
#3번
'''
ss = 'Python is Easy. 그래서 programming이 재미있습니다.^^'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())
'''
#실습 part 4
#1번
'''
aa = [10, 20, 30 ,40]
print('aa[-1]은 %d, aa[-2]는 %d'%(aa[-1], aa[-2]))

aa = [10, 20, 30, 40]
print(aa[0:3])
print(aa[2:4])
'''
#2번
'''
aa = [10, 20, 30, 40]
print(aa[2:])
print(aa[:2])

aa = [10, 20, 30]
bb = [40, 50, 60]
print(aa + bb)
print(aa * 3)
'''
#3번
'''
aa = [10, 20, 30, 40, 50, 60, 70]
print(aa[::2])
print(aa[::-2])
print(aa[::-1])
'''
#4번
'''
aa = [10, 20, 30]
aa[1] = 200
print(aa)

aa = [10, 20, 30]
aa[1:2] = [200, 201]
print(aa)
'''
#5번
'''
aa = [10, 20, 30]
aa[1] = [200, 201]
print(aa)

aa = [10, 20, 30]
del(aa[1])
print(aa)
'''
#6번
'''
aa = [10, 20, 30, 40, 50]
aa[1:4] = []
print(aa)

aa = [10, 20, 30]; aa = []; print(aa)
aa = [10, 20, 30]; aa = None; print(aa)
aa = [10, 20, 30]; del(aa); print(aa)
'''
#실습 part 5
#1번
'''
for i in range(6) :
    print('i = ', i)
for i in range(10) :
    print('9 * {} = {}'.format(i, 9*i))
'''
#2번
'''
count = 0
while count < 10 :
    count += 1
    print(count)

for count in range(1,11,1) :
    print(count)
for count in range(1,11) :
    print(count)
for count in range(11) :
    print(count)
'''
#3번
'''
s = 0
for i in [1, 2, 3, 4, 5]:
    s += 1
print('s : ', s)

s = 0
for i in range(1. 6) :
    s += 1
print('s : ', s)
'''
#4번
'''
s = 0
for i in [5, 4, 3, 2, 1]:
    s += 1
print('s : ', s)

s = 0
for i in range(5,0,-1) :
    s += 1
print('s : ', s)
'''
#5번
'''
a = int(input('값을 입력하세요 : '))
s = 0
for i in range(1, a+1) :
    s = s + i
print('1에서 {}까지의 합계 : {}'.format(a, s))
'''
#6번
'''
s = int(input('시작 값을 입력하세요 : '))
e = int(input('끝 값을 입력하세요 : '))
a = int(input('증가값을 입력하세요 : '))
c = 0
for i in range(s, e+1, a) :
    c = c + i
print('{}에서 {}까지 {}씩 증가시킨 값의 합계 : {}'.format(s, e, a, c))
'''
#7번
'''
d = int(input('단을 입력하세요 : '))
for i in range(10):
    print('{} X {} = {}'.format(d, i, d*i))
'''
#8번
'''
for a in range(2, 10) :
    print('#  {}단  #'.format(a), end = ' ')
print()
for b in range(1,10) :
    for c in range(2,10) :
        print('%d X %d = %2d' % (c, b, b*c), end = ' ')
'''
