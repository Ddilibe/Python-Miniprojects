# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename,'r')
    return file


def count_words():
    file = read_file_content("./story.txt")
    q,w= [],[]
    check = {}
    # [assignment] Add your code here
    for i in file:
        i = i.split(' ')
        for f in i:
                w.append(f)
    while True:
         if '\n' in w:
            if '' in w:
                w.remove('') 
            w.remove('\n')
         else:
            break
    for i in w:
        if i in q:
                num = check.get(i)
                num += 1
                check[i] = num
        else:
                q.append(i)
                check[i] = 1
    file.close()
    return check