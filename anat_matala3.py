def read_line(n, file):
    try:  n = int(n)
    except:
        print("invalid input detected")
        return
    try:f = open(file,"r")
    except:
        print("file not found")
        return
    count =0
    for index,line in enumerate (f):
        count += 1
        if index ==n-1:
            print(line.rstrip())
    if count <=n:
        str(n)
        print("line",n,"doesn't exist")

# read_line(4,'ex3_text.txt')
# read_line(9,'ex3_text.txt')
# read_line(29,'ex3_text.txt')
# read_line('c','ex3_text.txt')
# read_line(9,'ex4_text.txt')
#ex3_text.txt


def longest_words(file):
    try:f = open(file,"r")
    except:
        print("file not found")
        return
    biggest_words = ["","","","",""]
    for line in f:
        sentense = line.split()
        for word in sentense:
            word = word.rstrip(",")
            if not word.startswith("-"):
                biggest_words = top_five(word,biggest_words)
    print(biggest_words)
def top_five(word,list):
    for index,w in enumerate(list):
        if len(w)<len(word):
            list.insert(index,word)
            list.pop(5)
            return list
    return list


longest_words('ex3_text.txt')