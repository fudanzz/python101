def reverse_lines(input,output):
    with open(input) as infile, open(output,'w') as outfile:
        for line in infile.readlines():
            outfile.writelines(f'{line.rstrip()[::-1]}\n')

if __name__ == '__main__':
    reverse_lines('data/infile.txt','data/outfile.txt')

