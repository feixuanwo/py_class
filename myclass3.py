class P(object):
	def __init__ (self):
		print "calling P's constructor"

class C(P):
	def __init__ (self):
		super(C, self).__init__() #通过super调用父类构造器
		print "calling C's constructor"

c = C()

class RoundFloat(float): 
	def __new__(cls, val): #覆盖父类float的__new__函数
		return float.__new__(cls, round(val, 2))

print RoundFloat(1.599)

class RoundFloat1(float):
	def __new__(cls, val):
		return super(RoundFloat1, cls).__new__(cls, round(val, 2))

print RoundFloat1(1.233)

class SortedKeyDict(dict):
	def keys(self):
		return sorted(super(SortedKeyDict, self).keys())

d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))

print 'By iterator:'.ljust(12), [key for key in d]
print 'By keys():'.ljust(12), d.keys()

print issubclass(SortedKeyDict, dict)
print issubclass(SortedKeyDict, object)
print isinstance(c, C)
print isinstance(c, object)
print isinstance(c, dict)

class myClass(object):
	def __init__(self):
		self.foo = 100

myInst = myClass()
print hasattr(myInst, 'foo')
print getattr(myInst, 'foo')
print hasattr(myInst, 'bar')
#print getattr(myInst, 'bar')
print getattr(myInst, 'bar', 'oops!')

print '--------------'
setattr(myInst, 'bar', 'my attr')
print hasattr(myInst, 'bar')
print dir(myInst)
print getattr(myInst, 'bar')
print myInst.bar
delattr(myInst, 'foo')
print dir(myInst)
print hasattr(myInst, 'foo')
print getattr(myInst, 'foo', 'oops!')


class RoundFloatManual(object):
	def __init__(self, val):
		assert isinstance(val, float),\
		"Value must be a float!"
		self.value = round(val, 2)
	def __str__(self):
		return '%.2f' % self.value
	__repr__ = __str__   #print调用(__str__),而不带print调用(__repr__)

#rfm = RoundFloatManual(5)
rfm = RoundFloatManual(1.654)
print rfm


class Time60(object):
	def __init__(self, hr, min):
		self.hr = hr
		self.min = min
	def __add__(self, other):
		return self.__class__(self.hr + other.hr, self.min + other.min)
	def __str__(self):
		return '%d:%d' % (self.hr, self.min)
	__repr__ = __str__

mon = Time60(10, 30)
tue = Time60(11, 35)
mon + tue
print mon + tue


