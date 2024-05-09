def mutate_string(string, position, character):
    #First approach Indexing
    string = string[:position] + character + string[position+1:]
    return string

    # second approach convert it into list
    # l = list(string)
    # l[position] = character
    # string = ''.join(l)
    # return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)