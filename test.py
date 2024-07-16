s='"a.b"ccc"'
import re

r=re.findall('^".*?"',s)
print(r)