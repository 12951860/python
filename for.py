Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_list = ['one','two','three']
>>> for i in test_list:
	print(i)

	
one
two
three
>>> a = [(1,2),(3,4),(5,6)]
>>> for (first,last) in a:
	print(first+last)

	
3
7
11
>>> marks = [90,25,67,45,80]
>>> #marks1.py
>>> number = 0
>>> for mark in marks:
	number = number + 1
	if mark >= 60:
		print("%d번 학생은 합격입니다." %number)

		
1번 학생은 합격입니다.
3번 학생은 합격입니다.
5번 학생은 합격입니다.
>>> for mark in marks:
	number = number + 1
	if mark >= 60:
		print("%d번 학생은 합격입니다." %number)
		else:
			
SyntaxError: invalid syntax
>>> for mark in marks:
	number = number + 1
	if mark >= 60:
		print("%d번 학생은 합격입니다." %number)
	else:
		print(%d번 학생은 불합격입니다." %number)
		      
SyntaxError: invalid syntax
>>> for mark in marks:
	number = number + 1
	if mark >= 60:
		print("%d번 학생은 합격입니다." %number)
	else:
		print("%d번 학생은 불합격입니다." %number)

		      
6번 학생은 합격입니다.
7번 학생은 불합격입니다.
8번 학생은 합격입니다.
9번 학생은 불합격입니다.
10번 학생은 합격입니다.
>>> #marks2.py
		      
>>> marks = [90,25,67,45,80]
		      
>>> number = 0
		      
>>> for mark in marks:
		      number = number + 1
		      if mark < 60:continue
		      print("%d번 학생 축하합니다. 합격입니다."%number)

		      
1번 학생 축하합니다. 합격입니다.
3번 학생 축하합니다. 합격입니다.
5번 학생 축하합니다. 합격입니다.
>>> a = range(10)
		      
>>> a
		      
range(0, 10)
>>> a = range(1,11)
		      
>>> a
		      
range(1, 11)
>>> sum = 0
		      
>>> for i in range(1,11):
		      sum = sum + i

		      
>>> print(sum)
		      
55
>>> 
