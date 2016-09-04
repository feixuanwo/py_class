

class Abase(object):
	@classmethod
	def mymethod(cls):
		print 'a class method for', cls.__name__

class Bclass(Abase):
	pass

a = Abase()
b = Bclass()
Abase.mymethod()
a.mymethod()
Bclass.mymethod()
b.mymethod()
