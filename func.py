

def define(count_return=int, list_answers=list, element=str) -> str:
    return list_answers[int(element)-1]

def fullname_share(element=str) -> list:
    element += ' '
    names, word = [], ''
    for i in element:
        if i == ' ':
            names.append(word)
            word = ''
        else:
            word += i

    return names
