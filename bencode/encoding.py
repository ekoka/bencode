"""
Integers:
- integer is encoded as i<base ten int>e. 
- Leading zeros are not allowed (although the number zero is still represented as "0").
- Negative values are encoded by prefixing the number with a hyphen-minus. 
    e.g.: 
        - The number 42 would thus be encoded as i42e
        - 0 as i0e 
        - -42 as i-42e. 
        - Negative zero is not permitted.

Byte strings:
- byte string (a sequence of bytes) encoded as <length>:<contents>. 
- The length is encoded in base 10, like integers, but must be non-negative (zero is allowed)
- contents are just the bytes that make up the string.
- The string "spam" would be encoded as 4:spam.
- The specification does not deal with encoding of characters outside the ASCII set;
- to mitigate this, some BitTorrent applications explicitly communicate the encoding (most commonly UTF-8) in various non-standard ways.
- This is identical to how netstrings work, except that netstrings additionally append a comma suffix after the byte sequence.

Lists:
- list of values is encoded as l<contents>e . 
- The contents consist of the bencoded elements of the list, in order, concatenated.
- A list consisting of the string "spam" and the number 42 would be encoded as: l4:spami42ee.
- Note the absence of separators between elements
- the first character is the letter 'l', not digit '1'.

Dictionaries:
- A dictionary is encoded as d<contents>e.
- The elements of the dictionary are encoded each key immediately followed by its value.
- All keys must be byte strings and must appear in lexicographical order.
- the dict {"bar": "spam", "foo": 42} would be encoded as d3:bar4:spam3:fooi42ee.
"""
