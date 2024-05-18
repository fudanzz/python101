def passwd_dict(filename):
    passwd = {}
    for line in open(filename):
        ##print(line)
        if not line.startswith(('#','\n')):
           user_info = line.split(':')
           user = user_info[0]
           userid = user_info[2].strip()
           passwd[user] = userid
    return passwd

if __name__ == '__main__':
    print(passwd_dict('passwd'))