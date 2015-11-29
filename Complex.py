class Complex:
    """ represent and manipulate complex numbers """
    def __init__(self,x=0,y=0):
        """create a complex number """
        self.real = x
        self.imag = y

    def __str__(self):
        """ Pretty print complex number. """
        s = ""
        if self.real != 0:
            s+=str(self.real)
        if self.imag > 0 and self.imag !=1:
            if self.real == 0:
                s+="i"+str(self.imag)
            else:
                s+="+i"+str(self.imag)
        if self.imag < 0 and self.imag != -1:
            s+="-i"+str(-self.imag)
        if self.imag == 1:
            if self.real == 0:
                s+="i"
            else:
                s+="+i"
        if self.imag == -1:
            s+="-i"

        if self.real ==0 and self.imag==0:
            s+="0"

        return s

    def __add__(self,z):
        """ Add complex numbers using + """
        return Complex(self.real+z.real,self.imag+z.imag)

    def __sub__(self,z):
        """ Subtract complex numbers using - """
        return Complex(self.real-z.real,self.imag-z.imag)

    def __mul__(self,z):
        """ Multiply complex numbers using * """
        w1 = self.real
        w2 = self.imag
        z1 = z.real
        z2 = z.imag
        return Complex(w1*z1-w2*z2,w1*z2 + w2*z1)

    def __truediv__(self,z):
        """ Divide complex numbers using / """
        w1 = self.real
        w2 = self.imag
        z1 = z.real
        z2 = z.imag
        return Complex((w1*z1+w2*z2)/float(z1**2+z2**2),
                (w2*z1-w1*z2)/float(z1**2+z2**2))

    def __div__(self,z):
        """ Divide complex numbers using / """
        w1 = self.real
        w2 = self.imag
        z1 = z.real
        z2 = z.imag
        return Complex((w1*z1+w2*z2)/float(z1**2+z2**2),
                (w2*z1-w1*z2)/float(z1**2+z2**2))
    
    def __neg__(self):
        """ Negate complex number using - (e.g. -z) """
        return Complex(-self.real,-self.imag)

    def __eq__(self,z):
        """ Test for equality. """
        return (self.real == z.real) and (self.imag == z.imag)

    def __abs__(z):
        """ Compute the abs value of complex number using abs() function """
        return sqrt(z.real**2 + z.imag**2)

    def conjugate(self):
        """ Compute the complex conjugate of the complex number. """
        return Complex(self.real,-self.imag)
