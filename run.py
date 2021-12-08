from sympy import *
import sympy as sym
import warnings
from tkinter import *
from tkinter import messagebox
from sympy.parsing.sympy_parser import parse_expr
from scipy.optimize import fsolve
import numpy as np
import statistics as stat


class unconstrained:
    def __init__(self):
        pass

    def golden_min(inp, xl, xu, frame4):
        x = sym.symbols('x')
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        maximum = 0
        prev = 0
        counter = 1
        xl = float(xl)
        xu = float(xu)
        f = parse_expr(inp)
        x1bool = True
        x2bool = True
        xopt = 0
        while True:
            d = (((sqrt(5)-1)/2)*(xu-xl)).evalf()
            if x1bool == True:
                x1 = xl+d
            if x2bool == True:
                x2 = xu-d
            fx1 = f.subs(x, x1).evalf()
            fx2 = f.subs(x, x2).evalf()
            if fx2 < fx1:
                xopt = x2
                x1bool = False
                x2bool = True
                xu = x1
                x1 = x2
                maximum = fx2
            else:
                xopt = x1
                x1bool = True
                x2bool = False
                xl = x2
                x2 = x1
                maximum = fx1
            ea = 0.382*Abs((xu-xl)/xopt)*100
            if ea < 1:
                Label(frame4, text='').grid(row=5, column=1)
                Label(frame4, text='Solution').grid(row=6, column=1)
                if x1bool == True:
                    Label(frame4, text='Max. y = ' +
                          str(maximum)).grid(row=7, column=1)
                    Label(frame4, text=' Max. x = ' +
                          str(x1)).grid(row=8, column=1)
                else:
                    Label(frame4, text='Max. y = ' +
                          str(maximum)).grid(row=7, column=1)
                    Label(frame4, text=' Max. x = ' +
                          str(x1)).grid(row=8, column=1)
                Label(frame4, text='Approximate Relative Error: ' +
                      str(ea)+'%').grid(row=9, column=1)
                break
            prev = maximum
            counter += 1

    def golden_max(inp, xl, xu, frame4):
        x = sym.symbols('x')
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        maximum = 0
        prev = 0
        counter = 1
        xl = float(xl)
        xu = float(xu)
        f = parse_expr(inp)
        x1bool = True
        x2bool = True
        xopt = 0
        while True:
            d = (((sqrt(5)-1)/2)*(xu-xl)).evalf()
            if x1bool == True:
                x1 = xl+d
            if x2bool == True:
                x2 = xu-d
            fx1 = f.subs(x, x1).evalf()
            fx2 = f.subs(x, x2).evalf()
            if fx2 > fx1:
                xopt = x2
                x1bool = False
                x2bool = True
                xu = x1
                x1 = x2
                maximum = fx2
            else:
                xopt = x1
                x1bool = True
                x2bool = False
                xl = x2
                x2 = x1
                maximum = fx1
            ea = 0.382*Abs((xu-xl)/xopt)*100
            if ea < 1:
                Label(frame4, text='').grid(row=5, column=1)
                Label(frame4, text='Solution').grid(row=6, column=1)
                if x1bool == True:
                    Label(frame4, text='Max. y = ' +
                          str(maximum)).grid(row=7, column=1)
                    Label(frame4, text=' Max. x = ' +
                          str(x1)).grid(row=8, column=1)
                else:
                    Label(frame4, text='Max. y = ' +
                          str(maximum)).grid(row=7, column=1)
                    Label(frame4, text=' Max. x = ' +
                          str(x1)).grid(row=8, column=1)
                Label(frame4, text='Approximate Relative Error: ' +
                      str(ea)+'%').grid(row=9, column=1)
                break
            prev = maximum
            counter += 1

    def parab_interp(inp, x0, x1, x2, frame4):
        x = sym.symbols('x')
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        x0 = float(x0)
        x1 = float(x1)
        x2 = float(x2)
        while True:
            fx0 = f.subs(x, x0).evalf()
            fx1 = f.subs(x, x1).evalf()
            fx2 = f.subs(x, x2).evalf()
            x3 = (fx0*(x1**2-x2**2)+fx1*(x2**2-x0**2)+fx2*(x0**2-x1**2)) / \
                (2*fx0*(x1-x2)+2*fx1*(x2-x0)+2*fx2*(x0-x1))
            error = Abs((x3-x1)/x3)*100
            if error < 0.01:
                Label(frame4, text='').grid(row=6, column=1)
                Label(frame4, text='Solution').grid(row=7, column=1)
                Label(frame4, text='Max. y = ' +
                      str(f.subs(x, x3).evalf())).grid(row=8, column=1)
                Label(frame4, text=' Max. x = '+str(x3)).grid(row=9, column=1)
                Label(frame4, text='Approximate Relative Error: ' +
                      str(error)+'%').grid(row=10, column=1)
                break
            if x3 > x1:
                x0 = x1
                x1 = x3
            else:
                x2 = x1
                x1 = x3

    def newt_optim(inp, x0, frame4):
        x = sym.symbols('x')
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        x0 = float(x0)
        df = sym.diff(f, x)
        df2 = sym.diff(df, x)
        while True:
            x1 = x0-(df.subs(x, x0).evalf()/df2.subs(x, x0).evalf())
            ea = Abs((x1-x0)/x1)*100
            if ea < 1:
                Label(frame4, text='').grid(row=4, column=1)
                Label(frame4, text='Solution').grid(row=5, column=1)
                Label(frame4, text='Max. y = ' +
                      str(f.subs(x, x1).evalf())).grid(row=6, column=1)
                Label(frame4, text=' Max. x = '+str(x1)).grid(row=7, column=1)
                Label(frame4, text='Approximate Relative Error: ' +
                      str(ea)+'%').grid(row=8, column=1)
                break
            x0 = x1

    def steep_ascent(inp, x0, y0, frame4):
        x, y, h, hs = sym.symbols('x y h hs')
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        x0 = float(x0)
        y0 = float(y0)
        prevx = x0
        prevy = y0
        while True:
            dfx = sym.diff(f, x).subs(x, x0).subs(y, y0).evalf()
            dfy = sym.diff(f, y).subs(x, x0).subs(y, y0).evalf()
            g = f.subs(x, x0+dfx*h).subs(y, y0+dfy*h).evalf()

            dg = sym.diff(g.subs(h, hs), hs)
            h_star = sym.solve(dg, hs)

            x0 = x0+dfx*h_star[0]
            y0 = y0+dfy*h_star[0]

            ea1 = Abs((x0-prevx)/x0)*100
            ea2 = Abs((y0-prevy)/y0)*100

            if ea1 < 0.01 and ea2 < 0.01:
                Label(frame4, text='').grid(row=5, column=1)
                Label(frame4, text='Solution').grid(row=6, column=1)
                Label(frame4, text='Max. y = '+str(y0)).grid(row=7, column=1)
                Label(frame4, text=' Max. x = '+str(x0)).grid(row=8, column=1)
                Label(frame4, text='Approximate Relative Error: ' +
                      str((ea1+ea2)/2)+'%').grid(row=9, column=1)
                break
            prevx = x0
            prevy = y0


class curve_fitting:
    def __init__(self):
        pass

    def lin_reg(x, y, w4):
        n = len(x)
        xy = []
        sxy = 0
        sx = 0
        sy = 0
        sx2 = 0
        for i in range(len(x)):
            xy.append(float(x[i])*float(y[i]))
            sx += float(x[i])
            sy += float(y[i])
            sx2 += float(x[i])*float(x[i])
        for i in range(len(xy)):
            sxy += xy[i]
        a1 = (n*sxy-sx*sy)/(n*sx2-(sx**2))
        a0 = stat.mean(y)-a1*stat.mean(x)
        Sr = 0
        for i in range(n):
            Sr += (float(y[i])-a0-a1*float(x[i]))**2
        syx = sqrt(Sr/(n-2))
        St = 0
        for i in range(n):
            St += (float(y[i])-stat.mean(y))**2
        r2 = (St-Sr)/St
        r = sqrt(r2)
        Label(w4, text='').pack()
        Label(w4, text='y = '+str(a0)+'+ '+str(a1)+'x').pack()
        Label(w4, text='Standard Deviation = '+str(stat.stdev(y))).pack()
        Label(w4, text='Standard Error = '+str(syx)).pack()
        Label(w4, text='Coefficient of Determination = '+str(r2)).pack()
        Label(w4, text='Correlation Coefficient = '+str(r)).pack()

    def pol_reg(x, y, m, w4):
        if m == '':
            messagebox.showerror('Error', 'Input Box is Empty')
            pass
        else:
            m = int(m)
            for i in range(len(x)):
                x[i] = float(x[i])
                y[i] = float(y[i])
            n = len(x)
            s2x = 0
            s3x = 0
            sxy = 0
            for i in range(len(x)):
                s2x += x[i]**2
                s3x += x[i]**3
                sxy += x[i]*y[i]
            A = [[n, sum(x), s2x], [sum(x), s2x, s3x]]
            temp = 0
            if m > 2:
                for i in range(2):
                    j = 2+i
                    h = 2
                    while h < m:
                        for z in range(len(x)):
                            temp += x[z]**(j+1)
                        h += 1
                        j += 1
                    A[i].append(temp)
            b = [sum(y), sxy]
            power = 2
            q = 2
            for i in range(m-1):
                temp = []
                val = 0
                p = power
                for j in range(m+2):
                    if j == m+1:
                        for z in range(len(x)):
                            val += (x[z]**q)*y[z]
                        b.append(val)
                        val = 0
                        q += 1
                    else:
                        for z in range(len(x)):
                            val += x[z]**p
                        temp.append(val)
                        val = 0
                        p += 1
                A.append(temp)
                power += 1
            A = np.array(A, dtype='float')
            b = np.array(b, dtype='float')
            a = np.linalg.solve(A, b)
            Text = ''
            counter = 0
            for i in range(len(a)):
                if i == 0:
                    Text += 'y = '+str('{:.5}'.format(float(a[i])))
                elif i == 1:
                    Text += '+'+str('{:.5}'.format(float(a[i])))+'x'
                else:
                    Text += '+'+str('{:.5}'.format(float(a[i])))+'x^'+str(i)
            Label(w4, text='').pack()
            Label(w4, text=Text).pack()
            Sr = 0
            for i in range(n):
                exponent = 1
                holder = 0
                for j in range(m+2):
                    if j == 0:
                        holder += y[i]
                    if j == 1:
                        holder -= a[0]
                    if j > 1:
                        holder -= a[j-1]*x[i]**exponent
                        exponent += 1
                Sr += holder**2
            syx = sqrt(Sr/(n-(m+1)))
            St = 0
            for i in range(n):
                St += (y[i]-stat.mean(y))**2
            r2 = (St-Sr)/St
            r = sqrt(r2)
            Label(w4, text='Standard Deviation = '+str(stat.stdev(y))).pack()
            Label(w4, text='Standard Error = '+str(syx)).pack()
            Label(w4, text='Coefficient of Determination = '+str(r2)).pack()
            Label(w4, text='Correlation Coefficient = '+str(r)).pack()

    def mult_reg(x, y, m, w4):
        if m == '':
            messagebox.showerror('Error', 'Input Box is Empty')
            pass
        else:
            m = int(m)
            for i in range(len(x)):
                for j in range(len(y)):
                    x[i][j] = float(x[i][j])
                    y[i] = float(y[i])
            n = len(y)
            sx12 = 0
            sx1y = 0
            sx1x2 = 0
            for i in range(len(y)):
                sx12 += x[0][i]**2
                sx1y += x[0][i]*y[i]
                sx1x2 += x[0][i]*x[1][i]

            A = [[n, sum(x[0]), sum(x[1])], [sum(x[0]), sx12, sx1x2]]

            if m > 2:
                for i in range(2):
                    temp = 0
                    j = 2
                    if i == 0:
                        while j < m:
                            for z in range(len(y)):
                                temp += x[j][z]
                            j += 1
                        A[i].append(temp)
                    elif i == 1:
                        while j < m:
                            for z in range(len(y)):
                                temp += x[j][z]*x[0][z]
                            j += 1
                        A[i].append(temp)
            b = [sum(y), sx1y]
            q = 1
            for i in range(m-1):
                temp = []
                val = 0
                for j in range(m+2):
                    if j == m+1:
                        for z in range(len(x)):
                            val += x[q][z]*y[z]
                        b.append(val)
                        val = 0
                        q += 1
                    elif j == 0:
                        for z in range(len(x)):
                            val += x[i-1][z]
                        temp.append(val)
                        val = 0

                    else:
                        for z in range(len(x)):
                            val += x[i-1][z]*x[j-1][z]
                        temp.append(val)
                        val = 0

                A.append(temp)

            A = np.array(A, dtype='float')
            b = np.array(b, dtype='float')
            a = np.linalg.solve(A, b)
            Text = ''
            counter = 0
            for i in range(len(a)):
                if i == 0:
                    Text += 'y = '+str('{:.5}'.format(float(a[i])))
                elif i == 1:
                    Text += '+'+str('{:.5}'.format(float(a[i])))+'x'
                else:
                    Text += '+'+str('{:.5}'.format(float(a[i])))+'x^'+str(i)
            Label(w4, text='').pack()
            Label(w4, text=Text).pack()
            Sr = 0
            for i in range(n):
                exponent = 1
                holder = 0
                for j in range(m+2):
                    if j == 0:
                        holder += y[i]
                    if j == 1:
                        holder -= a[0]
                    if j > 1:
                        holder -= a[j-1]*y[i]**exponent
                        exponent += 1
                Sr += holder**2
            syx = sqrt(Sr/(n-(m+1)))
            St = 0
            for i in range(n):
                St += (y[i]-stat.mean(y))**2
            r2 = (St-Sr)/St
            r = sqrt(r2)
            Label(w4, text='Standard Deviation = '+str(stat.stdev(y))).pack()
            Label(w4, text='Standard Error = '+str(syx)).pack()
            Label(w4, text='Coefficient of Determination = '+str(r2)).pack()
            Label(w4, text='Correlation Coefficient = '+str(r)).pack()

    def nonlin_reg(x, y, inp, parameters, ig):
        w4 = Tk()
        w4.geometry('200x200+600+200')
        w4.title('Solution')
        w4.geometry('')
        ig = ig.split()
        for i in range(len(ig)):
            ig[i] = float(ig[i])
        for i in range(len(x)):
            x[i] = float(x[i])
            y[i] = float(y[i])
        X = sym.symbols('x')
        param = parameters.split()
        if len(param) != len(ig):
            messagebox.showerror(
                'Error', 'Number of inital guesses must equal number of parameters')
            pass
        else:
            s = []
            for i in param:
                s.append(sym.symbols(i))
            inp = inp.replace('e^', 'exp')
            inp = inp.replace('^', '**')
            inp = inp.replace('ln', 'log')
            inp = inp.replace('abs', 'Abs')
            c = 0
            for i in range(len(inp)-1):
                if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                    inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                    c += 1
            while True:
                f = parse_expr(inp)
                Z = []
                df = []
                F = f
                for i in range(len(s)):
                    F = F.subs(s[i], ig[i])
                    df.append(sym.diff(f, s[i]).subs(s[i], ig[i]))
                    for j in range(len(s)):
                        df[i] = df[i].subs(s[j], ig[j])
                for i in range(len(x)):
                    temp = []
                    for j in range(len(df)):
                        temp.append(df[j].subs(X, x[i]).evalf())
                    Z.append(temp)
                z = np.array(Z)
                Ztran = z.transpose()

                d = []
                for i in range(len(y)):
                    d.append(y[i]-F.subs(X, x[i]).evalf())
                D = np.array(d)
                RHS = np.array(Ztran.dot(D), dtype='float64')
                try:
                    LHS = np.linalg.inv(
                        np.array(Ztran.dot(z), dtype='float64'))
                except BaseException:
                    messagebox.showwarning(
                        'Warning', 'Can not fit to equation!')
                    pass
                A = RHS.dot(LHS)
                print(A)
                new_a = []
                for i in range(len(A)):
                    new_a.append(ig[i]+A[i])
                a = np.array(new_a, dtype='float32')
                error = []
                for i in range(len(a)):
                    error.append(Abs((a[i]-ig[i])/a[i])*100)
                avg = sum(error)/len(error)
                if avg < 1:
                    Label(w4, text='').pack()
                    for i in range(len(a)):
                        Label(w4, text='a'+str(i)+' = '+str(a[i])).pack()
                    Label(w4, text='True Relative Error: '+str(avg)+'%').pack()
                    break
                else:
                    ig = a


class integrate:
    def __init__(self):
        pass

    def sing_trap(inp, a, b, frame3, w3):
        a = float(a)
        b = float(b)
        x = sym.symbols('x')
        # reformat the input
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        I = (b-a)*(f.subs(x, a).evalf()+f.subs(x, b).evalf())/2
        fp = sym.diff(f, x)
        fpp = sym.diff(fp, x)
        fppx = sym.integrate(fpp, (x, a, b))/(b-a)
        Ea = (-1/12)*fppx*(b-a)**3
        Label(frame3, text='Solution').grid(row=5, column=1)
        Label(frame3, text='Integral = '+str(I)).grid(row=6, column=1)
        Label(frame3, text='Approximate Error = '+str(Ea)).grid(row=7, column=1)

    def mult_trap(inp, a, b, n, frame3, w3):
        a = float(a)
        b = float(b)
        n = int(n)
        x = sym.symbols('x')
        # reformat the input
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        fx0 = f.subs(x, a).evalf()
        fx1 = 0
        step = (b-a)/(n)
        var = step
        for i in range(n-1):
            fx1 += f.subs(x, var).evalf()
            var += step

        fx2 = f.subs(x, b).evalf()

        I = (b-a)*((fx0+2*fx1+fx2)/(2*n))
        fp = sym.diff(f, x)
        fpp = sym.diff(fp, x)
        fppx = sym.integrate(fpp, (x, a, b))/(b-a)
        Ea = ((-b+a)**3/(12*n**2))*fppx
        Label(frame3, text='Solution').grid(row=5, column=1)
        Label(frame3, text='Integral = '+str(I)).grid(row=6, column=1)
        Label(frame3, text='Approximate Error = '+str(Ea)).grid(row=7, column=1)

    def sing_onethird(inp, a, b, frame3, w3):
        a = float(a)
        b = float(b)
        x = sym.symbols('x')
        # reformat the input
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        I = (b-a)*(f.subs(x, a).evalf()+4 *
                   f.subs(x, (b-a)/2)+f.subs(x, b).evalf())/6
        fp = sym.diff(f, x)
        fpp = sym.diff(fp, x)
        f3p = sym.diff(fpp, x)
        f4p = sym.diff(f3p, x)
        f4px = sym.integrate(f4p, (x, a, b))/(b-a)
        Ea = f4px*((-b+a)**5)/2880
        Label(frame3, text='Solution').grid(row=5, column=1)
        Label(frame3, text='Integral = '+str(I)).grid(row=6, column=1)
        Label(frame3, text='True Error = '+str(Ea)).grid(row=7, column=1)

    def mult_onethird(inp, a, b, n, frame3, w3):
        a = float(a)
        b = float(b)
        n = int(n)
        x = sym.symbols('x')
        # reformat the input
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        fx0 = f.subs(x, a).evalf()
        fx1 = 0
        fx2 = 0
        step = (b-a)/(n)
        var = step
        i = 1
        while i <= n-1:
            if i % 2 == 1:
                fx1 += f.subs(x, var).evalf()
                var += step
            if i % 2 == 0:
                fx2 += f.subs(x, var).evalf()
                var += step
            i += 1

        fx3 = f.subs(x, b).evalf()

        I = (b-a)*((fx0+4*fx1+2*fx2+fx3)/(3*n))
        fp = sym.diff(f, x)
        fpp = sym.diff(fp, x)
        f3p = sym.diff(fpp, x)
        f4p = sym.diff(f3p, x)
        f4px = sym.integrate(f4p, (x, a, b))/(b-a)
        Ea = ((-b+a)**5/(180*n**4))*f4px
        Label(frame3, text='Solution').grid(row=5, column=1)
        Label(frame3, text='Integral = '+str(I)).grid(row=6, column=1)
        Label(frame3, text='Approximate Error = '+str(Ea)).grid(row=7, column=1)

    def threeEighth(inp, a, b, frame3, w3):
        a = float(a)
        b = float(b)
        x = sym.symbols('x')
        # reformat the input
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1
        f = parse_expr(inp)
        step = (b-a)/3
        I = (b-a)*(f.subs(x, a).evalf()+3*f.subs(x, a+step)+3 *
                   f.subs(x, a+step*2).evalf()+f.subs(x, b).evalf())/8
        fp = sym.diff(f, x)
        fpp = sym.diff(fp, x)
        f3p = sym.diff(fpp, x)
        f4p = sym.diff(f3p, x)
        f4px = sym.integrate(f4p, (x, a, b))/(b-a)
        Ea = f4px*((-b+a)**5)/6480
        Label(frame3, text='Solution').grid(row=5, column=1)
        Label(frame3, text='Integral = '+str(I)).grid(row=6, column=1)
        Label(frame3, text='True Error = '+str(Ea)).grid(row=7, column=1)

    def uneq_segments(x, fx, w3):
        I = 0
        for i in range(len(x)-1):
            I += (float(x[i+1])-float(x[i]))*((float(fx[i])+float(fx[i+1]))/2)
        Label(w3, text='').pack()
        Label(w3, text='Integral: '+str(I),
              font=("Times", "12", "bold")).pack()


class differentiate:
    def __init__(self):
        pass

    def fkutta_eval(df, end, h, x0, y0, frame2, w2):
        x, y = sym.symbols('x y')
        while x0 < end:
            k1 = (df.subs(x, x0).evalf()).subs(y, y0).evalf()
            k2 = (df.subs(x, x0+0.25*h).evalf()).subs(y, y0+0.25*k1*h).evalf()
            k3 = (df.subs(x, x0+0.25*h).evalf()).subs(y,
                                                      y0+0.125*k1*h+0.125*k2*h).evalf()
            k4 = (df.subs(x, x0+0.5*h).evalf()
                  ).subs(y, y0-0.5*k2*h+k3*h).evalf()
            k5 = (df.subs(x, x0+0.75*h).evalf()).subs(y,
                                                      y0+(3/16)*k1*h+(9/16)*k4*h).evalf()
            k6 = (df.subs(x, x0+h).evalf()).subs(y, y0-(3/7)*k1*h+(2/7)
                                                 * k2*h+(12/7)*k3*h-(12/7)*k4*h+(8/7)*k5*h).evalf()
            y1 = y0+(1/90)*(7*k1+32*k3+12*k4+32*k5+7*k6)*h

            y0 = y1
            x0 += h
        return y1

    def fif_rkutta(inp, end, h, x0, y0, frame2, w2):
        x0 = float(x0)
        y0 = float(y0)
        h = float(h)
        end = float(end)

        if Abs(x0-end) % h != 0:
            messagebox.showerror(
                title='Error', message="x-value to evaluate doesn't agree with step size value")
            w2.lift()
        else:
            x, y = sym.symbols('x y')
            # reformat the input
            inp = inp.replace('e^', 'exp')
            inp = inp.replace('^', '**')
            inp = inp.replace('ln', 'log')
            inp = inp.replace('abs', 'Abs')
            c = 0
            for i in range(len(inp)-1):
                if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                    inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                    c += 1

            df = parse_expr(inp)

            while x0 < end:
                k1 = (df.subs(x, x0).evalf()).subs(y, y0).evalf()
                k2 = (df.subs(x, x0+0.25*h).evalf()
                      ).subs(y, y0+0.25*k1*h).evalf()
                k3 = (df.subs(x, x0+0.25*h).evalf()).subs(y,
                                                          y0+0.125*k1*h+0.125*k2*h).evalf()
                k4 = (df.subs(x, x0+0.5*h).evalf()
                      ).subs(y, y0-0.5*k2*h+k3*h).evalf()
                k5 = (df.subs(x, x0+0.75*h).evalf()).subs(y,
                                                          y0+(3/16)*k1*h+(9/16)*k4*h).evalf()
                k6 = (df.subs(x, x0+h).evalf()).subs(y, y0-(3/7)*k1*h +
                                                     (2/7)*k2*h+(12/7)*k3*h-(12/7)*k4*h+(8/7)*k5*h).evalf()
                y1 = y0+(1/90)*(7*k1+32*k3+12*k4+32*k5+7*k6)*h

                y0 = y1
                x0 += h
                # 4*e^(0.8*x)-0.5*y

            Label(frame2, text='Solution').grid(row=6, column=1)
            Label(frame2, text='y('+str(end)+') = ' +
                  str(y1)).grid(row=7, column=1)

    def runge_kutta(inp, end, h, x0, y0, frame2, w2):
        x0 = float(x0)
        y0 = float(y0)
        h = float(h)
        end = float(end)

        if Abs(x0-end) % h != 0:
            messagebox.showerror(
                title='Error', message="x-value to evaluate doesn't agree with step size value")
            w2.lift()
        else:
            x, y = sym.symbols('x y')
            # reformat the input
            inp = inp.replace('e^', 'exp')
            inp = inp.replace('^', '**')
            inp = inp.replace('ln', 'log')
            inp = inp.replace('abs', 'Abs')
            c = 0
            for i in range(len(inp)-1):
                if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                    inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                    c += 1

            df = parse_expr(inp)
            tval = differentiate.fkutta_eval(df, end, h, x0, y0, frame2, w2)

            while x0 < end:
                k1 = (df.subs(x, x0).evalf()).subs(y, y0).evalf()
                k2 = (df.subs(x, x0+0.5*h).evalf()
                      ).subs(y, y0+0.5*k1*h).evalf()
                k3 = (df.subs(x, x0+0.5*h).evalf()
                      ).subs(y, y0+0.5*k2*h).evalf()
                k4 = (df.subs(x, x0+h).evalf()).subs(y, y0+k3*h).evalf()
                y1 = y0+(1/6)*(k1+2*k2+2*k3+k4)*h

                y0 = y1
                x0 += h
                et = 100*Abs((tval-y1)/tval)
                # 4*e^(0.8*x)-0.5*y

            Label(frame2, text='Solution').grid(row=6, column=1)
            Label(frame2, text='y('+str(end)+') = ' +
                  str(y1)).grid(row=7, column=1)
            Label(frame2, text='Error: '+str(et)+'%').grid(row=8, column=1)

    def midpoint(inp, end, h, x0, y0, frame2, w2):
        x0 = float(x0)
        y0 = float(y0)
        h = float(h)
        end = float(end)

        if Abs(x0-end) % h != 0:
            messagebox.showerror(
                title='Error', message="x-value to evaluate doesn't agree with step size value")
            w2.lift()
        else:
            x, y = sym.symbols('x y')
            # reformat the input
            inp = inp.replace('e^', 'exp')
            inp = inp.replace('^', '**')
            inp = inp.replace('ln', 'log')
            inp = inp.replace('abs', 'Abs')
            c = 0
            for i in range(len(inp)-1):
                if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                    inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                    c += 1
            df = parse_expr(inp)
            tval = differentiate.fkutta_eval(df, end, h, x0, y0, frame2, w2)

            while x0 < end:
                y_half = y0+(df.subs(x, x0).evalf()).subs(y, y0).evalf()*(h/2)
                y1 = y0+(df.subs(x, x0+(h/2)).evalf()
                         ).subs(y, y_half).evalf()*h
                print(y1)
                y0 = y1
                x0 += h

            et = 100*Abs((tval-y1)/tval)

            Label(frame2, text='Solution').grid(row=6, column=1)
            Label(frame2, text='y('+str(end)+') = ' +
                  str(y1)).grid(row=7, column=1)
            Label(frame2, text='Error: '+str(et)+'%').grid(row=8, column=1)

    def heun(inp, end, h, x0, y0, frame2, w2):
        x0 = float(x0)
        y0 = float(y0)
        h = float(h)
        end = float(end)

        if Abs(x0-end) % h != 0:
            messagebox.showerror(
                title='Error', message="x-value to evaluate doesn't agree with step size value")
            w2.lift()
        else:
            x, y = sym.symbols('x y')
            # reformat the input
            inp = inp.replace('e^', 'exp')
            inp = inp.replace('^', '**')
            inp = inp.replace('ln', 'log')
            inp = inp.replace('abs', 'Abs')
            c = 0
            for i in range(len(inp)-1):
                if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                    inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                    c += 1
            df = parse_expr(inp)
            tval = differentiate.fkutta_eval(df, end, h, x0, y0, frame2, w2)

            i = x0
            while i < end:
                yi = y0
                y0ip1 = yi+(df.subs(x, x0).evalf()).subs(y, y0).evalf()*h

                yip1 = yi+((df.subs(x, x0).evalf()).subs(y, y0).evalf() +
                           (df.subs(x, x0+h).evalf()).subs(y, y0ip1).evalf())*(h/2)
                if i+1 == end:
                    break
                # 4e^(0.8*x)-0.5*y
                x0 = x0+h
                y0 = yip1
                i += h
            prev = yip1
            et = Abs((tval-prev)/tval)*100
            print(et)
            # extra iterations
            iterations = 1
            while et > 1:
                yip1 = yi+((df.subs(x, x0).evalf()).subs(y, y0).evalf() +
                           (df.subs(x, x0+h).evalf()).subs(y, prev).evalf())*(h/2)
                if Abs(prev-yip1) < 0.000001:
                    break
                et = Abs((tval-prev)/tval)*100
                prev = yip1
                print(et)
                iterations += 1
            Label(frame2, text='Solution').grid(row=6, column=1)
            Label(frame2, text='y('+str(end)+') = ' +
                  str(prev)).grid(row=7, column=1)
            Label(frame2, text='Error: '+str(et)+'%').grid(row=8, column=1)
            Label(frame2, text='Iterations: ' +
                  str(iterations)).grid(row=9, column=1)

    def euler(inp, end, h, x0, y0, frame2, w2):
        x0 = float(x0)
        y0 = float(y0)
        h = float(h)
        end = float(end)

        if Abs(x0-end) % h != 0:
            messagebox.showerror(
                title='Error', message="x-value to evaluate doesn't agree with step size value")
            w2.lift()
        else:
            x, y = sym.symbols('x y')
            # reformat the input
            inp = inp.replace('e^', 'exp')
            inp = inp.replace('^', '**')
            inp = inp.replace('ln', 'log')
            inp = inp.replace('abs', 'Abs')
            c = 0
            for i in range(len(inp)-1):
                if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                    inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                    c += 1

            df = parse_expr(inp)
            tval = differentiate.fkutta_eval(df, end, h, x0, y0, frame2, w2)

            i = x0
            while i < end:
                df0 = df.subs(x, i)
                df0 = df0.subs(y, y0)

                y1 = y0+df0*h
                print(y1)
                y0 = y1
                i += h
            et = 100*Abs((tval-y1)/tval)
            print(tval)
            Label(frame2, text='Solution').grid(row=6, column=1)
            Label(frame2, text='y('+str(i)+') = ' +
                  str(y1)).grid(row=7, column=1)
            Label(frame2, text='True Relative Error: ' +
                  str(et)+'%').grid(row=8, column=1)


class execute:
    def __init__(self, clicks):
        self.clicks = clicks
        prev = 0
        prev1 = 0
        prev2 = 0
        prev3 = 0

    def sys_eq(self, inp, x, ig):
        # determine symbols based on input
        var_num = len(x)  # number of variables = number of equations

        # print(inp)
        for i in range(len(inp)):
            inp[i] = inp[i].replace('e^', 'exp')
            inp[i] = inp[i].replace('^', '**')
            inp[i] = inp[i].replace('ln', 'log')
            inp[i] = inp[i].replace('abs', 'Abs')
            c = 0
            for j in range(len(inp)-1):
                if inp[i][j+c].isnumeric() and inp[i][j+1+c].isalpha():
                    inp[i] = inp[i][0:j+1+c]+'*'+inp[i][j+1+c:]
                    c += 1
        f = []
        for i in inp:
            f.append(i)

        for i in range(len(f)):
            f[i] = parse_expr(f[i])

        # define partial derivatives
        df_partials = []
        for i in range(len(f)):
            for j in range(var_num):
                df_partials.append(sym.diff(f[i], x[j]))

        nl = sqrt(len(df_partials))
        hold = []
        step = nl
        for i in range(nl):
            if i == 0:
                hold.append(df_partials[0:step])
            else:
                hold.append(df_partials[step:step+nl])
        df_partials = hold
        # df_partials contain partial derivatives
        # matrix A = df_partials
        # matrix x contains variables

        # define f with inital values plugged in
        temp = f
        fi = temp

        for i in range(len(fi)):  # make all variable substitutions into each equation
            for j in range(var_num):
                fi[i] = fi[i].subs(x[j], ig[j])

        for i in range(len(fi)):  # evaluate each function
            fi[i] = fi[i].evalf()

        # define df_partials with initial values plugged in
        dfi = []
        co = 0
        for i in range(len(df_partials)):
            for j in range(len(df_partials[i])):
                for k in range(var_num):
                    if k == 0:
                        dfi.append(df_partials[i][j].subs(x[k], ig[k]))
                    else:
                        dfi[co] = dfi[co].subs(x[k], ig[k])
                co += 1

        hold = []
        step = nl
        for i in range(nl):
            if i == 0:
                hold.append(dfi[0:step])
            else:
                hold.append(dfi[step:step+nl])
        dfi = hold

        A = np.array(dfi, dtype='float')

        B = []
        co = 0
        temp = 0

        for i in range(var_num):
            for j in range(var_num+1):
                if j == 0:
                    B.append(-1*fi[i])
                else:
                    temp = B[co]
                    B[co] = temp+(dfi[co][j-1]*ig[j-1])
            co += 1

        b = np.array(B, dtype='float')
        solution = np.linalg.solve(A, b)
        # error evaluation
        error = []
        for i in range(len(solution)):
            error.append(Abs((solution[i]-ig[i])/solution[i])*100)
        avg = 0
        for i in range(len(error)):
            avg += error[i]
        avg = (avg/len(error))

        return [avg, solution]

    def mod_newt(self, E1, E2, E3, frame):
        global prev
        if self.clicks > 1:
            try:
                prev.destroy()
            except TclError:
                self.clicks = 1

        # inital run
        x = sym.symbols('x')

        inp = E1

        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1

        counter = 0
        des_err = float(E3)

        for i in str(E3):
            if i == '.':
                counter += 1
                break
            else:
                counter += 1
        n = len(str(E3))-counter

        x0 = float(E2)

        option = True

        if 'log' in inp:

            f = parse_expr(inp)

            fx0 = f.subs(x, x0).evalf()
            df = sym.diff(f, x)
            dfx0 = df.subs(x, x0).evalf()
            d2f = sym.diff(df, x)
            d2fx0 = d2f.subs(x, x0).evalf()
            x1 = x0-((fx0*dfx0)/(dfx0*dfx0-fx0*d2fx0))
            fx1 = f.subs(x, x1).evalf()

            s = sym.solve(f, x)

            s.append(0)
            tvalue = float(s[0])
            option = True
        else:
            df = sym.diff(parse_expr(inp), x)
            d2f = sym.diff(df, x)
            df = lambdify(x, df)
            d2f = lambdify(x, d2f)
            f = lambdify(x, parse_expr(inp))

            fx0 = f(x0)
            dfx0 = df(x0)
            d2fx0 = d2f(x0)
            x1 = x0-((fx0*dfx0)/(dfx0*dfx0-fx0*d2fx0))
            fx1 = f(x1)

            tvalue = float(fsolve(f, x0))
            option = False

        error = (Abs(tvalue-x1)/Abs(tvalue))*100

        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                while error > des_err:

                    x0 = x1
                    fx0 = fx1

                    if option == True:
                        dfx0 = df.subs(x, x0).evalf()
                        d2fx0 = d2f.subs(x, x0).evalf()
                        x1 = x0-((fx0*dfx0)/(dfx0*dfx0-fx0*d2fx0))
                        fx1 = f.subs(x, x1).evalf()
                    else:
                        dfx0 = df(x0)
                        d2fx0 = d2f(x0)
                        x1 = x0-((fx0*dfx0)/(dfx0*dfx0-fx0*d2fx0))
                        fx1 = f(x1)

                    error = (Abs(tvalue-x1)/Abs(tvalue))*100

                Label(frame, text='Root:  ' +
                      str('{:.8}'.format(float(x1)))).grid(row=5, column=0, padx=10)
                if n <= 6:
                    prev = Label(frame, text='Error: ' +
                                 str("{:f}".format(float(error)))+'%')
                    prev.grid(row=6, column=0, padx=10)
                else:
                    prev = Label(frame, text='Error: '+str(float(error))+'%')
                    prev.grid(row=6, column=0, padx=10)

                Label(frame, text='Solution', font=("Times", "12")).grid(
                    row=4, column=0, padx=10)

            except RuntimeWarning:
                messagebox.showerror('Error', 'Solution Diverges')
                pass
            except TypeError:
                messagebox.showerror('Error', 'Solution Diverges')
                pass

    def newt(self, E1, E2, E3, frame):
        global prev
        if self.clicks > 1:
            try:
                prev.destroy()
            except TclError:
                self.clicks = 1

        # inital run
        x = sym.symbols('x')

        inp = E1

        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1

        counter = 0
        des_err = float(E3)

        for i in str(E3):
            if i == '.':
                counter += 1
                break
            else:
                counter += 1
        n = len(str(E3))-counter

        x0 = float(E2)

        option = True

        if 'log' in inp:

            f = parse_expr(inp)

            fx0 = f.subs(x, x0).evalf()
            df = sym.diff(f, x)
            dfx0 = df.subs(x, x0).evalf()
            x1 = x0-(fx0/dfx0)
            fx1 = f.subs(x, x1).evalf()

            s = sym.solve(f, x)

            s.append(0)
            tvalue = float(s[0])
            option = True
        else:
            df = sym.diff(parse_expr(inp), x)
            df = lambdify(x, df)
            f = lambdify(x, parse_expr(inp))

            fx0 = f(x0)
            dfx0 = df(x0)
            x1 = x0-(fx0/dfx0)
            fx1 = f(x1)

            tvalue = float(fsolve(f, x0))
            option = False

        error = (Abs(tvalue-x1)/Abs(tvalue))*100

        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                while error > des_err:

                    x0 = x1
                    fx0 = fx1

                    if option == True:
                        dfx0 = df.subs(x, x0).evalf()
                        x1 = x0-(fx0/dfx0)
                        fx1 = f.subs(x, x1).evalf()
                    else:
                        dfx0 = df(x0)
                        x1 = x0-(fx0/dfx0)
                        fx1 = f(x1)

                    error = (Abs(tvalue-x1)/Abs(tvalue))*100

                Label(frame, text='Root:  ' +
                      str(float('{:.8}'.format(x1)))).grid(row=5, column=0, padx=10)
                if n <= 6:
                    prev = Label(frame, text='Error: ' +
                                 str("{:f}".format(float(error)))+'%')
                    prev.grid(row=6, column=0, padx=10)
                else:
                    prev = Label(frame, text='Error: '+str(float(error))+'%')
                    prev.grid(row=6, column=0, padx=10)

                Label(frame, text='Solution', font=("Times", "12")).grid(
                    row=4, column=0, padx=10)

            except RuntimeWarning:
                messagebox.showerror('Error', 'Solution Diverges')
                pass
            except TypeError:
                messagebox.showerror('Error', 'Solution Diverges')
                pass

    def finish(self, E1, E2, E3, E4, frame):  # secant method
        # global variable to hold the displayed solution in tkinter
        # making it global allows us to access previous display on UI and destroy it
        global prev
        # If the user recalculates, and therefore has clicked a second time, the solution user interface is cleared
        # to prevent the result from the previous calculation from overlapping with the current display
        if clicks > 1:
            # since destroy() is a Tcl command we try it with an except of Tcl error that
            # might arise if a solution is not found and prev is null and we try to destroy nothing
            try:
                prev.destroy()
            except TclError:
                clicks = 1
        # inital run
        x = sym.symbols('x')  # identify x as a symbol
        inp = E1  # stores function as a string

        # replace mathematical symbols with python equaivalent symbols for calculating
        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')

        c = 0  # counter for indexing
        # iterate over the length of the input function string
        for i in range(len(inp)-1):
            # determine when a number is followed by a symbol, denoting multiplication
            # insert a * sign
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1

        counter = 0
        # user desired error
        des_err = float(E4)
        # determine number of decimal places for formatting float in the solution
        for i in str(E4):
            if i == '.':
                counter += 1
                break
            else:
                counter += 1
        n = len(str(E4))-counter

        # initial estimates of x @ i-1 and x @ i-2 are provided by the user
        xi_2 = float(E2)
        xi_1 = float(E3)

        option = True
        # parse_expr takes a string and returns a SymPy expression to evaluating using the SymPy module
        # subs substitutes a variable x with another variable like xi_1 which in our case holds a float value
        # evalf() returns an evaluated expression
        # lambdify transforms sympy expressions to lamda functions which can be used to calculate numerical values fast
        if 'log' in inp:

            f = parse_expr(inp)

            # secant method formula
            fxi_2 = f.subs(x, xi_2).evalf()
            fxi_1 = f.subs(x, xi_1).evalf()
            xi = xi_1 - ((fxi_1*(xi_2-xi_1))/(fxi_2-fxi_1))
            fxi = f.subs(x, xi).evalf()

            option = True
        else:
            # make a function out of f to get f(x) for ease of writing code
            f = lambdify(x, parse_expr(inp))

            fxi_2 = f(xi_2)
            fxi_1 = f(xi_1)

            xi = xi_1 - ((fxi_1*(xi_2-xi_1))/(fxi_2-fxi_1))
            fxi = f(xi)

            option = False

        error = (Abs(xi-xi_1)/Abs(xi))*100

        # handle error while carrying multiple iterations till the error is less than the desired error
        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                # run iterations to calculate the root until the error is less than or equal the desired error
                while error > des_err:
                    xi_2 = xi_1
                    xi_1 = xi

                    fxi_2 = fxi_1
                    fxi_1 = fxi

                    xi = xi_1 - ((fxi_1*(xi_2-xi_1))/(fxi_2-fxi_1))

                    if option == True:
                        fxi = f.subs(x, xi).evalf()
                    else:
                        fxi = f(xi)
                    # print(fxi)
                    error = (Abs(xi-xi_1)/Abs(xi))*100
                # check that the function evaluated at the calculated root is within at least 0.1 of 0
                if(Abs(fxi-0) > 0.1):
                    # replace old text with blank to clear it
                    Label(frame, text='                                    ').grid(
                        row=5, column=0, padx=10)
                    Label(frame, text='                                    ').grid(
                        row=6, column=0, padx=10)
                    messagebox.showwarning('Warning', 'Adjust Initial Guesses\n Root: '+str(
                        float('{:.8}'.format(xi)))+'\n f(x): '+str(float('{:.8}'.format(fxi))))
                else:
                    # display calculated root value
                    Label(frame, text='Root:  ' +
                          str(float('{:.8}'.format(xi)))).grid(row=6, column=0, padx=10)
                    # formatting the error calculated to ensure all digits are shown
                    if n <= 6:
                        prev = Label(frame, text='Error: ' +
                                     str("{:f}".format(float(error)))+'%')
                        prev.grid(row=7, column=0, padx=10)
                    else:
                        prev = Label(frame, text='Error: ' +
                                     str(float(error))+'%')
                        prev.grid(row=7, column=0, padx=10)

                    Label(frame, text='Solution', font=("Times", "12")).grid(
                        row=5, column=0, padx=10)
            except RuntimeWarning:
                messagebox.showerror('Error', 'Solution Diverges')
                pass
            # getting imaginary numbers means that solution diverges and a type error might arise
            except TypeError:
                messagebox.showerror('Error', 'Solution Diverges')
                pass

    def mod_finish(self, E1, E2, E3, E4, frame):
        global prev2
        if self.clicks > 1:
            try:
                prev2.destroy()
            except TclError:
                self.clicks = 1
        # inital run
        x = sym.symbols('x')
        inp = E1

        inp = inp.replace('e^', 'exp')
        inp = inp.replace('^', '**')
        inp = inp.replace('ln', 'log')
        inp = inp.replace('abs', 'Abs')
        c = 0
        for i in range(len(inp)-1):
            if inp[i+c].isnumeric() and inp[i+1+c].isalpha():
                inp = inp[0:i+1+c]+'*'+inp[i+1+c:]
                c += 1

        counter = 0
        des_err = float(E4)

        for i in str(E4):
            if i == '.':
                counter += 1
                break
            else:
                counter += 1
        n = len(str(E4))-counter

        x0 = float(E2)
        dx0 = float(E3)

        option = True

        if 'log' in inp:

            f = parse_expr(inp)
            print(type(f))

            fx0 = f.subs(x, x0).evalf()
            fx0_dx0 = f.subs(x, x0+dx0).evalf()
            x1 = x0-((dx0*fx0)/(fx0_dx0-fx0))
            fx1 = f.subs(x, x1).evalf()

            s = sym.solve(f, x)
            print(s)
            s.append(0)
            tvalue = float(s[0])
            option = True
        else:
            f = lambdify(x, parse_expr(inp))

            fx0 = f(x0)
            fx0_dx0 = f(x0+dx0)
            x1 = x0-((dx0*fx0)/(fx0_dx0-fx0))
            fx1 = f(x1)

            tvalue = float(fsolve(f, x0))
            option = False

        error = (Abs(tvalue-x1)/Abs(tvalue))*100

        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                while error >= des_err:

                    x0 = x1
                    fx0 = fx1

                    if option == True:
                        fx0_dx0 = f.subs(x, x0+dx0).evalf()
                        x1 = x0-((dx0*fx0)/(fx0_dx0-fx0))
                        fx1 = f.subs(x, x1).evalf()
                    else:
                        fx0_dx0 = f(x0+dx0)
                        x1 = x0-((dx0*fx0)/(fx0_dx0-fx0))
                        fx1 = f(x1)

                    error = (Abs(tvalue-x1)/Abs(tvalue))*100

                Label(frame, text='Root:  ' +
                      str(float('{:.8}'.format(x1)))).grid(row=6, column=0, padx=10)
                if n <= 6:
                    prev2 = Label(frame, text='Error: ' +
                                  str("{:f}".format(float(error)))+'%')
                    prev2.grid(row=7, column=0, padx=10)
                else:
                    prev2 = Label(frame, text='Error: '+str(float(error))+'%')
                    prev2.grid(row=7, column=0, padx=10)

                Label(frame, text='Solution', font=("Times", "12")).grid(
                    row=5, column=0, padx=10)
            except RuntimeWarning:
                messagebox.showerror('Error', 'Solution Diverges')
                pass
            except TypeError:
                messagebox.showerror('Error', 'Solution Diverges')
                pass
