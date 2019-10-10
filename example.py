from bencode.decoding import decode

contents = b'd3:foo3:bar1:ai22e1:cli33e3:bazeel3:abci9ee'
data = decode(contents)
expected = [{
    b'foo': b'bar', 
    b'a':22, 
    b'c': [
        33, 
        b'baz'
    ]}, 
    [
        b'abc', 
        9
    ]
]
assert expected==data
print(data)
