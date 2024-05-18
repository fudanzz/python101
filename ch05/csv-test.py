import csv

def passwd_to_cswv(passwd_filename,csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename,'w') as output:
        infile = csv.reader(passwd,delimiter=':')
        outfile = csv.writer(output,delimiter='\t')
        for line in infile:
            if(len(line) > 1):
                outfile.writerow((line[0],line[2]))


if __name__ == '__main__':
    passwd_to_cswv('data/passwd','data/passwd.csv')