"""."""
from nltk.stem import RSLPStemmer
import unicodedata
import string


class text_cleaner:
    """."""

    __st = RSLPStemmer()
    __translator = str.maketrans({key: ' ' for key in string.punctuation})

    @staticmethod
    def remove_accents(input_str):
        """."""
        nkfd_form = unicodedata.normalize('NFKD', str(input_str))
        return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

    @staticmethod
    def remove_special_characters(input_str):
        """."""
        return input_str.translate(text_cleaner.__translator).lower()

    @staticmethod
    def stem(text):
        """."""
        stemmed_words = []
        dictionary = {}
        for word in text.split():
            stemmed_word = text_cleaner.__st.stem(word)
            stemmed_words.append(stemmed_word)
            if dictionary.get(stemmed_word) is None:
                dictionary[stemmed_word] = {}
            dictionary[stemmed_word][word] = 1
        out = {}
        out['stemmed_text'] = ' '.join(stemmed_words)
        out['dictionary'] = dictionary
        return out

    @staticmethod
    def last_dict(text):
        """."""
        return ' '.join([text_cleaner.__st.stem(w) for w in text.split()])

    @staticmethod
    def clean(text):
        """."""
        text = text_cleaner.remove_special_characters(text)
        text = text_cleaner.remove_accents(text)
        text = text.lower()
        text = text_cleaner.stem(text)['stemmed_text']
        return text
