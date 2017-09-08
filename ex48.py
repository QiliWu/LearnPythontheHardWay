D = {'direction': ['north', 'south', 'east','west', 'down', 'up', 'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
         'noun': ['door', 'bear', 'princess', 'fighter','cabinet']
         }

def convert_numbers(word):
    try:
        return int(word)
    except ValueError:
        return None


def scan(sentence):
    words = sentence.split(" ")
    res = []
    for word in words:
        if convert_numbers(word) != None:
            res.append(('number', convert_numbers(word)))
        else:
            type = 'error'
            for t in D:
                if word.lower() in D[t]:
                    type = t
                    break
            res.append((type, word)) # error for res=res.append()

    return res




