class P(object):
	def __init__ (self):
		print "calling P's constructor"
	def foo(self):
		print "parent test"

class C(P):
	def __init__ (self):
		print "calling C's constructor"

c = C()
print C.__bases__
print c.__class__.__name__

class C1(P):
	def __init__ (self):
		print '================='
		P.__init__(self)
		super(C1, self).__init__()
		print "calling C1's constructor"
	def foo(self):
		super(C1, self).foo()
		print "child test"

c1 = C1()
c1.foo()

print c.__class__
print C.__bases__
print C.__dict__
print C.__doc__
print dir(C)
