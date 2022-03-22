# fonte de pesquisa:
# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    elif low_index == high_index:  # se só tem 1 caracter, será true
        return True
# se o primeiro e o último caracter não forem iguais, será false
    elif word[low_index] != word[high_index]:
        return False
# se tem mais de 2 caracters, check se a string do meio
# é tbm um palindrome
    elif low_index < high_index + 1:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return True
# Para ser recursiva:
# condições de parada e a função faz chamada a si mesma
