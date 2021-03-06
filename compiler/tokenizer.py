# tokenizer.py
#
# Copyright(c) Exequiel Ceasar Navarrete <exequiel.navarrete09gmail.com>
# Licensed under MIT
# Version 1.0.0-alpha2

import re

# define constant regex
NUMBERS = re.compile('[0-9]') # numbers
LETTERS = re.compile('[a-zA-Z]') # name
WHITESPACE = re.compile(r'\s')
QUOTES = re.compile(r'\"')

class Tokenizer(object):
  """ Class that generates tokens for the compiler """

  def __init__(self, text):
    self.text = text
    self.current = 0
    self.tokens = []

  def run(self):
    separated = list(self.text)

    while self.current < len(separated):
      char = separated[self.current]

      # check for parenthesis
      if char == '(' or char == ')':
        self.tokens.append({
          'type': 'paren',
          'value': char
        })

        self.current += 1

        continue

      # skip white space
      if WHITESPACE.match(char):
        self.current += 1
        continue

      # check for numbers
      if NUMBERS.match(char):
        value = ""

        # loop until the next character is a number
        while NUMBERS.match(char):
          # append the character to the value
          value += char

          # increment the counter
          self.current += 1

          # get the next character
          char = separated[self.current]

        # finally, append the token to the list
        self.tokens.append({
          'type': 'number',
          'value': value
        })

        continue

      # check quoted strings
      if QUOTES.match(char):
        value = ""

        # increment the counter
        self.current += 1

        # get the next character
        char = separated[self.current]

        # loop until the next character is a number, letter or space
        while LETTERS.match(char) or NUMBERS.match(char) or WHITESPACE.match(char):
          # append the character to the value
          value += char

          # increment the counter
          self.current += 1

          # get the next character
          char = separated[self.current]

        # finally, append the token to the list
        self.tokens.append({
          'type': 'name',
          'value': value
        })

        # increment the counter to skip the closing quote
        self.current += 1

        continue

      # check for letters
      if LETTERS.match(char):
        value = ""

        # loop until the next character is a number
        while LETTERS.match(char):
          # append the character to the value
          value += char

          # increment the counter
          self.current += 1

          # get the next character
          char = separated[self.current]

        # finally, append the token to the list
        self.tokens.append({
          'type': 'name',
          'value': value
        })

        continue

      raise ValueError('Unknown character passed')

    return self.tokens


