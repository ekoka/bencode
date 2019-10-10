from .tinytest import run
from .decoding import (
    decode_integer,
    decode_dictionary,
    decode_bytestring,
    decode_list,
    parse,
    decode,
)

@run
def test_decode_integer_returns_value():
    inputval = b'abcdi43euje9'
    data, index = decode_integer(inputval, 4)
    assert data==43

@run
def test_decode_integer_returns_end_index():
    inputval = b'abcdi4833euje9'
    data, index = decode_integer(inputval, 4)
    assert index==9

@run
def test_decode_bytestrint_returns_value():
    inputval = b'abd12:abcdefghijklmnopqrstuvwxy'
    data, index = decode_bytestring(inputval, 3)
    assert data==b'abcdefghijkl'

@run
def test_decode_bytestrint_returns_end_index():
    inputval = b'abd12:abcdefghijklmnopqrstuvwxy'
    data, index = decode_bytestring(inputval, 3)
    assert index==17

@run
def test_parse_can_return_context_of_simple_values():
    inputval = b'3:abd2:ab2:cd1:ei54e3:fghi0e' + b'e'
    data, index = parse(inputval)
    assert data==[b'abd', b'ab', b'cd', b'e', 54, b'fgh', 0]

@run
def test_decode_list_can_return_nested_context_of_simple_values():
    inputval = b'abdll3:abd2:abe2:cd1:ei54e3:fghi0eexyz'
    data, index = decode_list(inputval, 3)
    assert data[0]==[b'abd', b'ab']

@run
def test_decode_list_returns_index_for_remainder():
    inputval = b'abdll3:abd2:abe2:cd1:ei54e3:fghi0eexyz'
    data, index = decode_list(inputval, 3)
    assert index==34
    assert inputval[index]==ord(b'e')
    assert inputval[index+1]==ord(b'x')

@run
def test_decode_dictionary_can_return_dict_of_simple_values():
    inputval = b'abd3:abd2:ab2:cd1:e2:45i54e3:fghi0eexyz'
    expected = {b'abd':b'ab', b'cd':b'e', b'45':54, b'fgh':0} 
    data, index = decode_dictionary(inputval, 2)
    assert expected==data

@run
def test_decode_dictionary_returns_index_for_remainder():
    inputval = b'abd3:abd2:ab2:cd1:e2:45i54e3:fghi0eexyz'
    data, index = decode_dictionary(inputval, 2)
    assert index==35
    assert inputval[index]==ord(b'e')
    assert inputval[index+1]==ord(b'x')

@run
def test_readme_example_works():
    contents = b'd3:foo3:bar1:ai22eel3:abci9ee'
    data = decode(contents)
    expected = [{b'foo': b'bar', b'a':22}, [b'abc', 9]]
    assert expected==data
