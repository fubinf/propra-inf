def find_substring(outer_string: str, sub_string:str) -> (str, str):
    """Finds the first occurrence of sub_string within outer_string.

       Returns a tuple of the part of the string
       before the first occurrence of sub_string,
       and the part starting at the first occurrence
       of sub_string. If not found, the second tuple
       is empty.
    """

    outer_len = len(outer_string)
    sub_len = len(sub_string)
    flag = 1
    i = 0   # declaring i beforehand so we can use it in the return statement

    for i in range(outer_len):
        for j in range(sub_len):
            if outer_string[i+j] != sub_string[j]:
                break
        else:
            # wind up here if for j loop terminates naturally
            flag = 0
            break  # break out of i loop

    return outer_string[:(i+flag)], outer_string[(i+flag):]


print(find_substring("Hello", "l"))
