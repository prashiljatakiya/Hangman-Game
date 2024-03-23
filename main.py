import random
from tkinter import *
from tkinter import messagebox
score=0
New_Game = True

# main loop
while New_Game:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG_MAN')
    root.resizable(width=False,height=False)
    img=PhotoImage(file="Your_img10.png")
    
    BG=Label(root,image=img)
    BG.place(x=0,y=0,relwidth=1,relheight=1)
    messagebox.showinfo("Welcome","Lets play hangman game!!")

    no_of_guesses = 0
    win_count = 0

     # choosing word from a given list of words
    
    words=['alligator','alpaca','anaconda','ant','antelope','ape','baboon','eagle','bat','bear','bee','beetle','bird','bison','whale','spider','cat','buffalo','butterfly','camel','catfish','chicken','cobra','chimpanzee','crab','crane','crow','crocodile','deer','dog','dinosaur','dolphin','dove','duck','donkey','elephant','falcon','fish','flamingo','fox','frog','goat','goose','gorilla','grasshopper','hamster','hare','hawk','hippopotamus','horse','husky','kangaroo','ladybug','lion','lizard','llama','alpaca','moose','mosquito','mongoose','moth','octopus','ostrich','otter','oyster','panda','peacock','pig','pigeon','porcupine','quail','rabbit','raccoon','rat','sheep','rooster','zebra','tiger','whale',’india’,’australia’,’africa’,’europe’,’argentina’,’china’,’russia’,’korea’,’red’,’green’,’pink’,’blue’,’black’,’yellow’,’ruby’,’pearl’,’diamond’,’sapphire’,’rose’,’jasmine’,’sunflower’,’lilly’,’tulip’,’apple’,’mango’,’banana’,’onion’,’tomato’,'wolf']
    selected_word = random.choice(words)
    l=len(selected_word)

    # creation of dashes corresponding to the word chosen including variables
    
    x = 250
    for i in range(0,l):
        x += 60
        exec('d{}=Label(root,text="_",bg="#005536",font=("Comic Sans MS",40),fg="white")'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))

   #Button images
    a=PhotoImage(file="a.png")
    b=PhotoImage(file="b.png")
    c=PhotoImage(file="c.png")
    d=PhotoImage(file="d.png")
    e=PhotoImage(file="e.png")
    f=PhotoImage(file="f.png")
    g=PhotoImage(file="g.png")
    h=PhotoImage(file="h.png")
    i=PhotoImage(file="i.png")
    j=PhotoImage(file="j.png")
    k=PhotoImage(file="k.png")
    l=PhotoImage(file="l.png")
    m=PhotoImage(file="m.png")
    n=PhotoImage(file="n.png")
    o=PhotoImage(file="o.png")
    p=PhotoImage(file="p.png")
    q=PhotoImage(file="q.png")
    r=PhotoImage(file="r.png")
    s=PhotoImage(file="s.png")
    t=PhotoImage(file="t.png")
    u=PhotoImage(file="u.png")
    v=PhotoImage(file="v.png")
    w=PhotoImage(file="w.png")
    x=PhotoImage(file="x.png")
    y=PhotoImage(file="y.png")
    z=PhotoImage(file="z.png")
        

    #Hangman images
    
    
    abc=PhotoImage(file="abc.png")
    abr=PhotoImage(file="abr.png")
    acr=PhotoImage(file="acr.png")
    adr=PhotoImage(file="adr.png")
    aer=PhotoImage(file="aer.png")
    afr=PhotoImage(file="afr.png")
    agr=PhotoImage(file="agr.png")
    
    
    #Placing the buttons
    
    b1=Button(root,bd=0,command=lambda:check("a","b1"),bg="#005536",activebackground="#005536",font=10,image=a)
    b1.place(x=0,y=595)
    b2=Button(root,bd=0,command=lambda:check("b","b2"),bg="#005536",activebackground="#005536",font=10,image=b)
    b2.place(x=70,y=595)
    b3=Button(root,bd=0,command=lambda:check("c","b3"),bg="#005536",activebackground="#005536",font=10,image=c)
    b3.place(x=140,y=595)
    b4=Button(root,bd=0,command=lambda:check("d","b4"),bg="#005536",activebackground="#005536",font=10,image=d)
    b4.place(x=210,y=595)
    b5=Button(root,bd=0,command=lambda:check("e","b5"),bg="#005536",activebackground="#005536",font=10,image=e)
    b5.place(x=280,y=595)
    b6=Button(root,bd=0,command=lambda:check("f","b6"),bg="#005536",activebackground="#005536",font=10,image=f)
    b6.place(x=350,y=595)
    b7=Button(root,bd=0,command=lambda:check("g","b7"),bg="#005536",activebackground="#005536",font=10,image=g)
    b7.place(x=420,y=595)
    b8=Button(root,bd=0,command=lambda:check("h","b8"),bg="#005536",activebackground="#005536",font=10,image=h)
    b8.place(x=490,y=595)
    b9=Button(root,bd=0,command=lambda:check("i","b9"),bg="#005536",activebackground="#005536",font=10,image=i)
    b9.place(x=560,y=595)
    b10=Button(root,bd=0,command=lambda:check("j","b10"),bg="#005536",activebackground="#005536",font=10,image=j)
    b10.place(x=630,y=595)
    b11=Button(root,bd=0,command=lambda:check("k","b11"),bg="#005536",activebackground="#005536",font=10,image=k)
    b11.place(x=700,y=595)
    b12=Button(root,bd=0,command=lambda:check("l","b12"),bg="#005536",activebackground="#005536",font=10,image=l)
    b12.place(x=770,y=595)
    b13=Button(root,bd=0,command=lambda:check("m","b13"),bg="#005536",activebackground="#005536",font=10,image=m)
    b13.place(x=840,y=595)
    b14=Button(root,bd=0,command=lambda:check("n","b14"),bg="#005536",activebackground="#005536",font=10,image=n)
    b14.place(x=0,y=645)
    b15=Button(root,bd=0,command=lambda:check("o","b15"),bg="#005536",activebackground="#005536",font=10,image=o)
    b15.place(x=70,y=645)
    b16=Button(root,bd=0,command=lambda:check("p","b16"),bg="#005536",activebackground="#005536",font=10,image=p)
    b16.place(x=140,y=645)
    b17=Button(root,bd=0,command=lambda:check("q","b17"),bg="#005536",activebackground="#005536",font=10,image=q)
    b17.place(x=210,y=645)
    b18=Button(root,bd=0,command=lambda:check("r","b18"),bg="#005536",activebackground="#005536",font=10,image=r)
    b18.place(x=280,y=645)
    b19=Button(root,bd=0,command=lambda:check("s","b19"),bg="#005536",activebackground="#005536",font=10,image=s)
    b19.place(x=350,y=645)
    b20=Button(root,bd=0,command=lambda:check("t","b20"),bg="#005536",activebackground="#005536",font=10,image=t)
    b20.place(x=420,y=645)
    b21=Button(root,bd=0,command=lambda:check("u","b21"),bg="#005536",activebackground="#005536",font=10,image=u)
    b21.place(x=490,y=645)
    b22=Button(root,bd=0,command=lambda:check("v","b22"),bg="#005536",activebackground="#005536",font=10,image=v)
    b22.place(x=560,y=645)
    b23=Button(root,bd=0,command=lambda:check("w","b23"),bg="#005536",activebackground="#005536",font=10,image=w)
    b23.place(x=630,y=645)
    b24=Button(root,bd=0,command=lambda:check("x","b24"),bg="#005536",activebackground="#005536",font=10,image=x)
    b24.place(x=700,y=645)
    b25=Button(root,bd=0,command=lambda:check("y","b25"),bg="#005536",activebackground="#005536",font=10,image=y)
    b25.place(x=770,y=645)
    b26=Button(root,bd=0,command=lambda:check("z","b26"),bg="#005536",activebackground="#005536",font=10,image=z)
    b26.place(x=840,y=645)
    
   
    #placement of hangman images
    c1=Label(root,bg="#005536",image=abc)
    c2=Label(root,bg="#005536",image=abr)
    c3=Label(root,bg="#005536",image=acr)
    c4=Label(root,bg="#005536",image=adr)
    c5=Label(root,bg="#005536",image=aer)
    c6=Label(root,bg="#005536",image=afr)
    c7=Label(root,bg="#005536",image=agr)
    
    # placement of first hangman image
    c1.place(x = 350,y =-10)

    # exit button
    def close():
        global New_Game
        answer = messagebox.askokcancel('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            New_Game = False
            root.destroy()

    
    B = Button(root,bd = 0,text="Close",command = close,font=("Comic Sans MS",15),bg="#005536",fg="white")
    B.place(x=10,y=10)
  
   

    # button press to check function
    def check(letter,button):
        global no_of_guesses,win_count,New_Game,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score+=1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    New_Game = True
                    root.destroy()   
                else:
                    New_Game = False
                    messagebox.showinfo('your score',score)
                    root.destroy()
        else:
            no_of_guesses += 1
            exec('c{}.destroy()'.format(no_of_guesses))
            exec('c{}.place(x={},y={})'.format(no_of_guesses+1,350,-10))
            if no_of_guesses == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    New_Game = True
                    score = 0
                    root.destroy()
                else:
                    New_Game = False
                    messagebox.showinfo('correct_word',selected_word)
                    root.destroy()   
    
    root.mainloop()
