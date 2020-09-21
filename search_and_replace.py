import re


def Replace(f1, s1, s2):
    with open(f1) as f:
        fData = f.read()
        (NewData, Count) = re.subn(s1+r'(\W.*)', s2+r'\1', fData)
    if Count:
        f = open('Νεο_' + f1, 'w')
        f.write(NewData)
        f.close()

    print(f'βρηκα {Count} εμφανιστικε στο '+s1)


filename = input('Δωσε το ονομα του αρχειου: ')
word = input('δωσε την λεξη που ψαχνεις: ')
wordR = input('δωσε την λεξη που θα την αντικαταστησειι: ')

Replace(filename, word, wordR)
