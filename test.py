import re
from script import maximize
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import numpy as np

class InputError(BaseException):    #exception class deals with syntax error in input
    def _init_(self, m):
        self.message = m
    def _str_(self):
        return self.message
        
class read_in_obj:
    def _init_(self):   #empty constructor
        pass
    def getObjectiveInp(self, z):
        prevx = 1
        for x in z: #count number of terms [one term proceeds sign]
            if x == '+' or x == '-':
                if prevx == '+' or prevx == '-':    
                    return False
            if x.isalpha() and x != 'x':
                return False
            if x=='x' and prevx=='x':
                return False
            prevx = x
        return z
        
    def getTerms(self, z):
        n_terms=[]
        c=0
        #inspect string z and find out number of characters in each term
        for x in range(len(z)):
           if z[x] == '+' or z[x] == '-':
                n_terms.append(c)
                c=0
           else:
                c+=1
        n_terms.append(c)
        return n_terms
        
    def sort(self, eq):
        arr=[]
        for x in eq:    
            check=False
            holder = ''
            yprev=None
            for y in x:
                if check==True:
                    holder+=y
                if yprev=='x' and y.isnumeric():
                    check = True
                    holder=holder+yprev+y
                yprev=y
            arr.append(holder)

        holder=''
        for x in max(arr):
            if x.isnumeric()==True:
                holder+=x
        index=int(holder)

        #sort arr
        for i in range(len(arr)-1): 
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
            if i!=0:
                for x in range(i):
                    if arr[i] > arr[i+1]:
                        temp = arr[i]
                        arr[i]=arr[i+1]
                        arr[i+1]=temp

        arr1=[0]*index
        for x in arr:
            for y in eq:
                holder=''
                index=''
                holder2=''
                hold=False
                neg=False
                for n in y:
                    if hold==True:
                        holder+=n
                        index+=n 
                    if n=='-':
                        neg=True
                    if n == 'x':
                        hold=True
                        holder+=n 
                    if hold==False:
                        holder2+=n  
                if holder==x and neg==False:
                    if holder2=='':
                        arr1[int(index)-1]=1
                    else:
                        arr1[int(index)-1]=float(holder2)
                    break
                if holder==x and neg==True:
                    if holder2=='-':
                        arr1[int(index)-1]=-1
                    else:
                        arr1[int(index)-1]=float(holder2)
                    break

        return arr1
        
    def preSort(self, z, n_terms):
        #seperate out the terms, extract numbers and variables
        h=0
        eq=[]
        holder=''

        for x in n_terms:   #number of terms at the index
            i=0
            for i in range(x+1):
                if i+h < len(z):
                    #print(i,' ',h)
                    if z[i+h] != '+' and z[i+h] != '-':
                        holder = holder+z[i+h]
                    elif z[i+h] == '-' and i==0:
                        holder = holder+z[i+h]
                    elif z[i+h] == '+':
                        h+=1
            h=i+h
            eq.append(holder)
            holder=''
        return eq
        
    def finish(self, obj, lists):
        #negate obj
        for i in range(len(obj)):
            obj[i]=float(-1*obj[i])
        #append n zeros = len(lists)
        for i in range(len(lists)+1):
            obj.append(0.0)
        #finally append a 1
        obj.insert(len(obj)-1,1)
        return obj
  
class read_in_constraint:
    def _init_(self):
        self.n=0
    def getConstraintInp(self, obj, eq_num, plug, x_vars):         #returns a list
        #count number of constraint equations
        lists=[]
        self.n=eq_num
        if eq_num > 1:
            for z in plug:
                z=z.replace('-','+-')
                z=z.replace('<=', '+1=')
                z=z.replace('>=', '+-1=')
                if z[0]=='+':
                    z=z[:0]+z[1:]
                #print(z)

                l=re.split('\+|=',z)
                
                #self.n+=1
                lists.append(l)
        elif eq_num==1:
            z=z.replace('-','+-')
            z=z.replace('<=', '+1=')
            z=z.replace('>=', '+-1=')
            if z[0]=='+':
                z=z[:0]+z[1:]
                #print(z)

            l=re.split('\+|=',z)

            #self.n+=1
            lists.append(l)
        #print(lists)
        #allocates zeros for slack variables not part of eq    
        k=eq_num
        j=k
        if eq_num>1:
            for i in range(len(lists)):
                #print(i)
                #print(j,' ',k)
                if i==0:
                    for s in range(eq_num-1):
                        lists[i].insert(len(lists[i])-1,'0')
                    k-=1
                elif i==len(lists)-1:
                    for s in range(eq_num-1):
                        lists[i].insert(len(lists[i])-2,'0')
                else:
                    for s in range(j-k):
                        lists[i].insert(len(lists[i])-2,'0')
                    for s in range(k-1):
                        lists[i].insert(len(lists[i])-1,'0')
                    k-=1
                    
        #print(lists)
        temp=[]
        temp2=[]
        #need to sort the x variables
        #more than 1 constraint eq
        for y in range(len(lists)):
            c=-1
            for x in lists[y]:
                if ('x' in x)==True:
                    c+=1
                else:
                    break
            temp=lists[y][:c+1]
            #print(temp)
            r=0
            r1=0
            tempor=''
            check=True
            while check==True:
                check2=False
                for x in range(len(temp)-1):
                    r=temp[x].find('x')
                    r1=temp[x+1].find('x')
                    if temp[x][r:]>temp[x+1][r1:]:
                        tempor=temp[x]
                        temp[x]=temp[x+1]
                        temp[x+1]=tempor
                for x in range(len(temp)-1):
                    r=temp[x].find('x')
                    r1=temp[x+1].find('x')
                    if temp[x][r:]>temp[x+1][r1:]:
                        check2=True
                        break
                if check2==False:
                    check=False
            for i in range(len(temp)):
                lists[y][i]=temp[i]
        #print(lists)
        #len(obj) will tell us number of x-variables [let it be f]
        f=len(obj)
        for i in range(len(lists)):
            s=0
            for x in range(len(lists[i])):
                if s==f:
                    break
                holder=''
                check=False
                ck=False
                for y in lists[i][x]:
                    if check==True:
                        holder+=y
                    if y=='x':
                        check=True
                    else:
                        check=False
                if holder.isnumeric()==True:
                    #print('holder=%s , index=%d' %(holder,x+1))
                    if int(holder)!=(x+1):
                        lists[i].insert(x,'0')
                        ck=True
                if ('x' in lists[i][x])==False and ck==False:
                    lists[i].insert(x,'0')
                s+=1
        #print(lists)
        for i in range(len(lists)):
            s=0
            for x in range(len(lists[i])):
                holder=''
                if s==f:
                    break
                for y in lists[i][x]:
                    if y=='x':
                        if holder.isnumeric()==False:
                            holder='1'
                        break
                    holder+=y
                    #print(holder)
                
                lists[i][x]=holder
                s+=1
        #print(lists)
        return lists
    
    def make_num(self, lists):
        for i in range(len(lists)):
            for x in range(len(lists[i])):
                lists[i][x]=float(lists[i][x])
        return lists
        
          

class simplex:
    entries=[]
    plug=[]
    eq_num=4
    obj=''
    def __init__():
        pass
    def be():
        r=read_in_obj()

        rt=Tk()
        rt.title('Simplex Method')
        rt.configure(bg='#7D7E7E')
        rt.geometry('650x180+300+100')
        #entries=[]
        #plug=[]
        root=Frame(rt,bg='#7D7E7E')
        root.pack(side=TOP)
        #icon
        rt.iconbitmap(r'c:\Users\ahalw\icon.ico')

        #image 1
        #t_img1=ImageTk.PhotoImage(Image.open(r'c:\Users\ahalw\max.gif').resize((100,50),Image.ANTIALIAS))
        #P1=Label(root,image=t_img1)
        #label.grid(row=1, column=1)

        #Title 
        myLabel=Label(root, fg='#0D062E', bg='#7D7E7E', text="Simplex Method Calculator", borderwidth=5, font=("Courier", 14, "bold"))
        myLabel.grid(row=1, column=2)

        #image 2
        #t_img2=ImageTk.PhotoImage(Image.open(r'c:\Users\ahalw\min.jpg').resize((100,50),Image.ANTIALIAS))
        #P2=Label(root,image=t_img2)
        #P2.grid(row=1, column=3, padx=10)

        #objective fun input box and label
        of=Entry(root, width=50, borderwidth=5, font=('Times',10,'bold'))
        of.grid(row=2, column=2, pady=5)

        myLabel2=Label(root, fg='#0D062E', bg='#7D7E7E', text='Objective Function Z(x) = ', font=('Helvetica', 10, 'bold', 'italic'))
        myLabel2.grid(row=2, column=1, pady=5)

        #constraint eqs input box and label
        con=Entry(root, width=50, borderwidth=5, font=('Times',10,'bold'))
        con.grid(row=3, column=2, pady=5)
        simplex.entries.append(con)

        myLabel3=Label(root, fg='#0D062E', bg='#7D7E7E', text='Constraint Equations ', font=('Helvetica', 10, 'bold', 'italic'))
        myLabel3.grid(row=3, column=1, pady=5)
        
        #simplex.obj=''
    
        #simplex.eq_num=4  

        b1=Button(root, text='Add Another Equation', borderwidth=2, bg='black', fg='white', width=17, command=lambda:simplex.b_click(rt,root))
        b1.grid(row=4, column=1)

        b2=Button(root, text='Maximize', borderwidth=2, bg='blue', fg='white', width=12, command=lambda:simplex.calc_max(of,r))
        b2.grid(row=2, column=3)

        b3=Button(root, text='Minimize', borderwidth=2, bg='red', fg='white', width=12, command=lambda:simplex.calc_min(of,r))
        b3.grid(row=3, column=3)

        b4=Button(root, text='Clear', borderwidth=2, width=12, command=lambda:simplex.clear_entries(of))
        b4.grid(row=4, column=3)

        rt.mainloop()

    def b_click(rt,root):
        rt.geometry('')
        con1=Entry(root, width=50, borderwidth=5, font=('Times',10,'bold'))
        con1.grid(row=simplex.eq_num, column=2, pady=5)
        simplex.entries.append(con1)
        simplex.eq_num+=1

    #minimization
    def calc_min(of,r):
        inp=r.getObjectiveInp(of.get())
        if inp==False:
            messagebox.showerror('Error','Objective Function Invalid Input')
        else:
            # 0.12x1+0.15x2
            # 60x1+60x2>=300
            # 12x1+6x2>=36
            # 10x1+30x2>=90
                
            terms=r.getTerms(inp)
            obj=r.sort(r.preSort(inp,terms))
            x_vars=len(obj)
            
            #make constraint eqs [matrix ready]
            count=simplex.eq_num-4
            for entry in simplex.entries:
                if count>=0:
                    simplex.plug.append(entry.get())
                count-=1
            
            r2=read_in_constraint()
            const=r2.getConstraintInp(obj, simplex.eq_num-3, simplex.plug, len(obj))  

            num=r2.make_num(const)#constraint eqs into matrix
            i=0
            while i < len(num):
                j=len(obj)
                while j < len(num[i])-1:
                    num[i].remove(num[i][j])
                i+=1
            obj.append(0)
            num.append(obj)
            T=np.transpose(np.array(num,dtype='float'))
            temp=T[len(T)-1]
            obj=[]
            for i in range(len(temp)-1):
                obj.append(temp[i])
            const.clear()
            for i in range(len(T)-1):
                temp=[]
                for j in range(len(T[i])):
                    temp.append(T[i][j])
                const.append(temp)
            final=r.finish(obj, const) #objective function into matrix
            s_vars=len(const)   
            #create top label
            top=[]
            for x in range(x_vars):
                top.append('x'+str(x+1))

            for s in range(s_vars):
                top.append('s'+str(s+1))

            top.append('Z')
            top.append('')

            #create left label
            left=[]
            temp=''
            for s in range(s_vars):
                temp='s'+str(s+1)
                left.append(temp)
                temp=''
            left.append('Z')
            i=0
            ins=0
            while i<s_vars:
                j=0
                while j<s_vars:
                    if j==ins:
                        const[i].insert(len(const[i])-1,1)
                    else:
                        const[i].insert(len(const[i])-1,0)
                    j+=1
                ins+=1
                i+=1
            for i in range(len(const)):
                const[i].insert(len(const[i])-1,0)
            matrix=const
            matrix.append(final)
            s=maximize()
            res=s.do(x_vars, top, left, matrix, False)
            if res!=False:
                root2=Tk()
                frame=Frame(root2)
                root2.title('Results')
                root2.iconbitmap(r'c:\Users\ahalw\icon.ico')
                root2.geometry('100x100+600+150')
                root2.geometry('')
                frame.pack(side=TOP,expand=False)
                Label(frame,text='').pack()
                count=1
                for i in range(len(res)-2):
                    if i>x_vars:
                        Label(frame, text='x'+str(count)+' = '+str(res[i])).pack()
                        count+=1
                Label(frame,text='Z(x) = '+str('{:f}'.format(res[len(res)-1]))).pack()
                Label(frame,text='').pack()
            else:
                messagebox.showerror('Error','The Problem Has An Infeasible Solution')
            
            simplex.plug.clear()

#maximization
    def calc_max(of,r):
        #global obj, of
        inp=r.getObjectiveInp(of.get())
        if inp==False:
            messagebox.showerror('Error','Objective Function Invalid Input')
        else:
            terms=r.getTerms(inp)
            obj=r.sort(r.preSort(inp,terms))
            
            #make constraint eqs [matrix ready]
            count=simplex.eq_num-4
            for entry in simplex.entries:
                if count>=0:
                    if entry.get()!='':
                        simplex.plug.append(entry.get())
                count-=1
            
            r2=read_in_constraint()
            const=r2.getConstraintInp(obj, simplex.eq_num-3, simplex.plug, len(obj))  

            final=r.finish(obj, const) #objective function into matrix

            num=r2.make_num(const)#constraint eqs into matrix

            #create top label
            s_vars=r2.n #number of slack variables
            #number of x variables = len(final)-1-s_vars
            x_vars = len(final)-2-s_vars
            top=[]
            for x in range(x_vars):
                top.append('x'+str(x+1))

            for s in range(s_vars):
                top.append('s'+str(s+1))

            top.append('Z')
            top.append('')

            #create left label
            left=[]
            temp=''
            for s in range(s_vars):
                temp='s'+str(s+1)
                left.append(temp)
                temp=''
            left.append('Z')
            
            # 300x1+36x2+90x3
            # 60x1+12x2+10x3<=0.12
            # 60x1+6x2+30x3<=0.15
            
            num.append(final)
            for i in range(len(num)-1):
                num[i].insert(len(num[i])-1,0)
            matrix=num
            #pivot column - break ties by choosing left-most column
            #pivot row - break ties by choosing top-most row
            #maximization - search for most negative coefficient in z-row
            s=maximize()

            res=s.do(x_vars, top, left, matrix, True)
            
            if res!=False:
                root2=Tk()
                frame=Frame(root2)
                root2.title('Results')
                root2.iconbitmap(r'c:\Users\ahalw\icon.ico')
                root2.geometry('100x100+600+150')
                root2.geometry('')
                frame.pack(side=TOP,expand=False)
                Label(frame,text='').pack()
                for i in res:
                    Label(frame, text=str(i)).pack()
                Label(frame,text='').pack()
            else:
                messagebox.showerror('Error','The Problem Has An Infeasible Solution')
            
            simplex.plug.clear()
            
    def clear_entries(of):
        of.delete(0,END)
        for entry in simplex.entries:
            entry.delete(0,END)
