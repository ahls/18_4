from random import choice
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, path):
        f = open(path,'r')
        self.words = f.read().split('\n')
        f.close()
        self.displayNumRead()
    
    def displayNumRead(self):
        print(f"{len(self.words)} words read.")

    def random(self):
        return choice(self.words)



class RandomWordFinder(WordFinder):
    def __init__(self, path):
        self.words = []
        f = open(path,'r')
        while True:
            line = f.readline()
            if(len(line) == 0):
                break

            word = line.strip()
            if word == "" or  word[0] == '#':
                continue
            
            self.words.append(word)
        f.close()
        self.displayNumRead()
    