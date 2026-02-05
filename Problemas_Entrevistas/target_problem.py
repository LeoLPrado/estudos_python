vetor_original = [11, 15, 2, 7]
target = 9

def search_target(vetor_original):
    vetor_sort = sorted(vetor_original)
    i = 0
    j = len(vetor_sort) - 1
    tupla = (None, None)

    while i < j:
        if vetor_sort[i] + vetor_sort[j] < target:
            i += 1
        elif vetor_sort[i] + vetor_sort[j] > target:
            j -= 1
        else:
            tupla = (i, j)
            break
    return tupla

print(search_target(vetor_original))