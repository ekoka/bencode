def decode(contents):
    try:
        # the parser will use the additional 'e' to return the data
        return [data for data, index in parse(contents + b'e') 
                if data is not None]
    except TypeError as e:
        raise TypeError('Wrong string type. Expected bytes, received unicode')
    except: 
        raise ValueError('Malformed bencoded data')

def parse(bytedata, index=-1):
    data = None
    while True:

        if data is not None:
            yield data, index
            data = None

        index += 1

        if bytedata[index]==ord(b'e'):
            # closing a parsing context
            yield data, index
            return

        # handle int
        if bytedata[index]==ord(b'i'):
            data, index = decode_integer(bytedata, index)
            continue

        # handle list
        if bytedata[index]==ord(b'l'):
            data, index = decode_list(bytedata, index)
            continue

        # handle dict 
        if bytedata[index]==ord(b'd'):
            data, index = decode_dictionary(bytedata, index)
            continue

        # handle byte
        data, index = decode_bytestring(bytedata, index)


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
    length = 0 # length of the bytestring to parse
    while True:
        length = length * 10 + int(chr(data[index]))
        index += 1
        if data[index]==ord(b':'):
            break
    index += 1
    return data[index: index+length], index+length-1

def decode_list(bytedata, index):
    stream = [(item, index) for item, index in parse(bytedata, index)]
    end_of_stream, index = stream.pop()
    data = [item for item, i in stream]
    return data, index

def decode_dictionary(bytedata, index):
    stream = [(item, index) for item, index in parse(bytedata, index)]
    end_of_stream, index = stream.pop()
    data = {}
    for i in range(0, len(stream), 2):
        key = stream[i][0]
        value = stream[i+1][0]
        data[key] = value
    return data, index
