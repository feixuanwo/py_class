class Singleton(object):
	_singletons = {}
	def __new__(cls, *args, **kwds):
		if not cls._singletons.has_key(cls):
			cls._singletons[cls] = object.__new__(cls)
		return cls._singletons[cls]

a = Singleton()
b = Singleton()
print a
print b
