# Case Insensitive replace() for Python
Case insensitive string replace() alternative for Python 3.

Does not use regex in order to prevent ReDoS attacks.

* https://en.m.wikipedia.org/wiki/ReDoS
* https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS

## Example

```python
from replace_ci import *
result = replace_ci("Why am I not in the StAnDard LIBRarY?", "standard library", "string library")
print(result)
# Why am I not in the string library?
```

## License

Public domain.
