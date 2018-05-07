def pretty_dict(dictionary, wrap_length):
    keys = list(dictionary.keys())
    lines = []
    
    for i in range(len(keys)//wrap_length+1):
        try:
            line = ["%s: %s, " % (repr(key),repr(dictionary[key])) for key in keys[wrap_length*i:wrap_length*i+wrap_length]]
            lines.append(''.join(line))
        except IndexError:
            line = ["%s: %s, " % (repr(key),repr(dictionary[key])) for key in keys[wrap_length*i:]]
            lines.append(''.join(line))
    return '{' + '\n'.join(lines) + '}'

def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda t: t[1], reverse=True))

def increment_or_create(d,entry):
    try:
        d[entry] += 1
    except KeyError:
        d[entry] = 1  
