'''
#1
dic1 = {1:'a', 2:'b',3:'c'}
print(dic1)
student1 ={'학번':1000,'이름':'홍길동','학과':'컴퓨터학과'}
print(student1)
student1['연락처'] = '010-1111-2222'
print(student1)

#2
print(student1['학번'])
print(student1['이름'])
print(student1['학과'])

#3
student1['학과'] = '파이썬학과'
print(student1)
del(student1['학과'])
print(student1)
student1 ={'학번':2000,'이름':'홍길동','학과':'파이썬학과'}
print(student1)
'''
'''
#4,7
phone_book = {'홍길동' : '010-1234-5678', '강감찬':'010-1234-5679','이순신':'010-1234-5680'}

print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

for key in sorted(phone_book.keys()) :
    print(key, phone_book[key])
'''
'''
#5
if '이름' in student1 :
    print('TRUE')
else :
    print('FALSE')
    
if '주소' in student1 :
    print('TRUE')
else :
    print('FALSE')
'''
'''
#6
dic1 = {'one':'하나','two':'둘','three':'셋','a':'test'}

for key in sorted(dic1.keys()) :
    print(key,dic1[key])
    
while True :
    a = input('단어를 입력하시오 : ')
    print(dic1[a])
'''
'''
#7
def 걸그룹(**para) :
    for k in para.keys() :
        print('%s --> %d명입니다.' % (k, para[k]))
        
걸그룹(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)
'''
'''
#8
foods = ['떢볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sides = ['오뎅', '단무지', '김치']
tupList = list(zip(foods, sides))
dic = dict(zip(foods, sides))
print(tupList)
print(dic)
'''
'''
#9
oldList = ['짜장면', '탕수육', '군만두']
newList = oldList
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)

oldList = ['짜장면', '탕수육', '군만두']
newList = oldList[:]
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)
'''
'''
#1
ml = [1,2,3,4,5]
def add10(num) :
    return num +10

for i in range(len(ml)):
    ml[i] = add10(ml[i])
print(ml)

ml = [1,2,3,4,5]
add10 = lambda num : num +10
ml = list(map(add10,ml))
print(ml)
'''
'''
#2
ml =[1,2,3,4,5]
ml = list(map(lambda num : num+10,ml))
print(ml)

list1 =[1,2,3,4]
list2 =[10,20,30,40]
hap = list(map(lambda n1,n2:n1+n2,list1,list2))
print(hap)
'''
'''
#3
def s2(x) :
    return x**2
print(s2(5))

s1=lambda x: x**2
print(s1(5))

def add(x,y):
    return x+y
print(add(10,20))

add2 = lambda x,y : x+y
print(add2(10,20))
'''
'''
#4
def hap(num1,num2) :
    res = num1+num2
    return res
print(hap(10,20))

hap2 = lambda num1,num2:num1+num2
print(hap(10,20))

hap3 = lambda num1 = 10, num2 = 20:num1+num2
print(hap3())
print(hap3(100,200))
'''
'''
#1
def start():
    while True :
        s_mode = input('mode입력(e(encrypt) or d(decrypt) or s(stop) : ')
        if s_mode == 'e':
            print('암호화를 시작합니다.')
            print('암호화 결과 : ', encrypt())
            
        elif s_mode == 'd':
            print('복호화를 시작합니다.')
            print('복호화 결과 : ', decrypt())

        elif s_mode == 's':
            print('프로그램이 종료되었습니다.')
            break

        else :
            print('mode입력을 잘 못하셨습니다.')

def encrypt():
    answer = ''
    m = input('message 입력 : ')
    k = int(input('key 입력 : '))

    for i in m :
        if 65 + ((ord(i) + 7) % 26) + k > 90 :
            answer += chr(65 + ((ord(i) + 7)%26)+ k - 26)
        else :
            answer += chr(65 + ((ord(i) + 7)%26)+ k)
    return answer


def decrypt():
    answer = ''
    m = input('message 입력 : ')
    k = int(input('key 입력 : '))
    for i in m :
        if (97 + (ord(i) +13) % 26 - k) < 97 :
            answer += chr(97 + ((ord(i) + 13)%26) - k + 26)
        else :
            answer += chr(97 + ((ord(i) + 13)%26) - k)
    return answer

start()
'''
'''
#입력 받을 리스트 내용
low = 'abcdefghijklmnopqrstuvwxyz'
high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
emo1 = ' !"#$%&\'()*+,-./'
emo2 = '0123456789:;<=>?'
answer = ''

#start함수
def start():
    while True :
        s_mode = input('mode입력(e(encrypt) or d(decrypt) or s(stop) : ')
        if s_mode == 'e':
            print('암호화를 시작합니다.')
            encrypt(answer)
            
        elif s_mode == 'd':
            print('복호화를 시작합니다.')
            decrypt(answer)

        elif s_mode == 's':
            print('프로그램이 종료되었습니다.')
            break

        else :
            print('mode입력을 잘 못하셨습니다.')

#암호화 함수
def encrypt(answer) :
    m = input('message 입력 : ')
    k = int(input('key 입력 : '))
    for i in m :
        #message의 값 i가 입력된 경우의 수로 진행
        #i의 값을 경우의 수의 리스트의 인덱스(수) 값에
        #key값을 더한 후 26의 나머지의 값을
        #암호화할 리스트의 인덱스 값(문자)을 answer에 대입
        if low.count(i) != 0 :
            answer += high[(low.find(i) + k) % 26]
        if high.count(i) != 0 :
            answer += low[(high.find(i) + k) % 26]
        if emo1.count(i) != 0 :
            answer += emo2[(emo1.find(i) + k) % 16]
        if emo2.count(i) != 0 :
            answer += emo1[(emo2.find(i) + k) % 26]
    print('암호화 결과 : ', answer)

def decrypt(answer) :
    m = input('message 입력 : ')
    k = int(input('key 입력 : '))        
    for i in m :
        #message의 값 i가 입력된 경우의 수로 진행
        #i의 값을 경우의 수의 리스트의 인덱스(수) 값에
        #key값을 더한 후 26의 나머지의 값을
        #암호화할 리스트의 인덱스 값(문자)을 answer에 대입
        if low.count(i) != 0 :
            answer += high[(low.find(i) - k) % 26]
        if high.count(i) != 0 :
            answer += low[(high.find(i) - k) % 26]
        if emo1.count(i) != 0 :
            answer += emo2[(emo1.find(i) - k) % 16]
        if emo2.count(i) != 0 :
            answer += emo1[(emo2.find(i) - k) % 16]
    print('암호화 결과 : ', answer)

start()
'''

#파일 입출력
'''
#1
infile = open('c:\\test\\test.txt','r')
lines = infile.read()
print(lines)

lines = infile.readlines()
print(lines)
'''
'''
#2
infile = open('c:\\test\\test.txt','r')
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()
'''

#3번
'''
outfile = open('c:\\test\\test.txt','w')
outfile.write('홍 010-1234-5678\n')
outfile.write('철 010-1234-5679\n')
outfile.write('희 010-1234-5680\n')
outfile.close()

outfile = open('c:\\test\\test.txt','a')
outfile.write('강 010-1234-5681\n')
outfile.write('유 010-1234-5682\n')
outfile.write('용 010-1234-5683\n')
outfile.close()
'''
'''
#4번
with open('c:\\test\\test.txt','r') as inFp :
    inList = inFp.readlines()
    print(inList)
'''
'''
#5번
outFp = None
outStr = ''
outFp = open('c:\\test\\test.txt','w')

while True :
    outStr = input('내용 입력 : ')
    if outStr != '' :
        outFp.writelines(outStr + '\n')
    else :
        break

outFp.close()
print('-----정상적으로 파일에 씀-----')
'''
'''
#6번
infile = open('c:\\test\\test.txt','r')
for line in infile :
    line = line.rstrip()
    word_list = line.split()
    for word in word_list :
        print(word)
infile.close()
'''
'''
#7번
inFp = None
inStr = ''

inFp = open('c:\\test\\test.txt','r')

inStr = inFp.readline()
print(inStr, end = '')

inStr = inFp.readline()
print(inStr, end = '')

inStr = inFp.readline()
print(inStr, end = '')

inFp.close()
'''
'''
#8번
inFp = None
inStr = ''

inFp = open('c:\\test\\test.txt','r')

inList = inFp.readlines()
print(inList)
inFp.close()
'''
'''
#9번
import shutil
shutil.copy('c:\\test\\test.txt', 'c:\\test\\test2.txt')
'''
'''
#10번
import os.path
os.path.exists('c:\\test\\test2.txt')
os.path.isfile('c:\\test\\test2.txt')
os.path.isdir('c:\\test')
'''
'''
#11번
import os
os.remove('c:\\test\\test2.txt')
os.remove('c:\\test\\test2.txt')
'''
'''
#12번
#입력 파일 이름과 출력 파일 이름을 받는

import shutil
shutil.copy('c:\\test\\name.txt', 'c:\\test\\test.txt')

infilename = input('입력 파일 이름 : ')
outfilename = input('출력 파일 이름 : ')

#입력과 출력을 위한 파일을 연다.
infile = open(infilename, 'r')
outfile = open(outfilename, 'w')

#전체 파일을 읽는다.
s = infile.read()

#전체 파일을 쓴다.
outfil.write(s)

#파일을 닫는다.
infile.close()
outfile.close()
'''
'''
#13번
import os

inFp = None
fname, inList, inStr = '', [], ''

fName = input('파일명을 입력하세요 : ')

if os.path.exists(fName) :
    inFp = open(fName, 'r')

    inList = inFp.readlines()
    for inStr in inList :
        print(inStr, end = '')

    inFp.close()
else :
    print('%s 파일이 없습니다.' % fName)

'''
'''
#14번
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if(readFile != None):
    infile = open(readFile, 'r')
    
for line in infile.readlines():
    line = line.strip()
    print(line)
infile.close()
'''
'''
#15번
num1 = input('숫자1 --> ')
num2 = input('숫자2 --> ')

try :
    num1 = int(num1)
    num2 = int(num2)

except :
    print('오류가 발생했습니다.')

else :
    print(num1, '/', num2, '=', num1/num2)
finally :
    print('must')
'''
'''
#16번
#입력 받은 파일
infilename = input('파일 이름을 입력하세요 : ')

#파일 열기
with open(infilename, 'r') as inFp

'''


