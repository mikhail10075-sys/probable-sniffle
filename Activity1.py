import array as arr

set1 = {'apple', 'orange', 'plum', 'dragonfruit'}
set2 = {'banana', 'plum', 'starfruit','orange'}

set1.add('Pear')
print(set1)

print(set1.intersection(set2))

x = arr.array('i', [7, 10, 12, 5])
print(x)

x.insert(0,1)
x.insert(2,12)
print(x)
x.append(12)
print(x)

print("12 appears this many times in the array - ",x.count(12))

(x.reverse())
print(x)