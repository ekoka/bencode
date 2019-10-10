# Bencode decoder

A small utility function to decode bencoded data. It was built and tested with Python 3.6.7.

## How to

Import the `decoder` function from the `bencode.decoding` module and simply run it by passing a Python byte string that adhere to the bencode encoding format. The return value should be a Python list of values in native data types. Note that all string values are byte strings not unicode strings, that includes dictionary keys.

```python
from bencode.decoding import decode

contents = b'd3:foo3:bar1:ai22eel3:abci9ee'
data = decode(contents)
# [{b'foo': b'bar', b'a':22}, [b'abc', 9]]
```

## Errors

The `decode` function expects to receive data in byte string and will raise a `TypeError` if it receives an incompatible format instead (e.g. unicode).
A `ValueError` will be raised if the data is believed to be malformed.

## Tests

The util is bundled with a small function to run basic tests from the command line. To run, change to the project's parent directory:

    $ cd ~/projects/bencode

Verify that you're running Python 3.6+

    $ python --version
    Python 3.6.7

Call Python on the tests module 

    $ python -m bencode.tests
