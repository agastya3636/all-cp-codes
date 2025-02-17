def read_grammar(file_name):
    with open(file_name, 'r') as file:
        productions = {}
        for line in file:
            line = line.strip()
            if '->' in line:
                lhs, rhs = line.split('->')
                lhs = lhs.strip()
                rhs_options = [option.strip() for option in rhs.split('|')]
                productions[lhs] = rhs_options
        return productions

def first(symbol, productions, first_sets, visited):
    if symbol in visited:
        return first_sets[symbol]
    visited.add(symbol)

    first_set = set()
    if symbol not in productions:  # Terminal symbol
        first_set.add(symbol)
        return first_set

    for production in productions[symbol]:
        if production == 'ϵ':
            first_set.add('ϵ')
        else:
            for char in production:
                char_first = first(char, productions, first_sets, visited)
                first_set.update(char_first - {'ϵ'})
                if 'ϵ' not in char_first:
                    break
            else:
                first_set.add('ϵ')

    first_sets[symbol] = first_set
    return first_set

def follow(symbol, productions, first_sets, follow_sets, visited):
    if symbol in visited:
        return follow_sets[symbol]
    visited.add(symbol)

    follow_set = set()
    if symbol == list(productions.keys())[0]:  # Start symbol
        follow_set.add('$')

    for lhs, rhs_list in productions.items():
        for rhs in rhs_list:
            for i, char in enumerate(rhs):
                if char == symbol:
                    if i + 1 < len(rhs):
                        next_symbol = rhs[i + 1]
                        first_next = first_sets[next_symbol]
                        follow_set.update(first_next - {'ϵ'})
                        if 'ϵ' in first_next:
                            follow_set.update(follow(lhs, productions, first_sets, follow_sets, visited))
                    else:
                        if lhs != symbol:
                            follow_set.update(follow(lhs, productions, first_sets, follow_sets, visited))

    follow_sets[symbol] = follow_set
    return follow_set

def compute_first_follow(productions):
    first_sets = {}
    follow_sets = {}
    visited = set()

    # Compute First sets
    for symbol in productions:
        first(symbol, productions, first_sets, visited)

    visited.clear()

    # Compute Follow sets
    for symbol in productions:
        follow(symbol, productions, first_sets, follow_sets, visited)

    return first_sets, follow_sets

def main():
    productions = read_grammar('demo.txt')
    first_sets, follow_sets = compute_first_follow(productions)
    print(productions)
    print("First:")
    for symbol in first_sets:
        print(f"Fr({symbol})={{{', '.join(first_sets[symbol])}}}")

    print("Follow:")
    for symbol in follow_sets:
        print(f"Fw({symbol})={{{', '.join(follow_sets[symbol])}}}")

if __name__ == "__main__":
    main()