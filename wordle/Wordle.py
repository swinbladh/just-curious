# TODO: input and handle a letter with known position
# TODO: Word frequency

import json


class Wordle:
    def __init__(self):
        self.file = "word_freq.json"
        self.wordFrequency = self.getWords()
        self.words = list(self.wordFrequency.keys())

    def getWords(self):
        file = open(self.file)
        words = json.load(file)

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

        sortedWordList = wordList.sort(key=self.getFrequency)
        return sortedWordList

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

    def getFrequency(self, word):
        return self.wordFrequency[word]


Wordle().start()
