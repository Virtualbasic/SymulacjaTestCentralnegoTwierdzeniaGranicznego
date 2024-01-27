def sequence_division(sequence, length):
    subSequence = []
    sq = []
    i = 0
    while i<len(sequence):
        sq.append(sequence[i])
        if len(sq) == length:
            subSequence.append(sq)
            sq = []
        i+=1
    return subSequence