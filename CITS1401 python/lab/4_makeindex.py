def make_index(words_on_page):
    wdict= {}
    for key,value in words_on_page.items():
        for word in value:
            word_lower = word.lower()
            if word_lower in wdict:
                wdict[word_lower].append(key)
            else:
                wdict[word_lower] = [key]
    return wdict
            
        