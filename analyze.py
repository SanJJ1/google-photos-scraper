import shelve
import pprint as pp


with shelve.open('data') as db:
    links = db['links2']
print(links[0])

for link in links:
    for attrib in link[1].split('\n'):
        if '.mp4' in attrib:
            print(attrib)



