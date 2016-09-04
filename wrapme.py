#!coding:UTF-8
#包装后看可以使用对象的属性
class WrapMe(object):
	def __init__(self, obj):
		self.__data = obj
	def get(self):
		return self.__data
	def __repr__(self):
		#return 'self.__data'
		return str(self.__data)
	def __str__(self):
		return str(self.__data)
	def __getattr__(self, attr):
		return getattr(self.__data, attr)

wrappedComplex = WrapMe(3.5 + 4.2j)
wrappedComplex
print "==="
print wrappedComplex
print wrappedComplex.real
print wrappedComplex.imag
print wrappedComplex.conjugate()
print wrappedComplex.get()

print "==================="
wrappedList = WrapMe([123, 'foo', 45.67])
wrappedList.append('bar')
wrappedList.append(123)

print '---------'
wrappedList
print wrappedList
print '---------'
print wrappedList
print wrappedList.index(45.67)
print wrappedList.count(123)
print wrappedList.pop()
print wrappedList

#wrappedList[3]
print wrappedList.get()[3]
