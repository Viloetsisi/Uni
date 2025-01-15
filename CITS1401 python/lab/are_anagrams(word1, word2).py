def are_anagrams(word1, word2):
    word_list1 = list(word1)
    word_list2 = list(word2)
    word_list1.sort()
    word_list2.sort()
    if word1 == word2:
        return False
    elif word_list1 == word_list2:
        return True
    else:
        return False