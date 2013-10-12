import cPickle as pickle
# a1 = ['this is a string', 42, [1, 2, 3], None]
# print repr(a1)
# with open('temp.pkl', 'w') as f1:
# 	pickle.dump(a1, f1, True)
# with open('temp.pkl') as f2:
# 	print repr(pickle.load(f2))
# a1.pop(0)
# print repr(a1)
# with open('temp.pkl', 'w') as f1:
# 	pickle.dump(a1, f1, True)
# with open('temp.pkl') as f2:
# 	print repr(pickle.load(f2))
# a3 = ('this is not a string', 42, [1, 2, 3], None)
# with open('temp.pkl', 'w') as f3:
# 	pickle.dump(a3, f1, True)
# print repr(a3)
# with open('temp.pkl') as f4:
# 	print repr(pickle.load(f4))
a1 = []

with open('temp2.pkl') as f2:
	print type(f2)
	
# 	a1 = pickle.load(f2)

# a1.append(u'i am ok')

# with open('temp2.pkl', 'w') as f1:
# 	pickle.dump(a1, f1, True)

# with open('temp2.pkl') as f3:
# 	a1 = pickle.load(f3)
# print a1