def obscene_filter(profane_corpus, input_string):
    list_for_check = input_string.split(' ')
    output_str = ''
    for word in list_for_check:
        if word in profane_corpus:
            output_str += word.replace(word, word[0]+(len(word)-1)*'*') + ' '
        else:
            output_str += word + ' '
    return output_str
