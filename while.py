Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> treeHit=0
>>> while treeHit < 10:
	treeHit = treeHit + 1
	print("나무를 %d번 찍었습니다." %treeHit)
	if treeHit == 10:
		print("나무 넘어갑니다.")

		
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.
>>> prompt = """
1.Add
2.Del
3.List
4.Quit

Enter number:"""
>>> number = 0
>>> while number != 4:
	print(prompt)
	number = int(input())

	

1.Add
2.Del
3.List
4.Quit

Enter number:
1

1.Add
2.Del
3.List
4.Quit

Enter number:
4
>>> coffee = 10
>>> money = 300
>>> while money:
	print("돈을 받았으니 커피를 줍니다.")
	coffee = coffee - 1
	print("남은 커피의 양은 %d개 입니다." %coffee)
	if not coffee:
		print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
		break

	
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 9개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 8개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 7개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 6개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 5개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 4개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 3개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 2개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 1개 입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 0개 입니다.
커피가 다 떨어졌습니다. 판매를 중지합니다.
>>> 
