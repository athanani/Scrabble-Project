test = ["A", "B", "G"]
test1 = [1, 2, 3]
print(' '.join(str(test[i]) + ", " + str(test1[i]) for i in range(len(test1))))