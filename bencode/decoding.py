def decode(contents):
    try:
        # the parser will use the final 'e' to return the data
         data, index = parse(contents + b'e')
         return data
    except TypeError as e:
        raise TypeError('Wrong string type. Expected bytes, received unicode')
    except: 
        raise ValueError('Malformed bencoded data')

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
            data, index = decode_dictionary(bytedata, index)
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
