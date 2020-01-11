#1
#실습1
'''
number1 = 26
number2 = 31
sum = number1 + number2
print(sum)
'''
#실습2
'''
length = 9
width = 6
print('area = ',length * width)
'''
#실습3
'''
string1 = 'Hello,'
string2 = 'Python'
star = '***'
print(star * 3 + string1 + string2 + star * 3)
'''
#실습4
'''
print('What is your name?')
name = input()
print('Your name is ' + name)

name = input('What is your name?')
print('Your name is ' + name)
'''
#실습5
'''
guess = '23'
guess = int(guess)
print(guess * 2)

guess = 5
guess = str(guess)
print(guess * 2)
'''
#실습6
'''
#This is a guess the number game.
import random

print('Hello! What is your name?')
myName = input()

print('Well, ' + myName + ', I am thingking of a number between 1 and 20.')
print('Take a guess')

number = random.randint(1, 21)

answer = True
count = 0

while answer:
    guess = int(input())
    count = count + 1

    if guess < number :
        print('Your guess is too low' + '\n' + 'That is wrong.')
    elif guess > number :
        print('Your guess is too high' + '\n' + 'That is wrong.')
    else :
        print('Good job, ' + myName + '! You guessed my number!')
        print('Your try count is', count)
        answer = False
    if count > 5 :
        print('Your try count over. try later.')
        answer = False

    
if guess != number :
    print('Your guess is wrong.')
if guess == number :
    print('Good job, ' + myName + '! You guessed my number!')
'''
#실습7
'''
print('Input the first number A : ')
A = int(input())
print('Input the second number B : ')
B = int(input())
print('A is ', A, 'and B is ', B)
print('A + B = ', A + B)
'''
#실습8
'''
a = int(input('첫 번째 숫자를 입력하세요 : '))
b = int(input('두 번쨰 숫자를 입력하세요 : '))
print('첫 번째', a, '두 번째', b)
'''
#실습9
'''
a = int(input('첫 번째 숫자를 입력하세요 : '))
b = int(input('두 번째 숫자를 입력하세요 : '))
if a > b :
    print('큰 수는', a)
elif a < b :
    print('큰 수는', b)
else :
    print('두 수는 같다.')
'''
#실습10
'''
blood = input('당신의 혈액형은 A/B/O/AB ? ')
if blood == 'A' or blood == 'a' :
    print('당신은 호수처럼 맑은 성격을 소유하고 있습니다.')
elif blood == 'B' or blood == 'b' :
    print('당신은 모든일에 뜨거운 열정을 쏟는 사람입니다.')
elif blood == 'O' or blood == 'o' :
    print('당신은 매사 밝고 쾌활한 성격의 사람입니다.')
elif blood == 'AB' or blood == 'ab' :
    print('당신은 창의적인 사고를 하는 사람입니다.')
else :
    print('존재하지 않는 혈액형입니다.')
'''
#실습11
'''
score = int(input('점수를 입력하세요 : '))
if score >= 90 :
    print('*' * 30 + '\n' + '축하합니다!')
    print('당신은 창의적 컴퓨팅 과목 시험에 합격하셨습니다.' + '\n' + '*' * 30)
else :
    print('불합격입니다.' + '\n' + '다시 한번 시도하도록 합니다.')
'''
#프로젝트1
'''
print('-' * 28)
print('***   스위스 국제 금융   ***')
print('-' * 28)

name = input('Please enter your name     : ')
word = input('Please enter your password : ')

if name == 'moon' and word == '2019hyu' :
    print('Your password ' + word + ' is correct')
    print(name + ' Welcome to Swiss International Bank!!!')
    email = input('Please enter your e-mail address : ')
    print(' The secure number has been sending to ' + email)
else :
    if name != 'moon' and word != '2019hyu':
        print('Your name ' + name + ' and ' + 'password ' + word + ' is NOT correct')
        print('Your account is locked, sorry!')
    elif name != 'moon' :
        print('The name ' + name + ' is NOT correct')
        print('Your account is locked, sorry!')
    elif word != '2019hyu' :
        print('The password ' + word + '  is NOT correct')
        print('Your account is locked, sorry!')
'''
#실습1
'''
a = '★'

number = 1
print('-' * 18)
while number <= 10 :
    print(a * number)
    number = number + 1
print('-' * 18)
'''
#실습2
'''
cnt = 1
while cnt <= 10 :
    print('*')
    cnt = cnt + 1
'''
#실습3
'''
number = 1
while number <= 10 :
    print(number)
    number = number + 1
'''
#실습4
'''
number = 10
while number >= 1 :
    print(number)
    number = number - 1
'''
#실습5
'''
number = 1
while number <= 10 :
    if number % 2 == 0 :
        print(number)
    number = number + 1
'''
#실습6
'''
cnt = 1
while cnt <= 10 :
    print('파이썬은', cnt, '번 재미 있습니다.')
    cnt = cnt + 1
'''
#실습7
'''
cnt = 0
csum = 0
while cnt < 10 :
    cnt = cnt + 1
    csum = csum + cnt
    print('step', cnt, '=>', csum)
'''
#실습8

while True :
    a = int(input('첫 번째 숫자를 입력하세요 : '))
    b = int(input('두 번째 숫자를 입력하세요 : '))
    if a > b :
        print('큰 수는 ', a)
    elif a < b :
        print('큰 수는 ', b)
    else :
        print('두 수는 같다.')
