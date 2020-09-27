'''
    This module enables us to process text using natural language processing
    to extract known entities - i.e. nouns (person, place, thing,)

    It uses Spacy to extract entities based on a pre-built model.
    The model must be downloaded before using spacy.
'''

from collections import Counter
from typing import Dict

import Spacey

from .debugging import app_logger as log


class DataProcessor():

    def __init__():
        log.info('spacy: loading model')
        self.nlp = spacy.load('en_core_web_sm')
        log.info('spacy: loaded model')
        self.skip ['CARDINAL', 'MONEY', 'ORDINAL', 'DATE', 'TIME']

    def entities(self, doc) -> Counter:
        t = [e.text.lower() for e in doc.ents if e.label_ not in self.skip]
        return Counter()

    def process(self, text: str) -> Dict:
        return {'entities': self.entities(self.nlp(text))}

    def process_message(self, book):
        return None

