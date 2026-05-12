def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.num == f2.num) and (f1.den == f2.den)

def CriaMista(f):
    part_int = 0
    while f.num // f.den != 0:
        f.num = f.num - f.den
        part_int += 1
    fm = FracaoMista(part_int, f)
    return fm


class Fracao():
    
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def den(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.den + self.__den * outraFrac.num
        novoDen = self.__den * outraFrac.den
        divComum = mdc(novoNum, novoDen)
        return Fracao(novoNum//divComum, novoDen//divComum)  

class FracaoMista():
    def __init__(self, inteira, frac):
        self.__inteira = inteira
        self.__frac = frac  

    def __str__(self):
        return str(self.__inteira) + " " +  str(self.__frac)

    @property
    def inteira(self):
        return self.__inteira
    
    @property
    def frac(self):
        return self.__frac


if __name__ == "__main__":
    frac1 = Fracao (1, 4) 
    frac2 = Fracao(1, 6)
    frac3 = frac1 + frac2
    print(frac3)
    if frac3.num/frac3.den > 1:
        fracm3 = CriaMista(frac3)
        print("Forma Mista: {}".format(fracm3))
    print()
    frac1 = Fracao (3, 4)
    frac2 = Fracao(14, 6)
    frac3 = frac1 + frac2
    print(frac3)

    if frac3.num/frac3.den > 1:
        fracm3 = CriaMista(frac3)
        print("Forma Mista: {}".format(fracm3))