# library imports
# sympy for symbolic representation of equations
# tkinter for user interface
# warnings for intercepting and handling warnings
from tkinter import *
from tkinter import messagebox
from sympy import *
import sympy as sym
from sympy.parsing.sympy_parser import parse_expr
import warnings


def secant():  # function to handle button press in order to calculate solution
    # the following varibales are made global for ease of access outside function
    # button on press doesn't accept functions with inputs, another reason they are global
    global pressed, root, E1, E2, E3, E4, frame
    # increment pressed when button is pressed
    pressed += 1
    # if one of the user input boxes are empty we notify the user
    if E1.get() == '' or E2.get() == '' or E3.get() == '' or E4.get() == '':
        messagebox.showwarning(title='Warning', message='Empty Input Box!')
    elif float(E4.get()) > 100:
        messagebox.showerror(title='Error', message='Invalid Error Entry')
    else:
        # try calculating the root
        try:
            calculate(pressed, E1.get(), E2.get(), E3.get(), E4.get(), frame)
        # upon raising an exception we notify the user that the input is invalid
        except BaseException:
            messagebox.showerror('Error', 'Invalid Input Syntax')
            pass


def calculate(clicks, E1, E2, E3, E4, frame):  # calculate root using secant method
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
                    prev = Label(frame, text='Error: '+str(float(error))+'%')
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


# create tkinter window object
root = Tk()
# window title
root.title('Numerical Methods')
# dimensions width x height + left offset + top offset all in pixels
# offsets are taken relative to the user's screen
root.geometry('600x200+300+200')
# can't be resized
root.resizable(0, 0)

pressed = 0

# a tkinter frame lets you organize and group widgets
# create a frame in the window
frame = Frame(root)
# pack frame onto window to fit size
frame.pack(side=TOP, expand=False)

# Header
Label(frame, text='Secant Methond Calculator',
      font=("Times", "18", "bold italic")).grid(row=0, column=1)

# label for function and input box
Label(frame, text='f(x) =', font=("Times", "12")).grid(row=1, column=0)
E1 = Entry(frame, width=50)
E1.grid(row=1, column=1, columnspan=2)

# label for initial guess x_1 and input box
l = Text(frame, width=18, height=1, borderwidth=0,
         background=root.cget("background"), font=("Times", "12"))
l.tag_configure("subscript", offset=-4)
l.insert("insert", "Initial guess x", "", "-1", "subscript", ":")
l.configure(state="disabled")
l.grid(row=2, column=0)
E2 = Entry(frame, width=50)
E2.grid(row=2, column=1, columnspan=2)

# label for intial guess x0 and input box
h = Text(frame, width=17, height=1, borderwidth=0,
         background=root.cget("background"), font=("Times", "12"))
h.tag_configure("subscript", offset=-4)
h.insert("insert", "Initial guess x", "", "0", "subscript", ":")
h.configure(state="disabled")
h.grid(row=3, column=0)
E3 = Entry(frame, width=50)
E3.grid(row=3, column=1, columnspan=2)

# label for desired error and input box
Label(frame, text='Relative Error [%]:', font=(
    "Times", "12")).grid(row=4, column=0)
E4 = Entry(frame, width=50)
E4.grid(row=4, column=1, columnspan=2)

# button to calculate solution
button = Button(frame, text='calculate', width=10,
                command=secant).grid(row=5, column=1)

# label for displaying error for caclulated solution
prev = Label(frame, text='Error: ')

# a side window containing instructions on proper syntax for functions
side_w = Tk()
side_w.attributes('-alpha', 0.8)  # transparent window
side_w.title('For Your Reference')
side_w.geometry('300x200+900+50')
side_w.resizable(0, 0)
Label(side_w, text='\n\nTrig Functions Representation\n' +
      'cosine: cos(), sine: sin(), tangent: tan()\n\n' +
      'Inverse Trig Representation\n' +
      'arccosine: acos(), arcsin: asin(), arctangent: atan()\n\n' +
      'Hyperbolic Functions\n' +
      'cosh(), sinh(), tanh()\n\n' +
      'For Syntax Reference\n' +
      'Example of a function entry:\n' +
      '3*y^(2)*(2*x+e^(3*x))-log(3*y*x)\n\n').pack()

# keep main window displayed above other
root.lift()

# loop through to keep both windows displayed
side_w.mainloop()
root.mainloop()
