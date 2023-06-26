#Clasificar una serie de tweets con una puntuación acorde al numero de palabras positivas
#o palabras negativas contenidas en dicho tweet

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation (st):
    nst = ""
    for x in st:
        if x not in punctuation_chars:
            nst += x
    
    return nst

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(st):
    l_st = st.lower()
    st_wopn = strip_punctuation(l_st)
    list_st = st_wopn.split()
    
    pos_count = 0
    for x in list_st:
        if x in positive_words:
            pos_count += 1
    return pos_count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(st):
    l_st = st.lower()
    st_wopn = strip_punctuation(l_st)
    list_st = st_wopn.split()
    
    neg_count = 0
    for x in list_st:
        if x in negative_words:
            neg_count += 1
    return neg_count

fileref = open("project_twitter_data.csv","r")
data = fileref.readlines()

outfile = open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")

for i in data[1:]:
    res_row = ""
    splt = i.strip().split(",")           #Leading and trailing whitespaces are removed with strip
    res_row = ("{},{},{},{},{}".format(splt[1], splt[2], get_pos(splt[0]), get_neg(splt[0]), (get_pos(splt[0])-get_neg(splt[0]))))
    outfile.write(res_row)
    outfile.write("\n")

outfile.close()