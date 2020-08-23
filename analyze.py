import shelve

with shelve.open('data') as db:
    links = db['links']

sum = 0
anoms = []
# for i in links[-100:]:
#     print(i[1].split('\n'), i[0])
for i in links:
    s = False
    for j in i[1].split("\n"):
        if 'MB' in j or 'KB' in j or 'GB' in j:
            s = True
            x = j.split()
            try:
                if x[1] == 'KB':
                    sum += float(x[0])
                elif x[1] == 'MB':
                    sum += 1000 * float(x[0])
                elif x[1] == 'GB':
                    input(f'{x[0]} GB detected at {i}')
                else:
                    input(f'None detected at {i}')
            except:
                anoms.append(i)
    if not s:
        input(f'none detected at {i}')

        # else:
            #     input(f'None Detected at {i}')

print(sum)