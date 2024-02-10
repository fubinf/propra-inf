import random


def secret_santa(input_list: list[str]) -> dict[str, str]:
    """ Returns a dictionary, the keys are giver's names, the values are receiver's names.

    input_list: A list of names
    """

    if len(input_list) < 2:
        return {}

    return_dict = {}

    """ Make a copy of the input list; 
        we remove people from this list as they are assigned givers.
    """

    receivers_list = input_list[:]

    for person in input_list:
        """ If there are only two receivers left, and one
            of them is the last person in the input_list, then
            assign the last person to the second-to-last
            person.
        """

        if len(receivers_list) == 2:
            if receivers_list.count(input_list[-1]) == 1:
                return_dict[person] = input_list[-1]
                return_dict[input_list[-1]] = person
                break

        """ The typical situation, just randomly pick
            someone out of receivers_list and give them to
            person. We don't want to assign someone to 
            themselves. If that happens, we assign them the
            next person in receivers_list.
        """

        if receivers_list.count(person) == 1:
            receiver_index = int((len(receivers_list) - 1) * random.random())
            if receivers_list.index(person) <= receiver_index:
                receiver_index += 1
        else:
            receiver_index = int(len(receivers_list) * random.random())

        return_dict[person] = receivers_list.pop(receiver_index)

    return return_dict


test_input = ["Tom", "Joe", "Donna", "Susan", "Paul"]

print(secret_santa(test_input))
