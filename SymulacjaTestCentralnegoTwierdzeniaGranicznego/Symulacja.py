from Functions.strings import generation_sequence_of_random_variables
from Functions.sequence_division import sequence_division
from Functions.new_sequences import new_sequences
import  json
import  matplotlib.pyplot as plt
if __name__ == "__main__":
    def draw_hist(numbers, val, compartments):
        plt.hist(numbers,bins=compartments, density=True , edgecolor ="green" , color="b")
        plt.title("comparison")
        plt.xlabel(val)
        plt.grid(True)
        plt.show()

    with open("configuration.json" , "r") as config:
        Configuration = json.load(config)

    string_of_varaibles = generation_sequence_of_random_variables(Configuration["Number_Of_elements"],
                                                                  Configuration["lower_range"],
                                                                  Configuration["upper_range"])

    subsq_1 = string_of_varaibles

    subsq_2 = sequence_division(string_of_varaibles,2)

    subsq_5 = sequence_division(string_of_varaibles,5)

    subsq_10 = sequence_division(string_of_varaibles,10)

    '''
    print(subsq_1)
    print(subsq_2)
    print(subsq_5)
    print(subsq_10)
    '''
    new_sequence_1 = subsq_1

    new_sequence_2 = new_sequences(subsq_2)

    new_sequence_5 = new_sequences(subsq_5)

    new_sequence_10 = new_sequences(subsq_10)
    '''
    print(new_sequence_1)
    print(new_sequence_2)
    print(new_sequence_5)
    print(new_sequence_10)
    '''
    draw_hist(new_sequence_1,"zm",50)
    draw_hist(new_sequence_2, "zm", 50)
    draw_hist(new_sequence_5, "zm", 50)
    draw_hist(new_sequence_10, "zm", 50)