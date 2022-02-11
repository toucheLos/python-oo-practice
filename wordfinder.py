import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random() in self.words
    True

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, doc):
        """Pair document of words with WordFinder, read all words, print num of words read"""
        document = open(doc)
        self.words = self.setup(document)
        print(f"{len(self.words)} words read")
    
    def setup(self, document):
        """Parse the words in document into self.words"""
        return[w.strip() for w in document]
    
    def random(self):
        """Return one random word from the self.words list"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]