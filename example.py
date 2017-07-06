from random_en_us_diff import RandomEnUsDiff

r = RandomEnUsDiff()

for i in range(0, 5):
    result = r.get()
    print("%s (en) <-> %s (us)" % (result['en'], result['us']))


# Or simply :

print( RandomEnUsDiff() )

