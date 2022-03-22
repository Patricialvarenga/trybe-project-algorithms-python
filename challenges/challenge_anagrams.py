from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    if len(first_string) != len(second_string):
        return False
    if first_string != second_string:
        return merge_sort(
            first_string.lower()) == merge_sort(second_string.lower())
    else:
        return True
