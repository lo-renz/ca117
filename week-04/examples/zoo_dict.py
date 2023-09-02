#!/usr/bin/env python3

zoo = { 'snakes' : 20,
 'hippos' : 2,
 'tarantulas' : 15,
 'zebras' : 7 }

def tagger(item):
   item[0]

# increasing key order
for k, v in sorted(zoo.items()):
   print(f'{k} ---> {v}')

# decreasing key order
for k, v in sorted(zoo.items(), reverse=True):
   print(f'{k} ---> {v}')

def tagger(item):
   return item[1]

# increasing value order
for k, v in sorted(zoo.items(), key=tagger):
   print(f'{k} ---> {v}')

def tagger(item):
   return item[1]

# decreasing value order
for k, v in sorted(zoo.items(), key=tagger, reverse=True):
   print(f'{k} ---> {v}')

print(zoo.values())
print(max(zoo.values()))
print(str(max(zoo.values())))
max_v_width = print(len(str(max(zoo.values()))))
print(max_v_width)
# gives us the number of characters in the widest thing

print(zoo.keys())
print(max(zoo.keys()))
max_k_width = len(max(zoo.keys(), key=len))
print(max_k_width)


for k, v in sorted(zoo.items()):
    print(f'{k:>{max_k_width}s} ---> {v:>{max_v_width}d}')
