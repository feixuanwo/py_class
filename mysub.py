class P(object):
	def foo(self):
		print 'Hi, I am P-foo()'

class C(P):
	def foo(self):
		super(C, self).foo()
		print 'Hi, I am C-foo()'

c = C()
c.foo()

class C1(P):
	def foo(self):
		P.foo(self)
		print 'Hi, I am C1-foo()'

c1 = C1()
c1.foo()
