``` bash
pip install .
head -c 100 /dev/urandom | python -m bytepype '("0x{:02x}\n".format(ord(c)) for c in _)'
```
where `_` is a generator yielding characters from stdin.
