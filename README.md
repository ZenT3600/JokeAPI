# JokeAPI
A Python wrapper for "JokeAPI by Sv443"

---

# How To use:
```python
from jokes import Jokes
  
j = Jokes('Any') # Available categories: Programming, Miscellaneous, Dark, Any
print(j.get_jokes()) # Get Joke in string format
print(j.get_raw_joke()) # Get raw response
```
