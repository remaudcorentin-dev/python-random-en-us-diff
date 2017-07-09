# python-random-en-us-diff

##### v1.0.1

Cool simple Python module to get random difference between American and English languages.  
  
##### Isn't life so beautiful ?
  
    
### Installation

`pip install python-random-en-us-diff`


### Usage

```python

from random_en_us_diff import RandomEnUsDiff

r = RandomEnUsDiff()

for i in range(0, 5):
    result = r.get()
    print("%s <-> %s" % (result['en'], result['us']))

```

Or simply :

```python

>>> from random_en_us_diff import RandomEnUsDiff
>>> print( RandomEnUsDiff() )

```

(Note : 'US' & 'EN' are reversed...)
