table = [
['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'],
['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']
]
G = [
['?', '?', '?', '?' ,'?' ,'?'],
['?', '?', '?', '?' ,'?' ,'?'],
['?', '?', '?', '?' ,'?' ,'?'],
['?', '?', '?', '?' ,'?' ,'?'],
['?', '?', '?', '?' ,'?' ,'?'],
['?', '?', '?', '?' ,'?' ,'?']
]
S = ['null', 'null', 'null', 'null', 'null', 'null'] 
for i in range(4):
    if table[i][6] == 'yes' and  S== ['null', 'null', 'null', 'null', 'null', 'null']:
        S = table[i][:6]
    elif table[i][6]== 'yes':
        s1 = table[i][:6]
        for j in range(6):
            if S[j] != s1[j]:
                S[j]='?'
    else:
        for j in range(6):
            if table[i][j]!= S[j]:
                for k in range(6):
                    if G[k] ==['?', '?', '?', '?' ,'?' ,'?']:
                        G[k][j] = S[j]
                        break;
for i in range(6):
    for j in range(6):
        if G[i][j] not in S and G[i][j] !='?':
            G[i][j]='?'
print("The General Hypothesis is:")
for i in range(6):
    if G[i] != ['?', '?', '?', '?', '?', '?']:
        print(G[i])
print("The specific Hypothesis:")
print(S)

# output:
# The General Hypothesis is:
# ['sunny', '?', '?', '?', '?', '?']
# ['?', 'warm', '?', '?', '?', '?']
# The specific Hypothesis:
# ['sunny', 'warm', '?', 'strong', '?', '?']
