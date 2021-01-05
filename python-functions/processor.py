def process_numbers(unprocessed_list):
    processed_list = []
    if isinstance(unprocessed_list, list) == False:
        return processed_list
    for item in unprocessed_list:
        if isinstance(item, int):
            processed_list.append(item)
        elif item.isnumeric():
            processed_list.append(int(item))
    processed_list.sort()
    return processed_list

def process_names(unprocessed_list):
    processed_list = []
    if isinstance(unprocessed_list, list) == False:
        return processed_list
    for item in unprocessed_list:
        if isinstance(item, str):
            if item.isnumeric() == False:
                processed_list.append(item)
    processed_list.sort()
    return processed_list



