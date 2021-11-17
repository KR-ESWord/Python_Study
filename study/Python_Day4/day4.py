#실습 part1
#1
'''
def reverse(x,y,z):
    return z,y,x

ret=reverse(1,2,3)
print(ret)

r1,r2,r3 = reverse('a','b','c')

print(r1,r2,r3)
'''
#2
'''
def calc(x,y,z):
    print(x)
    print(y)
    print(z)
    return x+y+z

print(calc(y=20,x=10,z=30))
'''
#3
'''
def calc_area():
    result = 3.14*r**2
    return result

r = float(input('r : '))
area = calc_area()
print(area)
'''
#4
'''
def greet(name, msg='별일없죠?'):
    print('안녕',name+','+msg)
greet('영희')
'''
#5
'''
def pf(*para) :
    result = 0
    for num in para :
        result = result + num

    return result
hap = 0

hap = pf(10,20)
print('2 : %d' % hap)
hap = pf(10,20,30)
print('3 : %d' % hap)
'''
#6
'''
def pf(v1,v2,v3=0):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0
hap = pf(10, 20)
print('2 : %d' % hap)
hap = pf(10, 20, 30)
print('3 : %d' % hap)
'''
#7
'''
mt =(10,20,30)
ml = list(mt)
ml.append(40)
mt = tuple(ml)
print(mt)
'''
#8
'''
def mart(*r_t) :
    return r_t

nr_t = mart('coke', 'chocolate', 'watemelon', 'beer')

if 'coke' in nr_t :
    r_l = list(nr_t)
    r_l.remove('coke')
    r_l.insert(0, 'sprite')
    nr_t = tuple(r_l)

print('음식 리스트 : ', nr_t)
print('음식의 수 : %d' % len(nr_t))
'''
#9
'''
import random

def play(*c_t):
    return c_t

def win():
    print('User : {}'.format(choice[u]), ' vs ', 'AI : {}'.format(choice[c]))
    print('Win')

def lose():
    print('User : {}'.format(choice[u]), ' vs ', 'AI : {}'.format(choice[c]))
    print('Lose')


def draw():
    print('User : {}'.format(choice[u]), ' vs ', 'AI : {}'.format(choice[c]))
    print('Draw')

choice = play('Rock', 'Scissor', 'Paper')

u_cnt = 0
c_cnt = 0

while True :
    u = int(input('Rock(0), Scissor(1), Paper(2) : '))
    c = random.randint(0, 2)
    
    if choice[u] == choice[c] :
        draw()

    elif choice[u] == 'Rock' :
        if choice[c] == 'Scissor' :
            win()
            u_cnt += 1
        elif choice[c] == 'Paper' :
            lose()
            c_cnt += 1
        
    elif choice[u] == 'Scissor' :
        if choice[c] == 'Rock' :
            lose()
            c_cnt += 1
        elif choice[c] == 'Paper' :
            win()
            u_cnt += 1
            
    elif choice[u] == 'Paper' :
        if choice[c] == 'Rock' :
            win()
            u_cnt += 1
        elif choice[c] == 'Scissor' :
            lose()
            c_cnt += 1

    if u_cnt == 3 or c_cnt == 3 :
        break
    
if u_cnt == 3 :
        print('User Win')
elif c_cnt == 3 :
        print('AI Win')
'''
'''
import random

def play(*c_t):
    return c_t

def win():
    if (u == 0 and c == 1) or (u == 1 and c == 2) or (u == 2 and c == 0) :
        print('User : {}'.format(choice[u]), ' vs ', 'AI : {}'.format(choice[c]))
        print('Win')
        global u_cnt
        u_cnt += 1

def lose():
    if (u == 0 and c == 2) or (u ==1 and c == 0) or (u == 2 and c ==1) :
        print('User : {}'.format(choice[u]), ' vs ', 'AI : {}'.format(choice[c]))
        print('Lose')
        global c_cnt
        c_cnt += 1

def draw():
    if u == c :
        print('User : {}'.format(choice[u]), ' vs ', 'AI : {}'.format(choice[c]))
        print('Draw')

choice = play('Rock', 'Scissor', 'Paper')

u_cnt = 0
c_cnt = 0

while True :
    try :
        u = int(input('Rock(0), Scissor(1), Paper(2) : '))
        c = random.randint(0, 2)
        if u >= 0 and u < 3 :
            draw()
            win()
            lose()
        else :
            print('0~2의 숫자만 눌러주세요.')
            continue
    except :
        print('0~2의 숫자만 눌러주세요.')
        continue

    if u_cnt == 3 or c_cnt == 3 :
        break
    
if u_cnt == 3 :
        print('User Win')
elif c_cnt == 3 :
        print('AI Win')
'''
#calc
'''
def input_calc() :
    global n1
    global n2
    global cc
    n1 = int(input('첫 번째 정수를 입력하세요 : '))
    n2 = int(input('두 번째 정수를 입력하세요 : '))
    cc = input('기호를 입력하세요(+, -, *, /, all, who, end) : ')

def add(n1, n2) :
        print('Addtion result : %d' % (n1 + n2))

def sub(n1, n2) :
        print('Subtraction result : %d' % (n1 - n2))

def mul(n1, n2) :
        print('Multiplication result : %d' % (n1 * n2))

def div(n1, n2) :
    if n2 == 0 :
        print('Error')
    else :
        print('Division result : %3.2f' % (n1/n2))

def all_in(n1, n2) :
    add(n1,n2)
    sub(n1,n2)
    mul(n1,n2)
    div(n1,n2)

def who() :
        print('-'*25)
        print('빅데이터, 공돌이, 문동규')
        print('-'*25)

def calc() :
    while True :
        input_calc()
        
        if cc == '+' :
            add(n1,n2)
            
        elif cc == '-' :
            sub(n1,n2)
            
        elif cc == '*' :
            mul(n1,n2)
            
        elif cc == '/' :
            div(n1,n2)
            
        elif cc == 'all' :
            all_in(n1,n2)
            
        elif cc == 'who' :
            who()
            
        elif cc == 'end' :
            break

calc()
'''
#dragon

import time
import random

def start():
    a = True
    while a :
        openning()
        selc()
        draw()
        a = ending()
        
def openning() :
    print('당신은 공룡이 살고 있는 지역에 들어와 있습니다.'); time.sleep(1)
    print('당신 앞에 두개의 동굴이 보이는 군요. 한쪽 동굴은 친절한 공룡이 살고 있어서'); time.sleep(1)
    print('당신에게 보물을 나눠줄 것입니다. 다른 쪽 동굴의 공룡은'); time.sleep(1)
    print('무섭고, 배가고픈 공룡이여서 당신을 한 입에 먹어 버릴 것입니다.\n'); time.sleep(1)

def selc() :
    print('어떤 동굴로 들어 가시겠습니까? (1 or 2)')
    s = input(':: ')
    if int(s) == 1 or int(s) == 2 :
        print('당신은 동굴로 들어가고 있습니다.'); time.sleep(1)
        print('동굴은 어둡고 으스스합니다.'); time.sleep(1)
        print('커다란 공룡이 당신 앞으로 달려 나와 입을 쩍~~~~~~~\n')
    else :
        selc()

def draw() :
    e = random.randint(1,2)
    
    if e == 1 :
        print('''
      XAAAAAAAAAAAA                   ㅜㅡㅡㅡㅡㅡㄱ           HHHHHHHHHHHHHH
       XAAAAAAAAAAAA      ㄱㅡㅡㅡㅡㅡㅗ    ㅇ     I          HHHHHHHH
        XAAAAAAAAAAAA     I                        I        HHHHHHHHHHHHHHH
       XAAAAAAAAAAAAAA    ㄴAAAAAAAAAl             I      HHHHHHHHHH
      XAAAAAAAAAAAAAAAA             l              I       HHHHHHHHHHHHH
       XVVVVVVVVVVVVVVV   PVVVVVVVVVV              I        HHHHHHHH
    XVVVVVVVVVVVVVVVVV    I                        I         HHHH
      XVVVVVVVVVVVVVV     LㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡJㅡㅡㅡㅡㅡHHㅡㅡㅡㅡㅡㅡㅡ
        XVVVVVVVVVVV     
      XVVVVVVVVVVVV      
        ''')
        print('그 큰 입으로 당신을 꿀꺽! 쩝쩝! 잡아먹었습니다 ㅠㅠ')
        time.sleep(1)
        
    elif e == 2 :
        print('''
                                       PㅡㅡㅡㅡT            HHHH
                                      I     ^   I          HHHHHHHH
                                      L    ^ ^  I        HHHHHHHHHHHH
       WWWWWWWW        Kㅡㅡㅡㅡㅡㅡㅡㅓ  ^   ^ I       HHHHHHHHHHHHHHH
      WWWWWWWWWW       I                        I      HHHHHHHHHHHHHHHHHH
     WWWWWWWWWWWW      ㄴㅡㅡㅡㅡㅡㅡㅓ         I     HHHHHHHHHHHHHHHHHHHH
      WWWWWWWWWW                     J          I       HHHHHHHHHHHH
       WWWWWWWW        PㅡㅡㅡㅡㅡㅡJ           I        HHHHHHHH
        WWWWWW         I                        I         HHHH
         WWWW          LㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡJㅡㅡㅡㅡㅡHHㅡㅡㅡㅡㅡㅡㅡㅡ
        ''')
        print('그 큰 입에서 보물을 꺼내어 당신에게 선물로 줍니다 ^^')
        time.sleep(1)

def ending() :
    print('게임을 다시 하시겠습니까?(yes or no)')
    t = input(':: ')
    if t == 'y' or t == 'yes' or t =='Yes' or t == 'YES' :
        return True
    elif t == 'n' or t == 'no' or t == 'No' or t == 'NO' :
        print('게임이 종료되었습니다.')
        return False
    else :
        print('올바른 명령어를 입력하여 주십시오.')
        return ending()

#==================
start()

