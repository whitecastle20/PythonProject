from tkinter import*
from PIL import ImageTk
from PIL import Image
from tkinter.ttk import Frame, Label, Scale, Style
from tkinter import Tk,BOTH, IntVar
from tkinter import messagebox
import random


root = Tk()
root.geometry("600x770+100+100")
root.title("주문화면")

logo = Image.open("Mclogo.png")
logo= logo.resize((610,850), Image.ANTIALIAS)
logoImage = ImageTk.PhotoImage( logo )
mcLogo = Button( image=logoImage, bd=0)
mcLogo.image = mcLogo
mcLogo.place(x=-10, y=-10)

mc_menu1 = {1:(u"선택하지 않음",0),2:(u"불고기 버거",4000),3:(u"치킨 버거",4500),4:(u"불닭 버거",5000)}
mc_menu2 = {1:(u"선택하지 않음",0),2:(u"상하이 치킨 스낵랩",2500),3:(u"제주 감귤 샐러드",3500),4:(u"와플 후라이",2000)}
mc_menu3 = {1:(u"선택하지 않음",0),2:(u"빅맥 세트",8500),3:(u"더블 불고기 버거 세트",7900),4:(u"슈슈 버거 세트",8000)}
mc_menu4 = {1:(u"선택하지 않음",0),2:(u"콜라",1300),3:(u"스프라이트",1300),4:(u"아메리카노",1000)}
mc_menu5 = {1:(u"선택하지 않음",0),2:(u"아이스크림",500),3:(u"오레오 맥플러리",3000),4:(u"딸기 선데이 아이스크림",1700)}

mc_menu = {u"단품 버거":mc_menu1, u"사이드메뉴":mc_menu2, u"세트메뉴":mc_menu3, u"음료":mc_menu4, u"디저트":mc_menu5}
final_selected ={1:(u"선택하지 않음",0),2:(u"선택하지 않음",0),3:(u"선택하지 않음",0),4:(u"선택하지 않음",0)}
menu_name = {1:u"단품 버거",2:u"사이드메뉴",3:u"세트메뉴",4:u"음료",5:u"디저트"}



class menu:

    def __init__(self, number):
        self.number=number
        self.this_menu_name=menu_name.get(number)
        self.var=IntVar()
        self.var.set(1)

    def selected(self):
        temp = mc_menu.get(self.this_menu_name).get(self.var.get())[0]
        menu_1.destroy()
        Label(root, text=u"선택된 메뉴 :                           ",background = "yellowgreen").place(x = 340, y=70+150*(self.number-1))
        Label(root, text=u"선택된 메뉴 : " + temp,background = "yellowgreen").place(x = 340, y=70+150*(self.number-1))
        global final_selected
        final_selected[self.number]=mc_menu.get(self.this_menu_name).get(self.var.get())

    def pop_menu(self):
        global menu_1
        menu_1=Toplevel(root)
        menu_1.title(self.this_menu_name)
        y=100*self.number +45
        menu_1.geometry("250x100+110+%d"% (y))
        for i in mc_menu.get(self.this_menu_name):
            Radiobutton(menu_1, text=mc_menu.get(self.this_menu_name).get(i)[0], variable=self.var, value=i, indicatoron=0, relief=RAISED, command=self.selected).pack(fill=X)
            



def make_menu(number):
    global this_menu
    this_menu = menu(number)
    this_menu.pop_menu()


def btn_exit():
    msgbox = messagebox.askquestion('확인', '주문을 취소하시겠습니까?')
    if msgbox == 'yes':
        exit()
        
def order():
    ordering = Toplevel(root)
    sum = 0
    global order_num
    order_num= random.randint(1,1000)
    for i in final_selected:
         sum += final_selected[i][1]
    for i in menu_name:
        Label(ordering, text =menu_name.get(i) + ':').grid(row=i,column=1)
        Label(ordering, text =final_selected.get(i)[0]).grid(row=i,column=3)
        Label(ordering, text =final_selected.get(i)[1]).grid(row=i,column=5)
        Label(ordering, text = u"주문번호 ", font = ("Helvetica", 25)).grid(row=8,column=3)
        Label(ordering, text = str(order_num), font =("Helvetica", 25) ).grid(row=9,column=3)
        Label(ordering, text =u"계산하실 금액은 " + str(sum) + u"원 입니다.").grid(row=7,column=3)

    Label(ordering,text ="이용해주셔서 감사합니다",background = "pink").grid(row=10,column=3)

mymenu = menu(root)
Button(root, text = u"단품 버거", command=lambda: make_menu(1)).place(x = 10, y = 70)
Button(root, text = u"사이드메뉴", command=lambda: make_menu(2)).place(x = 10, y = 230)
Button(root, text = u"세트메뉴", command=lambda: make_menu(3)).place(x = 10, y = 390)
Button(root, text = u"음료", command=lambda: make_menu(4)).place(x = 10, y = 540)
Button(root, text = u"디저트", command=lambda: make_menu(5)).place(x = 10, y = 700)
Button(root, text = u"주문취소", command=lambda: btn_exit()).place(x = 300, y = 740)
Button(root, text = u"주문완료", command=order).place(x = 460, y = 740)




images = [(1,"burger.jpg"),(2,"side_menu.jpg"),(3,"set_menu.jpg"),(4,"beverage.jpg"),(5,"dessert.jpg")]
for i, image in images:
    img = Image.open(image)
    img= img.resize((130,120),Image.ANTIALIAS)
    this_image = ImageTk.PhotoImage( img )
    mylabel = Label( image=this_image)
    mylabel.image = this_image
    mylabel.place(x=100, y=10+(i-1)*157)
    
root.config(width=600, height=800)

root.mainloop()
 
