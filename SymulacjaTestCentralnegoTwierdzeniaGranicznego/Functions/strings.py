import json


def generation_sequence_of_random_variables(n, upz , downz):
    with open("Functions/sequences.json" , "r") as sequences:
        Sequences = json.load(sequences)
    import random
    sequence = []
    i = 0
    while i<n:
        num =  random.random() *(downz-upz) + upz
        sequence.append(num)
        i+=1
    Sequences["sequences"].append(sequence)
    with open("Functions/sequences.json", "w") as write_sequence:
        json.dump(Sequences,write_sequence,indent=2)
    return sequence