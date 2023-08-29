def find_symmetric_pairs(pairs):
    symmetric_pairs = []
    pair_map = {}

    for pair in pairs:
        first, second = pair
        if second in pair_map and pair_map[second] == first:
            symmetric_pairs.append((first, second))
        else:
            pair_map[first] = second

    return symmetric_pairs

input_str = input("Enter the pairs in the format 'a1 b1 a2 b2 ...': ")
pair_values = list(map(int, input_str.split()))

pairs = [(pair_values[i], pair_values[i + 1]) for i in range(0, len(pair_values), 2)]

symmetric_pairs = find_symmetric_pairs(pairs)

if symmetric_pairs:
    print("Symmetric pairs:")
    for pair in symmetric_pairs:
        print(pair)
else:
    print("No symmetric pairs found.")

