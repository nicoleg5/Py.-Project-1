def get_inputs():
#   Desc: Welcomes the user and requests three coefficients
#   Inputs: (None)
#   Outputs: A tuple of three values (presumed to be numbers)

    print('Hello. Welcome to the polynomial solver.')
    print('Please enter a, b, and c, to see the solutions of ax^2 + bx + c = 0.')
    

    a = float(input('Please enter a: '))
    b = float(input('Please enter b: '))
    c = float(input('Please enter c: '))

    coeff = (a, b, c)

    return(coeff)


def root_order(x1, x2):

  if isinstance(x1, complex) and isinstance(x2, complex):
      x3 = x1.real
      x4 = x2.real

      if x3 < x4:
        smaller = x1
        larger = x2
        print("There are two solutions: x = {:.4f} and x = {:.4f}".format(smaller, larger))
      elif x3 > x4:
        smaller = x2
        larger = x1
        print("There are two solutions: x = {:.4f} and x = {:.4f}".format(smaller, larger))
      else:
        print("There are two solutions: x = {:.4f} and x = {:.4f}".format(x1, x2))

  else:
    
      if x1 < x2:
        smaller = x1
        larger = x2
        print("There are two solutions: x = {:.4f} and x = {:.4f}".format(smaller, larger))
      elif x1 > x2:
        smaller = x2
        larger = x1
        print("There are two solutions: x = {:.4f} and x = {:.4f}".format(smaller, larger))
      else:
        print("There are two solutions: x = {:.4f} and x = {:.4f}".format(x1, x2))


def is_number(x):
#   Desc: Checks whether its input is numerical or not
#   Inputs: x (can be of any type)
#   Outputs: bool (true if x is numerical; False otherwise)

    try:
        float(x)
        return(True)
    except ValueError:
        return(False)


def linear_solver(a, b):
#   Desc: solves the linear equation ax + b = 0 for x
#   Inputs: a and b (both numerical. a is assumed nonzero)
#   Outputs: the solution to ax+ b = 0, float
    
    return(-b / a)


def quadratic_solver(a, b, c):
#   Desc: Solves the quadratic equation ax^2 + bx + c = 0 for x
#   Inputs: a, b, and c (all numerical, a is assumed nonzero)
#   Outputs: The solutions to ax^2 + bx + c = 0, floats    

    root_1 = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
    root_2 = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)

    if isinstance(root_1, complex) or isinstance(root_2, complex):
        return(root_1, root_2)

    else:
        return(round(root_1, 4), round(root_2, 4))


def constant_solver(c):
#   Desc: Solves the constant equation a = 0 for x
#   Inputs: a (numerical)
#   Outputs: bool (True if a is zero; False otherwise)

    if c != 0:
        print('There is no solution.')

    else:
        print('Every complex number is a solution.')


def polynomial_solver(a, b, c):
#   Desc: Solves the quadratic equation ax^2 + bx + c = 0 for x
#   Inputs: a, b, and c (all numerical)
#   Outputs: (None)

# When a != 0, use quadratic solver
# When a = 0 !=b, use linear solver
# When a = 0 = b, use constant solver

    if a != 0:      
        res1, res2 = quadratic_solver(a, b, c)
        root_order(res1, res2)

    elif b != 0:   
        res = linear_solver(b, c)
        print("There is one solution: x = {:.4f}".format(res))

    else:                
        constant_solver(c)


x = get_inputs()
polynomial_solver(*x)