import argparse
import string
import random


class Generator:
    DEFAULT_FILENAME = 'some_file'

    def __init__(self):
        self.parser = self._parse()
        self.number = int(self.parser.number)
        self.length = int(self.parser.length)
        self.filename = getattr(self.parser, 'file', None)
        if self.filename is None:
            self.filename = self.DEFAULT_FILENAME

    def _parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--number", "-n", action="store", required=True)
        parser.add_argument("--length", "-l", action="store", required=True)
        parser.add_argument("--file", "-f", action="store")
        return parser.parse_args()

    def _generate_string(self):
        str_len = random.randrange(1, self.length)
        return ''.join([random.choice(string.ascii_letters) for i in range(str_len)]) + '\n'

    def generate_file(self):
        with open(self.filename, 'w') as f:
            for i in range(self.number):
                f.write(self._generate_string())


if __name__ == "__main__":
    Generator().generate_file()
