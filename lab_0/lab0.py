# ------------------------------ Exceptions -------------------------------------
class UndocumentedError(Exception):
    """

    """
    pass


class ComplexConstructorTypeError(Exception):
    """
    An exception raised when trying to build a complex number incorrectly.
    """
    pass


# -------------------------------------------------------------------------------

# ------------------------------- Classes ---------------------------------------
class Complex:
    """ Description: The complex number class. Creates a complex number of the
                     form (a+bi). Includes methods to perform mathematical
                     operations.
    """

    def __init__(self, a=0, b=0):
        """ Description: The constructor for the Complex number class.
            Parameters:
                       1. a (the a part of the complex number a+bi)
                       2. b (the b part of the complex number a+bi)
                    The default value is 0 since 0 has a complex representation
                    of 0+0i.
        """

        if ((type(a) != int) and (type(a) != float)):
            raise ComplexConstructorTypeError("ERROR: The 'a' part of a " + \
                                              "complex number must be a float or an int.")
        elif ((type(b) != int) and (type(b) != float)):
            raise ComplexConstructorTypeError("ERROR: The 'b' part of a " + \
                                              "complex number must be a float or an int.")

        ###### YOUR CODE STARTS HERE ######
        self.a = a
        self.b = b

    def __str__(self):
        """ Returns a string representation of the complex number.
            Format: "(a + bi)"
        """
        ###### YOUR CODE STARTS HERE ######
        template = "({} + {}i)"
        return template.format(self.a, self.b)

    def __add__(self, other):
        """ Description: Adds two complex numbers togeather.
            Usage: number3 = number1 + number2
                    number3 = number1.__add__(number2)
            Return: Returns a complex number containing the summation.
        """
        returnValue = None
        if (type(other) != Complex):  # simple type check
            raise TypeError("ERROR: The other number is the wrong type.")
        ###### YOUR CODE STARTS HERE ######
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        
        return Complex(a+c, b+d)

    def __sub__(self, other):
        """ Description: subtracts one complex number from the other.
            Format: number3 = number1 - number2
                    number3 = number1.__sub__(number2)
        """
        returnValue = None
        if (type(other) != Complex):  # simple type check
            raise TypeError("ERROR: The other number is the wrong type.")
        ###### YOUR CODE STARTS HERE ######
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        
        return Complex(a-c, b-d)

    def __mul__(self, other):
        """ Description: Multiplies one complex number by another.
            Format: number3 = number1 * number2
                    number3 = number1.__mul__(number2)
        """
        returnValue = None
        if (type(other) != Complex):  # simple type check
            raise TypeError("ERROR: The other number is the wrong type.")
        ###### YOUR CODE STARTS HERE ######
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        
        return Complex(a*c-b*d, a*d+b*c)

    def __truediv__(self, other):
        """ Description: subtracts one complex number from the other.
            Format: number3 = number1 / number2
                    number3 = number1.__div__(number2)
        """
        returnValue = None
        if (type(other) != Complex):  # simple type check
            raise TypeError("ERROR: The other number is the wrong type.")
        elif other.a == 0 and other.b == 0:
            raise UndocumentedError('ERROR: Division by zero')
        ###### YOUR CODE STARTS HERE ######
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        
        return Complex((a*c+b*d)/(c**2+d**2), (b*c-a*d)/(c**2+d**2))
