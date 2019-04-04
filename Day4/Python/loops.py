#!/usr/bin/python

name = 'Steve Jobs'

print ('Length of name', len(name) )

length = len(name)

index = 0
while ( index < length ):
   print ( name[index] )
   index = index + 1

for c in name:
    print (c )

print ( name[:3] )
print ( name[3:] )
