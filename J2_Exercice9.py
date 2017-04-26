X = { "a", "b", "c", "d"}
Y = { "s", "b", "d"}

print(X,Y)
if "c" in X:
    print("c existe dans %s" % X)

if "a" in Y:
    print("a existe dans %s" % Y)
else:
    print("a n'existe pas dans %s" % Y)

print("X-Y : %s" % (X.difference(Y)))
print("Y-X : %s" % (Y.difference(X)))
print("X U Y : %s" % (X.union(Y)))
print("X intersection Y : %s" % (X.intersection(Y)))