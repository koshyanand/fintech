import pandas

header = "Item&nbsp;"

def get_item_combinations(section_no_list):
    partition_list = []
    df = pandas.read_csv('data/item_list.csv')

    shape = df.shape
    item_list = df.values.tolist()
    for section in section_no_list:
        for i, row in enumerate(item_list):  
            if row[0] == section:
                start = section
                if i + 1 < shape[0]: 
                    end = item_list[i + 1][0]
                else:
                    end = None
                partition_list.append((start, end))
    return partition_list


def get_raw_section(full_text, section_no_list):
    partition_list = get_item_combinations(section_no_list)
    section = []
    for partition in partition_list:
        start, end = partition
        print(header + start)
        start_pos = full_text.find(header + start)
        print(start_pos)
        if end != None:
            end_pos = full_text.find(header + end)
        print(end_pos)
        section.append(full_text[start_pos : end_pos])
    return section
    # print(partition_list)

    

