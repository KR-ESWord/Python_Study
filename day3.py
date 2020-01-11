#실습 part 1
#1번
'''
import random

numbers = []
for num in range(0,10) :
    numbers.append(random.randrange(0,10))

print('생성된 리스트 : ',numbers)

for i in range(10) :
  if i not in numbers :
      print('숫자 {}는(은) 리스트에 없네요.'.format(i))
'''
#2번
'''
myList = [30, 10, 20]
print('현재 리스트 : %s' % myList)

myList.append(40)
print('append(40) 후의 리스트 : %s' % myList)

print('pop()으로 추출한 값 : %s' % myList.pop())
print('pop() 후의 값 : %s' % myList)

myList.sort()
print('sort() 후의 리스트 : %s' % myList)

print('20값의 위치: %d' % myList.index(20))

myList.insert(2, 222)
print('insert(2, 222) 후의 리스트 : %s' % myList)

myList.remove(222)
print('remove(222) 후의 리스트 : %s' %myList)

myList.extend([77, 88, 77])
print('extend([77, 88, 77]) 후의 리스트 : %s' % myList)

print('77값의 개수 : %d' % myList.count(77))
'''
#3번
'''
myList = [30, 10, 20]
newlist = sorted(myList)
print('sorted() 후의 myList : %s' % myList)
print('sorted() 후의 newlist : %s' % newlist)
'''
#4번
'''
import time

print('Time 20s test Press \'Enter\' Button')
i1 = input('Start')
s = time.time()
i2 = input('End')
e = time.time()

t = e - s
print('Press time diff : %3.2f'%(t))
print('Press 20s diff : %3.2f'%(20-t))
'''
#5번
'''
import random
import time

g_list = ['a', 's', 'd', 'f']

print('[타자게임] 준비되면 엔터!')
k = input()

cnt = 0
while True :
    cnt += 1
    print('* 문제 {}'.format(cnt))
    c = random.choice(g_list)
    print(c)
    while True :
        a = input(': ')
        if a == c :
            print('정답입니다.')
            g_list.remove(c)
            break
        else :
            continue
    if len(g_list) < 1 :
        break
print('수고하셨습니다.')
'''
#실습 part 2
#1번
'''
def pattern() :
    for i in range(1,6) :
        print('*' * i)
pattern()
pattern()
pattern()
'''
#2번
'''
def pattern(x) :
    for i in range(1,6) :
        print('{}'.format(x) * i)


pattern('K')
pattern('A')
pattern('B')
'''
#3번
'''
def pattern(x) :
    for i in range(6,1,-1) :
        print('{}'.format(x) * i)


pattern('O')
pattern('T')
'''
#4번
'''
def pattern1(x) :
    for i in range(1,6,1) :
        print('{}'.format(x) * i)
        
def pattern2(x) :
    for i in range(5,1,-1) :
        print('{}'.format(x) * i)

pattern1('X-mas')
pattern2('Merry')
'''
#실습 part 3
#1번
'''
import turtle as t

t.color('red')
t.circle(100)

t.color('red', 'yellow')
t.begin_fill()
t.circle(50)
t.end_fill()
'''
#2번
'''
import turtle as t

n = int(input())

for i in range(n) :
    t.forward(100)
    t.right(360/n)
'''
#3번
'''
import turtle as t

s = int(t.textinput('','몇각형을 원하시나요? :'))

for i in range(s) :
    t.forward(100)
    t.right(360/s)
'''
#4번
'''
import turtle as t
t.speed(0)

t.circle(100)
t.circle(75, steps = 5)
t.circle(50, steps = 4)
t.circle(25, steps = 3)
t.circle(150, 90)
t.circle(100, 90)
t.circle(50, 90)
t.circle(25, 90)
'''
#5번
'''
import turtle as t
t.speed(0)

t.dot()
t.forward(100)
t.dot(5, 'red')
t.dot(10, 'red')
t.forward(100)
t.dot(20)
'''
#6번
'''
import turtle as t

t.forward(100)
t.pensize(3)
t.forward(100)
t.left(90)
t.up()
t.forward(100)
t.pensize(5)
t.down()
t.right(90)
t.back(100)
'''
#7번
'''
import turtle as t
t.speed(0)

t.forward(100)
t.left(90)
t.backward(50)
t.right(45)
t.forward(75)

t.pencolor('red')
t.goto(100,-100)
t.setheading(0)
t.setx(0)
t.sety(100)
'''
#8번
'''
import turtle as t
t.speed(0)

angle = 10
for i in range (angle) :
    t.circle(60)
    t.left(360/10)

t.color('blue')

angle = 20
for i in range (angle):
    t.circle(10*i)
    t.left(360/angle)
'''
#9번
'''
import turtle as t
t.speed(0)

for i in range(250):
    t.forward(i)
    t.left(90)
'''
#10번
'''
import turtle as t
t.speed(0)

n = 5
for i in range(20) :
    t.forward(i*10)
    t.right(720/n)
'''
#11번
'''
import turtle as t
t.speed(0)

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t.bgcolor('black')
t.width(3)
length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5
'''
#12번
'''
import turtle as t
t.speed(0)

t.setup(500,500)
t.title('제목창에 글씨쓰기')
t.bgcolor('black')

for k in range(1000):
    if k % 3 == 0:
        t.color('red')
        t.forward(k * 0.5)
        t.left(117)
    if k % 3 == 1:
        t.color('blue')
        t.forward(k * 0.5)
        t.left(117)
    if k % 3 == 2:
        t.color('yellow')
        t.forward(k *0.5)
        t.left(117)
'''
#13번
'''
import random
import turtle as t
t.speed(0)

t.shape('turtle')

for x in range(500):
    a = random.randint(1, 360)
    t.setheading(a)
    b = random.randint(1, 20)
    t.forward(b)
'''
#14번
'''
import turtle as t
t.speed(0)

def sq(x, y) :
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(4) :
        t.forward(100)
        t.left(90)

sq(-100,0)
sq(100,0)
sq(300,0)
'''
#15번
'''
import turtle

def draw(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Time New Roman', 16, 'bold'))
    t.right(90)

    t.forward(40)
    t.right(90)
    t.foward(height)
    t.left(90)
    t.end_fill()

data = [120, 56, 309, 220, 156, 23, 98]
t = turtle.Turtle()
t.color('blue')
t.fillcolor('red')
t.pensize(3)
'''
