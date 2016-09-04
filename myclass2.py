#!coding:UTF-8
class Time60(object):
	def __init__(self, hr, min):
		self.hr = hr
		self.min = min
	def __str__(self):
		return '%02d:%02d' % (self.hr, self.min)
	def __add__(self, other):
		return self.__class__(self.hr + other.hr, self.min + other.min)
	__repr__ = __str__
	def __iadd__(self, other): #原位加，修改原值未创建新对象
		self.hr += other.hr
		self.min += other.min
		return self

mon = Time60(10, 02)
tue = Time60(11, 01)
print mon
print id(mon) #通过內建函数id可以看出只是对原值进行了修改
mon += tue
print id(mon)
print mon
