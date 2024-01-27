def new_sequences(subseq):
    new_sq = []
    numberOfelements = len(subseq)
    i = 0
    while i < numberOfelements:
        mean = 0
        for q in subseq[i]:
            mean+=q
        mean = mean/len(subseq[i])
        new_sq.append(mean)
        i+=1
    return  new_sq
