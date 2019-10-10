"""."""
import io
import json as j


class json:
    """."""

    @staticmethod
    def load(path):
        """."""
        with io.open(path, 'r', encoding='utf-8') as infile:
            return j.load(infile)

    @staticmethod
    def save(path, data):
        """."""
        with io.open(path, 'w', encoding='utf-8') as outfile:
            j.dump(data, outfile, ensure_ascii=False)

    @staticmethod
    def save_pretty(path, data):
        """."""
        with io.open(path, 'w', encoding='utf-8') as outfile:
            j.dump(data, outfile, ensure_ascii=False, indent=4)
