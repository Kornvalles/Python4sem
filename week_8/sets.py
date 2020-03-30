thisset = {4,2,3,1}
otherset = {1,2,3,4,1,1}

print(type(thisset))

difset = thisset.symmetric_difference(otherset)

print(difset)

print(thisset == otherset)