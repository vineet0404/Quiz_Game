from tkinter import *

question = {
    "Current Prime Minster of India": ['Rahul Gandhi', 'Vineet Singh', 'Narendra Modi', 'Sachin Pilate'],
    "Which Captian Have all three ICC world cup": ['Ricky Point', 'Sachin Tendulkar', 'Virat kohli','MS Dhoni'],
    "how many Century have been hit by Schin in International Crciket": ['100','75','51','49'],
    "World Best finisher?":['Hardik Pandya','Virat','Kurnal','MSD'],
    "In which India win first world cup":['1885','1884','1983','1999'],
    "how many year later india win ICC World Cup":['25','24','23','28'],
    "In which year India win First world hockey Cup:":['1975','1985','1977','1976']
}
ans = ['Narendra Modi', 'MS Dhoni', '100','MSD','1983','28','1975']
checkquetion=[]
checkoption=[]
checkans=[]

current_question = 0

def start_quiz():
    start_button.forget()
    next_button.pack()
    next_question()

def next_question():
    global current_question
    if current_question < len(question):
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        clear_frame()
        Label(f1, text=f"Question : {c_question}", padx=15,
              font="calibre 25 normal").pack(anchor=NW)
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option,font="25", padx=28).pack(anchor=NW)
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(f1, text=output, font="calibre 25 bold").pack()
        Label(f1, text="Thanks for Participating",font="calibre 23 bold").pack()

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question - 1]:
        user_score.set(user_score.get() + 1)
    elif temp_ans == 'None' and temp_ans != ans[current_question - 1]:
        checkoption.append(ans[current_question])
        print(checkquetion)
        print(checkoption)

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()


root = Tk()
root.title("QUIZ Game")
root.geometry("850x520")

user_ans = StringVar()
user_ans.set('None')
user_score = IntVar()
user_score.set(0)

Label(root, text="Quiz App",font="calibre 40 bold",fg="white",relief=SUNKEN, background="green",padx=10, pady=9).pack()
Label(root, text="", font="calibre 20 bold").pack()
start_button = Button(root,text="Start Quiz",command=start_quiz,font="calibre 30 bold",bg="red",fg="white")
start_button.pack()

f1 = Frame(root)
f1.pack(side=TOP, fill=X)


next_button = Button(root, text="Next Question",command=next_question,font="calibre 17 bold")

frame2=Frame(root)
frame2.pack()
root.mainloop()