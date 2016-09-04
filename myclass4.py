
class P(object):
	'P class'
	def __init__ (self):
		print 'P created an instance of', \
			self.__class__.__name__

class P1(object):
	'P1 class'
	def __init__ (self):
		print 'P1 created an instance of', \
			self.__class__.__name__
class C(P,P1):
	pass

p = P()
print p.__class__
print P.__bases__
print P.__doc__
c = C()
print c.__class__
print C.__bases__
print C.__doc__
