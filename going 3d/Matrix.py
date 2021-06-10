class Matrix():
    def __init__(self,matrix=None,m=0,n=0):
        self.Matrix=[]
        if matrix==None:
            if m>0 and n>0:
                for _ in range(m):
                    temp=[]
                    for _ in range(n):
                        temp.append(0)
                    self.matrix.append(temp)
                self.m=m
                self.n=n
            else:
                raise ValueError('Recieved neither a matrix or matrix size')
        else:
            self.Matrix=matrix
            self.m=len(self.Matrix)
            self.n=len(self.Matrix[0])
    def __str__(self):
        value=""
        for x in self.Matrix:
            value+=" ".join(list(map(str,x)))+"\n"
        return value
    def __repr__(self):
        return(str("Matrix(matrix="+str(self.Matrix)+")"))
    def __sub__(self,other):
        if self.m == other.m and self.n == other.n:
            output=[]
            for x in range(self.m):
                temp=[]
                for y in range(self.n):
                    temp.append(self.Matrix[x][y]-other.Matrix[x][y])
                output.append(temp)
            return Matrix(output)
        else:
            raise IndexError('the two matricies are differnt sizes')
    def __add__(self,other):
        if self.m == other.m and self.n == other.n:
            output=[]
            for x in range(self.m):
                temp=[]
                for y in range(self.n):
                    temp.append(self.Matrix[x][y]+other.Matrix[x][y])
                output.append(temp)
            return Matrix(output)
        else:
            raise IndexError('the two matricies are differnt sizes')
    def tempMult(self,a,b):
        value=0
        for count in range(len(a)):
            value+=a[count]*b[count]
        return value
    def __mul__(self,other):
        if self.n == other.m:
            output=[]
            for x in range(self.m):
                temp=[]
                for y in range(other.n):
                    down=[]
                    for count in range(other.m):
                        down.append(other.Matrix[count][y])
                    temp.append(self.tempMult(self.Matrix[x],down))
                output.append(temp)
            return Matrix(output)
        else:
            raise IndexError('the two matricies are incorrect sizes')

