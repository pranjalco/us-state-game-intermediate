import pandas


class StateInfoCalculation:

    """This class create a final list which contains lists in the format [state, x, y]"""
    def __init__(self):

        self.data = pandas.read_csv("50_states.csv")
        self.data_dict = self.data.to_dict()

        self.data_list = []
        self.final_data_list = []
        self.index = 0
        for iteration in range(50):
            for item in self.data_dict:
                # here state, x, y are keys when we convert data to dict
                # So here item is state, x and y
                element = self.data_dict[item][self.index]
                # Here element will have this format: [state, x, y]
                self.data_list.append(element)
            self.index += 1
            # Here we are appending a list [state, x, y] to final data list
            self.final_data_list.append(self.data_list)
            self.data_list = []
        # print(self.final_data_list)


def blank_line():
    print("")
