import argparse
import heapq
import pathlib


class BigFileSort:
    DEFAULT_MEMORY_LIMIT = 100

    def __init__(self):
        self.parser = self._parse()

        self.memory_limit = getattr(self.parser, 'memory', None)

        if self.memory_limit is None:
            self.memory_limit = self.DEFAULT_MEMORY_LIMIT
        else:
            self.memory_limit = int(self.memory_limit)

        self.filename = self.parser.file
        self.file_obj = None
        self.finished = False
        self.sorted_files = []
        self.available_number = 0

    def __del__(self):
        for i in range(self.available_number):
            pathlib.Path(self._sorted_filename(i)).unlink()

    def _parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", "-f", action="store", required=True)
        parser.add_argument("--memory", "-m", action="store")
        return parser.parse_args()

    def _sorted_filename(self, number):
        return "sorted_file#" + str(number)

    def _sort_small_file(self):
        cur_file_size = 0
        strings_to_sort = []
        while cur_file_size < self.memory_limit:
            string = self.file_obj.readline()
            if string == '':
                self.finished = True
                break
            cur_file_size += len(string)
            strings_to_sort.append(string)
        if not strings_to_sort:
            return
        strings_to_sort.sort()
        sorted_filename = self._sorted_filename(self.available_number)
        self.available_number += 1
        with open(sorted_filename, 'w') as file_to_write:
            for s in strings_to_sort:
                file_to_write.write(s)

    def _merge_sorted_files(self):
        string_heap = []
        heapq.heapify(string_heap)
        for i in range(self.available_number):
            file = open(self._sorted_filename(i))
            string = file.readline()
            heapq.heappush(string_heap, (string, i))
            self.sorted_files.append(file)

        with open(self.filename + '_sorted', 'w') as f:
            while string_heap:
                cur_smallest, num = heapq.heappop(string_heap)
                f.write(cur_smallest)
                new_string = self.sorted_files[num].readline()
                if new_string != '':
                    heapq.heappush(string_heap, (new_string, num))
                else:
                    self.sorted_files[num].close()

    def run(self):
        self.file_obj = open(self.filename)
        while not self.finished:
            self._sort_small_file()
        self.file_obj.close()
        self._merge_sorted_files()


if __name__ == "__main__":
    BigFileSort().run()
