import glob

def Count (f1):
    count = 0
    for line in open(f1):
    
        if not line.startswith('#'):
            count += 1
    
    print(f'ο αριθμος των γραμμων στο {f1} ειναι {count}')



f1 = 'C:/Users/Georg/AppData/Local/Programs/Python/Python37-32/Lib/idlelib/*.py'
entries = glob.glob(f1)

for entry in entries:
    Count(entry)
