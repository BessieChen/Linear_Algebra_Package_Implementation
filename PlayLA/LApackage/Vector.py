import math

class Vector:

    def __init__(self, list):
        self._values = list

    def __repr__(self):#represent, 系统调用
        return "Vector({})".format(self._values)

    def __str__(self):#string，用户调用:例如用print(vec)
        return "({})".format(", ".join(str(e) for e in self._values))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values[item]

    def __add__(self, other):#TODO: 这里的add是两个vec相加，而不是vec和int相加
        assert len(self) == len(other), \
            "Error in adding, length of vectors must be same." #TODO: 这里不是assert len(self._values) == len(other._values)
        #return Vector([a + b] for a,b in zip(self._values, other._values))
        #上面方案不是很好，因为other._values是私有的， 但是python不存在绝对的私有，但是命名为_是希望不要触碰
        #所以更好的方法：
        return Vector([a + b for a,b in zip(self, other)])

    def __sub__(self, other):#TODO: 这里的sub是两个vec相减，而不是vec和int相减
        assert len(self) == len(other), "Error in subtracting, length of vectors must be same."
        return Vector([a - b for a,b in zip(self, other)])

    def __mul__(self, k):#TODO: self * k
        return Vector([ k * e for e in self])

    def __rmul__(self, k): #TODO: rmul()是指数量乘法 k * vec, 也就是vec在右边
        return self * k #TODO:这里的*不是一般的*，而是引用了上面的def __mul__(self, k)

    def __pos__(self):
        return self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__() #因为列表本身有迭代器

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        return math.sqrt(sum(e**2 for e in self))

    def __truediv__(self, k):#TODO:这个是魔法函数。有div：整数除法， truediv: 普通除法（数量除法）：self / k
        return (1 / k) * self#TODO:这里的/是普通的/, 但是这里的*表示的是Vector类的乘法__mul__()


    def normalize(self):
        if self.norm() < EPSILON:#TODO: 浮点数不要用==判断，因为精度不一样,不能写成self.norm() == 0
            #EPSILON如果定义在
            raise ZeroDivisionError("Normalize error! norm is zero.")
        #return Vector([ e / self.norm() for e in self]) #TODO:这里重复计算了self.norm(),所以改成下面这一句
        #return 1 / self.norm() * Vector(self._values)
        return Vector(self._values) / self.norm()  #TODO：这个在没有定义def __truediv__(self, k)之前会报错。

