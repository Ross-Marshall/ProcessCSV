# [{'fawn': 'bird', 'sermersheim': 'Mr Myer', 'sonji': 'Bonji', 'scheuring': 'Taste'}]

dicts_from_file = []
with open('myfile.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval(line))   

d = dicts_from_file[0]
for tup in d:
    print 'Key ----> ' + str(tup) + ' value -----> ' + str( d[tup] )
