class lexicon:


    D = {'direction': ['north', 'south', 'east','west', 'down', 'up', 'left', 'right', 'back'],
         'verbs': ['go', 'stop', 'kill', 'eat'],
         'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
         'nouns': ['door', 'bear', 'princess', 'cabinet']
         }

    def convert_numbers(self, word):
        try:
            return int(word)
        except ValueError:
            return None


    def scan(self, sentence):
        words = sentence.split(" ")
        res = []
        for word in words:
            if self.convert_numbers(word) != None:
                res.append(('numbers', self.convert_numbers(word)))
            else:
                type = 'error'
                for t in lexicon.D:
                    if word in lexicon.D[t]:
                        type = t
                        break
                res.append((type, word)) # error for res=res.append()

        return res




