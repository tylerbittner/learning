def number_needed(a, b):
    ''' Bruteforce plan:
    - Store strings as dicts w/ letter as key & # of occurrences as value
    - Iter thru each char of dict a:
        - If not exists in dict b, store # of chars to delete
        - if exists in dict b, store abs value of diff of occurrences to delete
            - actually delete char from dict b
    - Iter thru what's left of dict b:
        - for each add to # chars to delete

    Time complexity of this solution should be O(N + M)
    Example case:
        a = 'ycnwimmsssh'
        b = 'qoimcbgssgxujfnadsfoisdf'
    '''

    delete_count = 0

    dict_a = string_to_dict(a)
    dict_b = string_to_dict(b)

    for char in dict_a:
        if char not in dict_b:
            delete_count += dict_a[char]
        if char in dict_b:
            delete_count += abs(dict_a[char] - dict_b[char])
            del dict_b[char]

    for char in dict_b:
        delete_count += dict_b[char]

    return delete_count


def string_to_dict(s):
    '''Converts a string into a dict with frequency count for each char'''

    dict_count = {}
    for char in s:
        if char not in dict_count:
            dict_count[char] = 1
        else:
            dict_count[char] += 1

    # print dict_count
    return dict_count


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
