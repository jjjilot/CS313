import glob, os, importlib, json, pprint
import lab0 as module


class BadInt(int):
    pass

class Lab0Tester():
    """ Simple testing class for lab 1 """

    def __init__(self):
        """ Constructor for the class"""
        self.unitTestResults = ""
        self.score = 0


    def open(self, opt):
        msg = " Unit Testing Results (Complex) "
        ln = (78 - len(msg))//2
        self.unitTestResults += "#="+("="*ln)+msg+("="*ln)+"\n"

    def close(self):
        msg = " End of Testing "
        ln = (78 - len(msg))//2
        self.unitTestResults += "#="+("="*ln)+msg+("="*ln)+"\n"
        self.unitTestResults += 'Total: {}/100'.format(self.score)

    def testComplex(self):
        """ Runs the test on the students codes """
        self.open(True)

        #Test-01: Constructor Validation
        self.test_initValid(module)

        #test-02: str validation
        self.test_strValid(module)

        #test-03: add validation
        self.test_addValid(module)

        #test-04: sub validation
        self.test_subValid(module)

        #test-05: mult validation
        self.test_mulValid(module)

        #test-06: div validation
        self.test_divValid(module)

        self.close()

        return True

    def test_initValid(self, module):
        """ Test-01: Constructor Validation """
        output = "# Test-01: Valid Constructor Implementation - "
        error = ""
        N = None
        verdict = True

        try:
            N = module.Complex(6, 2)
        except Exception as e:
            error += "#    ERROR: Crashed on declaring a new complex number.\n"
            error += "#    "+str(e)+"\n"
            verdict = False

        if(verdict):
            try:
                assert N.a == 6
            except:
                error += "#    ERROR: Either self.a does not exist or was not set correctly."
                verdict = False

        if(verdict):
            try:
                assert N.b == 2
            except:
                error += "#    ERROR: Either self.b does not exist or was not set correctly."
                verdict = False

        if(verdict):
            self.score += 18
            output += "PASS [18/18]\n"
            self.unitTestResults += output
        else:
            output += "FAIL [0/18]\n"
            self.unitTestResults += output
            self.unitTestResults += error
        return verdict

    def test_strValid(self, module):
        output = "# Test-02: Valid __str__ Implementation - "
        error = ""
        N = None
        verdict = True

        try:
            N1 = module.Complex(3, 2)
        except Exception as e:
            error += "#    ERROR: Crashed on declaring a new complex number.\n"
            error += "#    "+str(e)+"\n"
            verdict = False

        msg = None
        msg2 = None
        if(verdict):
            try:
                msg = N1.__str__()
                msg2 = str(N1)
            except Exception as e:
                error += "#    ERROR: Crashed on call to __str__\n"
                error += "#    "+str(e)
                verdict = False

        if(verdict):
            try:
                control = "(3 + 2i)"
                assert msg == msg2
                assert msg == control
            except:
                error += "#    ERROR: The format of the str method does not comply\n"
                error += "#    with specifications.\n"
                error += "#    Expected: (3 + 2i)\n"
                error += "#    Got: "+msg+"\n"
                verdict = False

        if(verdict):
            self.score += 10
            output += "PASS [10/10]\n"
            self.unitTestResults += output
        else:
            output += "FAIL [0/10]\n"
            self.unitTestResults += output
            self.unitTestResults += error
        return verdict

    def test_addValid(self, module):
        output = "# Test-03: Valid __add__ Implementation - "
        error = ""
        N1 = None
        N2 = None
        verdict = True

        try:
            I1 = module.Complex(3, 2)
            I2 = module.Complex(2, 3)
            F1 = module.Complex(3.1, 2.6)
            F2 = module.Complex(6.2, 7.8)
        except Exception as e:
            error += "#    ERROR: Crashed on declaring a new complex number.\n"
            error += "#    "+str(e)+"\n"
            verdict = False

        I3 = None
        F3 = None
        if(verdict):
            try:
                I3 = I1 + I2
            except Exception as e:
                error += "#     ERROR: Crashed on addition of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                F3 = F1 + F2
            except Exception as e:
                error += "#     ERROR: Crashed on addition of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                assert I3.a == 5
                assert I3.b == 5
                assert round(F3.a, 2) == 9.3
                assert round(F3.b, 2) == 10.4
            except Exception as e:
                error += "#     ERROR: Failed assertion test for correct output.\n"
                error += "#     Expected: (5 + 5i) = (3 + 2i) + (2 + 3i)\n"
                error += "#     Got: ("+str(I3.a)+" + "+str(I3.b)+"i)\n"
                error += "#     Expected: (9.3 + 10.4i) = (3.1 + 2.6i) + (6.2 + 7.8i)\n"
                error += "#     Got: ("+str(F3.a)+" + "+str(F3.b)+"i)\n"
                verdict = False

        if(verdict):
            self.score += 18
            output += "PASS [18/18]\n"
            self.unitTestResults += output
        else:
            output += "FAIL [0/18]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_subValid(self, module):
        output = "# Test-04: Valid __sub__ Implementation - "
        error = ""
        verdict = True

        try:
            I1 = module.Complex(3, 2)
            I2 = module.Complex(2, 3)
            F1 = module.Complex(3.1, 2.6)
            F2 = module.Complex(6.2, 7.8)
        except Exception as e:
            error += "#    ERROR: Crashed on declaring a new complex number.\n"
            error += "#    "+str(e)+"\n"
            verdict = False

        I3 = None
        F3 = None
        if(verdict):
            try:
                I3 = I1 - I2
            except Exception as e:
                error += "#     ERROR: Crashed on subtraction of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                F3 = F1 - F2
            except Exception as e:
                error += "#     ERROR: Crashed on subtraction of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                assert I3.a == 1
                assert I3.b == -1
                assert round(F3.a, 2) == -3.1
                assert round(F3.b, 2) == -5.2
            except Exception as e:
                error += "#     ERROR: Failed assertion test for correct output.\n"
                error += "#     Expected: (1 + -1i) = (3 + 2i) - (2 + 3i)\n"
                error += "#     Got: ("+str(I3.a)+" + "+str(I3.b)+"i)\n"
                error += "#     Expected: (-3.1 + -5.2i) = (3.1 + 2.6i) - (6.2 + 7.8i)\n"
                error += "#     Got: ("+str(F3.a)+" + "+str(F3.b)+"i)\n"
                verdict = False

        if(verdict):
            self.score += 18
            output += "PASS [18/18]\n"
            self.unitTestResults += output
        else:
            output += "FAIL [0/18]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_mulValid(self, module):
        output = "# Test-05: Valid __mul__ Implementation - "
        error = ""
        verdict = True

        try:
            I1 = module.Complex(3, 2)
            I2 = module.Complex(2, 3)
            F1 = module.Complex(3.1, 2.6)
            F2 = module.Complex(6.2, 7.8)
        except Exception as e:
            error += "#    ERROR: Crashed on declaring a new complex number.\n"
            error += "#    "+str(e)+"\n"
            verdict = False

        I3 = None
        F3 = None
        if(verdict):
            try:
                I3 = I1 * I2
            except Exception as e:
                error += "#     ERROR: Crashed on multiplication of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                F3 = F1 * F2
            except Exception as e:
                error += "#     ERROR: Crashed on multiplication of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                assert I3.a == 0
                assert I3.b == 13
                assert round(F3.a, 2) == -1.06
                assert round(F3.b, 2) == 40.3
            except Exception as e:
                error += "#     ERROR: Failed assertion test for correct output.\n"
                error += "#     Expected: (0 + 13i) = (3 + 2i) * (2 + 3i)\n"
                error += "#     Got: ("+str(I3.a)+" + "+str(I3.b)+"i)\n"
                error += "#     Expected: (-1.06 + 40.3i) = (3.1 + 2.6i) * (6.2 + 7.8i)\n"
                error += "#     Got: ("+str(F3.a)+" + "+str(F3.b)+"i)\n"
                verdict = False

        if(verdict):
            self.score += 18
            output += "PASS [18/18]\n"
            self.unitTestResults += output
        else:
            output += "FAIL [0/18]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_divValid(self, module):
        output = "# Test-06: Valid __trudiv__ Implementation - "
        error = ""
        verdict = True

        try:
            I1 = module.Complex(3, 2)
            I2 = module.Complex(2, 3)
            F1 = module.Complex(3.1, 2.6)
            F2 = module.Complex(6.2, 7.8)
        except Exception as e:
            error += "#    ERROR: Crashed on declaring a new complex number.\n"
            error += "#    "+str(e)+"\n"
            verdict = False

        I3 = None
        F3 = None
        if(verdict):
            try:
                I3 = I1 / I2
                assert type(I3) == module.Complex
            except Exception as e:
                error += "#     ERROR: Crashed on division of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                F3 = F1 / F2
                assert type(F3) == module.Complex
            except Exception as e:
                error += "#     ERROR: Crashed on division of two valid complex numbers.\n"
                error += "#     "+str(e)+"\n"
                verdict = False

        if(verdict):
            try:
                assert round(I3.a, 2) == 0.92
                assert round(I3.b, 2) == -0.38
                assert round(F3.a, 3) == 0.398
                assert round(F3.b, 3) == -0.081
            except Exception as e:
                error += "#     ERROR: Failed assertion test for correct output.\n"
                error += "#     Expected: (0.92 + -0.38i) = (3 + 2i) / (2 + 3i)\n"
                error += "#     Got: ("+str(I3.a)+" + "+str(I3.b)+"i)\n"
                error += "#     Expected: (0.398 + -0.081i) = (3.1 + 2.6i) / (6.2 + 7.8i)\n"
                error += "#     Got: ("+str(round(F3.a, 3))+" + "+str(round(F3.b, 3))+"i)\n"
                verdict = False

        if(verdict):
            self.score += 18
            output += "PASS [18/18]\n"
            self.unitTestResults += output
        else:
            output += "FAIL [0/18]\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_initInvalid(self, module):
        """ Test-01: Constructor Validation """
        output = "# Corner Case Set - 01: Constructor invalid input - "
        error = ""
        N = None
        verdict = True

        if(verdict):
            try:
                module.ComplexConstructorTypeERROR
            except:
                error += "#    ERROR: Could not find required exception - ComplexConstructorTypeERROR"
                verdict = False

        if(verdict):
            try:
                N = module.Complex(None, 2)
                raise Exception("Failed corner case 1\n")
            except module.ComplexConstructorTypeERROR:
                pass
            except Exception as e:
                error += "#    ERROR: Either raised the wrong exception or did not raise an exception on invalid 'a'.\n"
                verdict = False

        if(verdict):
            try:
                N = module.Complex(2, None)
                raise Exception("Failed corner case 1\n")
            except module.ComplexConstructorTypeERROR:
                pass
            except Exception as e:
                error += "#    ERROR: Either raised the wrong exception or did not raise an exception on invalid 'b'.\n"
                verdict = False

        if(verdict):
            try:
                N = module.Complex(None, None)
                raise Exception("Failed corner case 1\n")
            except module.ComplexConstructorTypeERROR:
                pass
            except Exception as e:
                error += "#    ERROR: Either raised the wrong exception or did not raise an exception on invalid input.\n"
                verdict = False

        if(verdict):
            try:
                N = module.Complex(BadInt(1), BadInt(2))
                raise Exception
            except module.ComplexConstructorTypeERROR:
                pass
            except:
                error += "#    ERROR: Failed explicit type checking. Did you use isinstance()?\n"
                verdict = False

        if(verdict):
            output += "PASS\n"
            self.unitTestResults += output
        else:
            output += "FAIL\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_invalidAdd(self, module):
        output = "# Corner Case Set - 02: invalid add input - "
        error = ""
        N = None
        verdict = True

        if(verdict):
            try:
                N1 = module.Complex(1,1)
                N2 = (1, 1)
                N3 = N1 + N2
            except TypeError:
                pass
            except:
                error += "#    ERROR: Either raised the wrong exception or did not raise an exception on invalid input.\n"
                verdict = False

        if(verdict):
            output += "PASS\n"
            self.unitTestResults += output
        else:
            output += "FAIL\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_invalidSub(self, module):
        output = "# Corner Case Set - 03: invalid sub input - "
        error = ""
        N = None
        verdict = True

        if(verdict):
            try:
                N1 = module.Complex(1,1)
                N2 = (1, 1)
                N3 = N1 - N2
            except TypeError:
                pass
            except:
                error += "#    ERROR: Either raised the wrong exception or did not raise an exception on invalid input.\n"
                verdict = False

        if(verdict):
            output += "PASS\n"
            self.unitTestResults += output
        else:
            output += "FAIL\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_invalidMul(self, module):
        output = "# Corner Case Set - 03: invalid mul input - "
        error = ""
        N = None
        verdict = True

        if(verdict):
            try:
                N1 = module.Complex(1,1)
                N2 = (1, 1)
                N3 = N1 * N2
            except TypeError:
                pass
            except:
                error += "#    ERROR: Either raised the wrong exception or did not raise an exception on invalid input.\n"
                verdict = False

        if(verdict):
            output += "PASS\n"
            self.unitTestResults += output
        else:
            output += "FAIL\n"
            self.unitTestResults += output
            self.unitTestResults += error

    def test_invalidDiv(self, module):
        output = "# Corner Case Set - 04: invalid div input - "
        error = ""
        N = None
        verdict = True

        if(verdict):
            try:
                N1 = module.Complex(1,1)
                N2 = (1, 1)
                N3 = N1 / N2
            except TypeError:
                pass
            except:
                error += "#    ERROR: Either raised the wrong exception or did not raise an exception on invalid input.\n"
                verdict = False

        if(verdict):
            output += "PASS\n"
            self.unitTestResults += output
        else:
            output += "FAIL\n"
            self.unitTestResults += output
            self.unitTestResults += error

if __name__ == "__main__":
    test = Lab0Tester()
    test.testComplex()
    print(test.unitTestResults)
