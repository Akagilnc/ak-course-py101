def read_graph():
    with open('source.txt') as file:
        source_data = list(file)
        source_data.sort()
    return source_data


result_dict = {}
for info in read_graph():
    infos = info.strip().split(';')
    node_name = infos[0]
    node_value = infos[1]

    if [node_value] != result_dict.setdefault(node_name, [node_value]):
        result_dict[node_name].append(node_value)
        result_dict[node_name].sort()

print(result_dict)
