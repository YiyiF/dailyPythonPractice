import os


def isComment(line):
    """:param line:
    :return: String: Comment Type"""
    line = line.replace(' ', '')
    if line.startswith('#'):
        return 'lineComment'
    elif line.startswith((r"'''", r'"""')):
        return 'multilineComment'
    else:
        return 'NotComment'


def codeStatistics(path):
    """

    :param path:
    :return:
    """
    blankLines = 0
    commentLines = 0
    codeLines = 0
    file = open(path)
    line = file.readline()
    while line:
        if (line == ' ' * len(line)) or (line == '\n'):
            blankLines += 1
            line = file.readline()
        else:
            tmp = isComment(line)
            if tmp == 'lineComment':
                commentLines += 1
                line = file.readline()
            elif tmp == 'multilineComment':
                commentLines += 1
                while True:
                    commentLines += 1
                    line = file.readline()
                    if line.endswith(("'''\n", '"""\n')) or (isComment(line) == 'multilineComment'):
                        line = file.readline()
                        break
            else:
                codeLines += 1
                line = file.readline()
    return [blankLines, commentLines, codeLines]


if __name__ == '__main__':
    # path = 'testPyFile'
    # files = os.walk(path)
    # for dirpath, dirnames, filenames in files:
    #     for filename in filenames:
    #         if not filename.lower().endswith('.py'):
    #             continue
    #         result = codeStatistics(dirpath + os.path.sep + filename)
    #         print('File: {}\n    Blank line: {}\n    Comment line: {}\n    Code line: {}'
    #               .format(filename, result[0], result[1], result[2]))
    pythonFile = 'codeStatistics.py'
    result = codeStatistics(pythonFile)
    print('File: {}\n    Blank line: {}\n    Comment line: {}\n    Code line: {}'
          .format(pythonFile, result[0], result[1], result[2]))
