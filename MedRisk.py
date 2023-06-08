train_data = [
    ['medium', 'skiing', 'design', 'single', 'twenties', 'no', 'highRisk'],
    ['high', 'golf', 'trading', 'married', 'forties', 'yes', 'lowRisk'],
    ['low', 'speedway', 'transport', 'married', 'thirties', 'yes', 'medRisk'],
    ['medium', 'football', 'banking', 'single', 'thirties', 'yes', 'lowRisk'],
    ['high', 'flying', 'media', 'married', 'fifties', 'yes', 'highRisk'],
    ['low', 'football', 'security', 'single', 'twenties', 'no', 'medRisk'],
    ['medium', 'golf', 'media', 'single', 'thirties', 'yes', 'medRisk'],
    ['medium', 'golf', 'transport', 'married', 'forties', 'yes', 'lowRisk'],
    ['high', 'skiing', 'banking', 'single', 'thirties', 'yes', 'highRisk'],
    ['low', 'golf', 'unemployed', 'married', 'forties', 'yes', 'highRisk']
]

num_golf = 0
for example in train_data:
    if example[1]== 'golf':
        num_golf +=1

print(num_golf/ len(train_data))
num_single_medrisk=0
for example in train_data:
    if example[3] == 'single' and example[6] == 'medRisk':
        num_single_medrisk +=1

num_medrisk=0
for example in train_data:
    if example[6] == 'medRisk':
        num_medrisk +=1

x = num_single_medrisk/num_medrisk
print(x)


#output:
#     0.4
# 0.6666666666666666
