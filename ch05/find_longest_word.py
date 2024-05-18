import os

def find_longest_word(filename):
    with open(filename) as file:
        longest_word = ''
        for line in file:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

def find_all_longest_words(dirname):    
    return {
            filename:find_longest_word(os.path.join(dirname, filename)) 
            for filename in os.listdir(dirname) 
            if os.path.isfile(os.path.join(dirname, filename))
            }

if __name__ == '__main__':
    print(find_longest_word('wcfile.txt'))
    print(find_all_longest_words('./data'))
    