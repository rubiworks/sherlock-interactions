from os import walk
import jstyleson, json
import re

filenames = next(walk('.'), (None, None, []))[2]  # [] if no file

dic = {}

for file in filenames:
    with open(file, 'r') as f:
        if file[-6:] != '.jsonc' or '_schema' in file or '_meta' in file: continue
        s = f.read().replace('\n', '')
        pattern = '(".*?":?)'
        x = re.finditer(pattern, s)
        for y in x:
            z = y.group(0)
            if ":" in z:
                r = z[1:-2]
                v = dic.get(r, 0)
                dic[r] = v + 1

    with open(file, 'r') as f:
        # check for mandatory keys
        j = jstyleson.load(f)
        c_s = j['component-type']

print(dic.keys())