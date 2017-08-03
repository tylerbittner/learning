# Problem statement: https://www.hackerrank.com/challenges/ctci-ransom-note


def ransom_note(magazine, ransom):
    # Create dict of magazine word counts
    d_mag = {}
    for word in magazine:
        if word not in d_mag:
            d_mag[word] = 1
        else:
            d_mag[word] += 1
    # print d_mag

    result = 'Yes'
    # Iterate over ransom note to see if words exist in magazine
    for word in ransom:
        if word not in d_mag:
            result = 'No'
            break
        if d_mag[word] > 0:
            d_mag[word] -= 1
        else:
            # Ran out of words in the magazine!
            # print 'Ran out of words'
            result = 'No'
            break

    return result


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)

print answer
