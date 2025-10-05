from sklearn import tree

x = [
    [55, 160, 38],
    [62, 165, 40],
    [70, 170, 41],
    [80, 175, 43],
    [68, 172, 42],
    [90, 185, 45],
    [77, 178, 44],
    [50, 155, 36],
    [72, 169, 42],
    [85, 182, 44],
    [72, 172, 43],
    [48, 152, 35],
    [52, 158, 36],
    [60, 162, 38],
    [65, 168, 39],
    [74, 174, 42],
    [82, 180, 44],
    [95, 188, 46],
    [78, 176, 43],
    [85, 183, 45],
    [58, 161, 37],
    [63, 166, 39],
    [69, 170, 41],
    [73, 175, 42],
    [88, 186, 45],
    [92, 190, 47],
    [54, 159, 37],
    [49, 154, 35],
    [67, 169, 40],
    [71, 171, 41],
    [76, 177, 43],
    [81, 181, 44],
    [59, 163, 38],
    [64, 167, 39],
    [86, 184, 44],
    [93, 189, 46],
    [53, 157, 36],
    [47, 150, 34],
    [79, 179, 43],
    [83, 182, 44],
]

y = [
    'female', 'female', 'male', 'male', 'male', 'male', 'male', 'female', 'male', 'male', 'male',
    'female', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'male',
    'female', 'female', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'male',
    'male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male'
]
# Features: [weight (kg), height (cm), shoe size (EU)]
clf = tree.DecisionTreeClassifier()
clf.fit(x, y)

prediction = clf.predict([[60, 170, 40]])
print(prediction)  # should now say 'male'
