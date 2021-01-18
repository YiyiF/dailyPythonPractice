#! /usr/bin/env python3
import sys, string, time, os


def countWords(path):
    begin = time.time()
    if not path.endswith('.txt'):
        print('Must be .txt file!')
        sys.exit()

    words_count = 0

    file = open(path)
    line = file.readline()
    words_Punctuation = string.punctuation.replace('\'', '').replace('-', '') + string.whitespace
    i = 0
    while line:
        while i < len(line):
            if line[i] in string.ascii_letters:
                if line[i + 1] in words_Punctuation:
                    words_count += 1
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        line = file.readline()
        i = 0

    print('{} has {} words overall.'.format(path, words_count))  # testText.txt has 14 words overall.
    print('Count {} bytes sized file finish in {:.4f} secs.'.format(os.path.getsize(path), time.time() - begin))
    # Count 114 bytes sized file finish in 0.0006 secs.


if __name__ == '__main__':
    path = input('Input text file name (with path): ')
    countWords(path)
