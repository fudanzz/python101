def word_count(filename):
    with open(filename) as f:
        lines = f.readlines()
        print('number of lines:', len(lines))
        words = []
        total_characters = 0
        for line in lines:
            total_characters += len(line)
            words += line.split()
        print('number of words:', len(words))
        print('number of unique words:', len(set(words)))
        print('number of total characters:', total_characters)

if __name__ == '__main__':
    word_count('wcfile.txt')