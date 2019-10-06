from tkinter import *
from tkinter import messagebox
from random import shuffle
import webbrowser

w = Tk()
w.title("~ FLAMES - FINDER ~")
print("""\n
\t   #     #       #    #
\t   ##    #       #   #  
\t   # #   #       #  #   
\t   #  #  # ##### ###    
\t   #   # #       #  #   
\t   #    ##       #   #  
\t   #     #       #    #
\n""")
print("FOR SUGGESTIONS -->> naveenstudy2000sr@gmail.com\n")
# list of words
F1=['FRIENDS','LOVE','AFFECTION','MARRIAGE','ENEMY','SISTER']
F2=['DUDES','HOMIE','ENVY','BFF','ENEMY','HELPING HAND']
F3=['JEALOUSY','BUDDIES','SOULMATES','LIKEMINDS','FRESH_FLOWER','ODD_PAIR']
F4=[]
def CF() :
    global F4,C
    F4=[]
    IT,It=0,0
    Fs=''
    while IT < len(C):
        try:
            F4.insert(It,C[IT].get())
            It+=1
            IT+=1
        except TclError:
            IT+=1
    iT=0
    while iT < len(F4) :
        if str(F4[iT]).replace(' ','')!='' :
            Fs=Fs+str(F4[iT])
            Fs=Fs+','
        iT+=1
    Fs=Fs[:-1]
    if Fs!='' :F4=Fs.split(',')
    else :F4=[]
def HF():
    messagebox.showinfo("BY WHOM ?","NAVEEN S R\nwww.linkedin.com/in/naveensr-knight")
    print('''
this application is created by me... NAVEEN S R
LINKED IN :> www.linkedin.com/in/naveensr-knight
BLOGSPOT  :> nkprosr.blogspot.com''')

#0,1
Label(w, text='   WELCOME! to your destiny ~ will it be GOOD or BAD ?   ',
      fg='GREEN', bg='LIGHTGREY', font=("Arial Bold", 15)).grid(
          row=0,column=0,columnspan=10,sticky=W+E+N+S)
Label(w).grid(row=1)

def IF():
    global F1,F2,F3,F4
    def edit():
        pass
    FI=[F1,F2,F3,F4]
    l=[1,2,3,4]
    s=[1,2,3,4]
    info=Tk()
    info.title('~INFO~')
    I=0
    iI=0
    while I<4 :
        s[I] = Scrollbar(info)
        s[I].grid(row=1,column=iI+1,sticky=N+E+W+S)
        l[I] = Listbox(info,height=6,width=27)
        l[I].grid(row=1,column=iI)
        for i in FI[I] :
            l[I].insert(END, i)
        l[I].config(yscrollcommand=s[I].set)
        s[I].config(command=l[I].yview)
        I+=1
        iI+=2
    FI=[list(set(F1)),list(set(F2)),list(set(F3)),list(set(F4))]
    I=0
    iI=0
    while I<4 :
        s[I] = Scrollbar(info)
        s[I].grid(row=3,column=iI+1,sticky=N+E+W+S)
        l[I] = Listbox(info,height=6,width=27)
        l[I].grid(row=3,column=iI)
        for i in FI[I] :
            l[I].insert(END, i)
        l[I].config(yscrollcommand=s[I].set)
        s[I].config(command=l[I].yview)
        I+=1
        iI+=2
    Label(info,text='~~IN NORMAL ORDER:',font=("Arial Bold", 15)).grid(
        row=0,column=0,columnspan=8,sticky=N+W)
    Label(info,text='~~IN SPECIAL ORDER:',font=("Arial Bold", 15)).grid(
        row=2,column=0,columnspan=8,sticky=S+W)
    def l1f(event):
        webbrowser.open_new('https://drive.google.com/open?id=1FRy1A-4CbfR97wxyXLcL8mx781y9dRSfhULVAlgUxMs')
    def l2f(event):
        webbrowser.open_new('www.linkedin.com/in/naveensr-knight')
    def l3f(e):
        webbrowser.open_new('www.nkprosr.blogspot.com')
    def l4f(event):
        webbrowser.open_new('www.nkprosr.com')
    def l5f(event):
        webbrowser.open_new('')
    def l6f(event):
        webbrowser.open_new('')
    Label(info,text='   For more info:').grid(row=4,column=0,sticky=W+N+S)
    #l1
    l1=Label(info,text='~FLAMES-FINDER~\\~F-F~ extended info v0.00',fg='blue')
    l1.grid(row=4,column=1,columnspan=5,sticky=W+N+S)
    l1.bind("<Button>",l1f)
    save=Button(info,command=edit,width=9,relief=FLAT)
    save.grid(row=4,column=6,columnspan=2,sticky=N+S+E)
    #
    line='_'
    for null in range(145):line+='_'
    Label(info,text=line).grid(row=5,column=0,columnspan=8,sticky=W+E+N)
    Label(info,text='~~CREDITS:>',font=("Copperplate Gothic Bold",12)).grid(row=6,column=0,columnspan=8,sticky=W+N+S)
    #
    Label(info,text="#  ENGLISH SUPPORT -").grid(row=7,column=0,columnspan=2,sticky=N+S+W)
    Label(info,text="Vignaesh M  B.E.[IT]",font=("need",10)).grid(row=7,column=2,columnspan=6,sticky=N+S+W)
    Label(info,text="#  CREATED BY -").grid(row=18,column=0,columnspan=2,sticky=N+S+W)
    Label(info,text="Naveen S R  B.E.[CSE]",font=("need",10)).grid(row=18,column=2,columnspan=6,sticky=N+S+W)
    Label(info,text="~ NAVEEN-KNIGHT ~",font=("need",10)).grid(row=19,column=2,columnspan=6,sticky=N+S+W)
    Label(info,text="#  INSPIRATION -").grid(row=8,column=0,columnspan=2,sticky=N+S+W)
    Label(info,text="Naveen Prasath R ",font=("need",10)).grid(row=8,column=2,columnspan=6,sticky=N+S+W)
    Label(info,text="#  TESTER -").grid(row=9,column=0,columnspan=2,sticky=N+S+W)
    Label(info,text="Aswanth K  B.Tech[Aeronautical]",font=("need",10)).grid(row=9,column=2,columnspan=6,sticky=N+S+W)
    Label(info,text="#  NON CODE DESIGNER -").grid(row=10,column=0,columnspan=2,sticky=N+S+W)
    Label(info,text="Abishek D  B.E.[CSE]",font=("need",10)).grid(row=10,column=2,columnspan=6,sticky=N+S+W)
    #link
    l2=Label(info,text='LinkenIn\\NAVEEN S R',fg='blue')
    l2.grid(row=20,column=2,columnspan=6,sticky=N+S+W)
    l2.bind("<Button>",l2f)
    l3=Label(info,text='BLOG:> nkprosr.blogspot.com',fg='blue')
    l3.grid(row=21,column=2,columnspan=6,sticky=N+S+W)
    l3.bind("<Button>",l3f)
    l4=Label(info,text='FOR MORE APPS :> www.nkprosr.com',fg='blue')
    l4.grid(row=22,column=2,columnspan=6,sticky=N+S+W)
    l4.bind("<Button>",l4f)
    info.mainloop()
Button(w,text='|\t\t\t~INFO~    ', bg='LIGHTGREY', command=IF,
       width=27, anchor=NE, relief=FLAT, padx=5, pady=5).grid(
           row=0,column=10,columnspan=2)
#2,3
Label(w, text=' Select TYPE & ORDER\t   ').grid(row=2,column=0,columnspan=3)
Label(w).grid(row=3)
textT=StringVar()
T=0
def TF() :
    global T
    T+=1
    T=T%4
    if T==0   :textT.set(' Boy VS Girl ')
    elif T==1 :textT.set(' Boy VS Boy  ')
    elif T==2 :textT.set('Girl VS Girl ')
    else      :textT.set('   CUSTOM    ')
Button(w,textvariable=textT,relief=GROOVE,width=18,command=TF).grid(row=2,column=3,columnspan=3)
textT.set(' Boy VS Girl ')
textO=StringVar()
O=0
def OF() :
    global O
    O+=1
    O=O%3
    if O==0   :textO.set('Normal  Order')
    elif O==1 :textO.set('Random Order')
    else      :textO.set('Special Order')
Button(w,textvariable=textO,relief=GROOVE,width=18,command=OF).grid(row=2,column=6,columnspan=4)
textO.set('Normal  Order')
#2.CANVAS
sw=Frame(w)
sw.grid(row=2,column=10,rowspan=5)

canvas=Canvas(sw)
sf=Frame(canvas)
sbar=Scrollbar(w, command=canvas.yview)
canvas.configure(yscrollcommand=sbar.set)

canvas.grid(row=0,column=1,pady=10)
sbar.grid(row=3,column=11,rowspan=4,sticky=N+S+W+E)

canvas.create_window((0,0),window=sf,anchor='nw')
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=180,height=150)
sf.bind("<Configure>",myfunction)


C=[]
X=[]
CX=[]
it=0
def AF () :
    global C,X,CX,it
    CX.insert(it,Frame(sf))
    CX[it].grid(row=it,column=0,columnspan=2)
    C.insert(it,Entry(CX[it],width=26))
    C[it].grid(row=it,column=0)
    X.insert(it,Button(CX[it],text='X',command=CX[it].destroy))
    X[it].grid(row=it,column=1)
    it+=1
AF()
Button(w,text='+',command=AF).grid(row=2,column=11,sticky=W+E+N+S,pady=15)
#4,5,6
Label(w,text='Your Name \t\t').grid(row=4,column=0,columnspan=3)
A=Entry(w)
A.grid(row=4,column=3,columnspan=7,sticky=W+E+N)
Label(w,text='Your suspected destiny\t').grid(row=5,column=0,columnspan=3)
B=Entry(w)
B.grid(row=5,column=3,columnspan=7,sticky=W+E+S)
Label(w).grid(row=6)
#7,8,9
Label(w,text='   To ~PREDICT~ \t\t----->>>>').grid(row=7,columnspan=6,sticky=W)
def EF () :
    messagebox.showerror("~ERROR~",'''
This eror is due to any of the following reasons:
1. Your name entry is empty
2. Your suspected destiny is empty
3. Custom list is empty''')
def FF () :
    global A,B,T,O,rf,F1,F2,F3,F4
    F=[]
    if T==0:  F=F1[:]
    elif T==1:F=F2[:]
    elif T==2:F=F3[:]
    else:CF();F=F4[:]
    if O==2 : F=set(F);F=list(F)
    elif O==1 : shuffle(F)
    a=A.get();b=B.get()
    a=a.upper().replace(' ','')
    if a=='BYWHOM?':HF()
    else:
        print('\n\nResult:')
        print(F)
        print(A.get(),'_&_',B.get(),end=' ')
        b=b.upper().replace(' ','')
        c=a
        a=''
        for ii in c:
            if ii>='A' and ii<='Z':
                a=a+ii
        c=b
        b=''
        for ii in c:
            if ii>='A' and ii<='Z':
                b=b+ii
        if len(a)==0 or len(b)==0 or len(F)==0 :
            EF()
            rf.destroy()
            del(rf)
            rf=Frame(w)
            rf.grid(row=10,column=0,columnspan=10,sticky=W)
            Label(rf).grid(row=10,column=0,columnspan=10)
            print('~ERROR~')
            
        else:
            a,b=list(a),list(b)
            if(len(a)<len(b)):miN=a;maX=b
            else:miN=b;maX=a
            del(a,b)
            c,i=len(miN)+len(maX),0
            while i<len(miN):
                I=0
                while I<len(maX):
                    if miN[i]==maX[I]:
                        del(miN[i],maX[I])
                        i-=1
                        break
                    I+=1
                i+=1
            c=len(miN)+len(maX)
            c-=1
            s,r=len(F),0
            while len(F)>1 :
                i=((c%s)+r)%s   
                del(F[i])
                r=((c%s)+r)%s
                s-=1
            print(str(F[0]))
            rf.destroy()
            del(rf)
            rf=Frame(w)
            rf.grid(row=10,column=0,columnspan=10,sticky=W)
            Label(rf,text=' You are destined to be  '+str(F[0]+'  with  '+B.get()),font=("Arial Black", 12)).grid(row=10,column=0,columnspan=10,sticky=N+W)
Button(w,text='~FIND~',command=FF).grid(row=7,column=6,columnspan=4,sticky=E)
Label(w).grid(row=8)
Label(w).grid(row=9)
txt=Text(w, height=9, width=25)
txt.grid(row=7,column=10,columnspan=2,rowspan=99)
txt.insert(END, "~Rough_Use:>")
#10,11,12,13,14,15
rf=Frame(w)
rf.grid(row=10,column=0,columnspan=10,sticky=W)
Label(rf).grid(row=10)
Label(rf).grid(row=11)

w.mainloop()
print('\n\n\t\t\tThanking You for ~ SUPPORTING ME ~')
input()
