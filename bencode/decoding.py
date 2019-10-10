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

def decode(data):
    # the parser will use the final 'e' to return the data
    return parse(data + b'e')

def parse(bytedata, index=-1):
    context = []
    while True:
        index += 1

        if bytedata[index]==ord(b'e'):
            # closing a context
            return context, index

        # handle int
        if bytedata[index]==ord(b'i'):
            data, index = decode_integer(bytedata, index)
            context.append(data)
            continue

        # handle list
        if bytedata[index]==ord(b'l'):
            data, index = decode_list(bytedata, index)
            context.append(data)
            continue

        # handle dict 
        if bytedata[index]==ord(b'd'):
            data, index = decode_dictionary(bytedata, index+1)
            context.append(data)
            continue

        # handle byte
        data, index = decode_bytestring(bytedata, index)
        context.append(data)


def decode_integer(data, start):
    end = start+1
    # TODO: handle malformed data 
    # - empty integer
    # - containers without ending
    # - non integer value
    while True:
        if data[end]==ord(b'e'):
            return int(data[start+1:end]), end
        end += 1

def decode_bytestring(data, index):
    length = 0
    while True:
        length = length * 10 + int(chr(data[index]))
        index += 1
        if data[index]==ord(b':'):
            break
    index += 1
    return data[index: index+length], index+length-1

def decode_list(bytedata, index):
    context, index = parse(bytedata, index)
    return context, index

def decode_dictionary(bytedata, index):
    context, index = parse(bytedata, index)
    data = {}
    for i in range(0, len(context), 2):
        key = context[i]
        value = context[i+1]
        data[key] = value
    return data, index
