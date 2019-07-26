#myGlossary_Start.py

from tkinter import*

#키 입력 함수 :
def click():
    entered_text = entry.get()
    output.delete(0.0, END) #지움
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "단어의 정의를 찾을 수 없습니다."
    output.insert(END, definition)
    

##### 메인:
window = Tk() #설명필요
window.title("My Coding Club Glossary")

#레이블 생성
Label(window,text="정의되어있는 단어를 입력하고 엔터키를 누르세요:").grid(row=0,column=0,sticky=W)\

#텍스트 엔트리 위젯 생성
entry = Entry(window, width=20, bg="light green")
entry.grid(row=1, column=0, sticky=W)
           
#제출버튼 추가
Button(window, text="제출",width=5, command=click).grid(row=2,column=0,sticky=W)
#다른 레이블 생성
Label(window, text="\n정의:").grid(row=3, column=0,sticky=W)
#텍스트 박스 생성
output = Text(window, width=75, height=6, wrap=WORD, bg="light green")
output.grid(row=4, column=0, columnspan=2,sticky=W)

#사전
my_glossary = {
    '알고리즘':'컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해 놓은 것'
    
    }

#### 메인 반복문 실행
window.mainloop()

print(my_glossary["함수"])
