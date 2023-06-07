table = [
['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'],
['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']
]
hypothesis= ['null', 'null', 'null', 'null','null', 'null']
h1= ['null', 'null', 'null', 'null','null', 'null']
for i in range(4):
    if table[i][6]== 'yes' and hypothesis == ['null', 'null', 'null', 'null','null', 'null']:
        hypothesis =table[i][:6]
    elif table[i][6] == 'yes':
        h1= table[i][:6]
        for j in range(6):
            if hypothesis[j]!= h1[j]:
                hypothesis[j] ='?'
print(hypothesis)
