class Wordle:
    def __init__(self):
        self.file = "words.txt"
        self.words = self.getWords()

    def getWords(self):
        words = open(self.file, "r").read().split("\n")
        return words

    def start(self):
        print("Welcome to Wordle solver!")

        while True:
            letters = input("\nYour letters... ")
            words = self.possibleWords(letters)

            print([words, len(words)])

    def possibleWords(self, letters):
        wordList = []
        for word in self.words:
            if self.wordContainsAllLetters(word, letters):
                wordList.append(word)

        return wordList

    def wordContainsAllLetters(self, word, letters):
        matches = self.getWordMatches(word, letters)
        letterLen = len(letters)

        return matches >= letterLen

    def getWordMatches(self, word, letters):
        matches = 0

        for letter in letters:
            if letter in word:
                matches += 1

        return matches


Wordle().start()
