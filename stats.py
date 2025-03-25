def get_num_words(book_text):
    num_words=len(book_text.split())
    return num_words

def get_caracters_count(book_text):
    list_of_words=book_text.split()
    dict_of_caracters={}
    for word in list_of_words:
        word=word.lower()
        for caracter in word:
            if caracter in dict_of_caracters.keys():
                dict_of_caracters[caracter]=dict_of_caracters[caracter]+1
            else:
                dict_of_caracters[caracter]=1
    return dict_of_caracters

def sort_on(dict):
    return dict['count']

def output(dict_of_caracters,num_words,path_to_book):
    list_of_caracters_and_counts=[]
    for key,value in dict_of_caracters.items():
        pair={}
        pair['caracter']=key
        pair['count']=value
        list_of_caracters_and_counts.append(pair)
    list_of_caracters_and_counts.sort(reverse=True,key=sort_on)
    print(f'''
============ BOOKBOT ============
Analyzing book found at {path_to_book}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')
    for i in range(0,len(list_of_caracters_and_counts)):
        if list_of_caracters_and_counts[i]['caracter'].isalpha() == True:
            print(f'{list_of_caracters_and_counts[i]['caracter']}: {list_of_caracters_and_counts[i]['count']}')
    print('============= END ===============')
