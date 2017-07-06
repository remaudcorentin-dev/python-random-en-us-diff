# python-random-en-us-diff

##### v1.0.0


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