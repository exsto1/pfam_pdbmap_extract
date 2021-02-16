file = open('pdbmap').readlines()
file = [i.rstrip().split(';') for i in file]


def by_pfam_id(id):
    result = []
    used =[]
    for i in range(len(file)):
        if file[i][3].strip() == id:
            if file[i][0].strip() not in used:
                used.append(file[i][0].strip())
                result.append([id, file[i][0].strip(), file[i][1].strip()])
    return result


to_search=['PF01402', 'PF01381', 'PF13443']
res = []
for i in to_search:
    res.extend(by_pfam_id(i))

for i in res:
    print(i)