def parse_netlist(file_path):
    components = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith('*') or line.lower().startswith('.end'):
            continue  # Skip comments and .end

        parts = line.split()
        comp_type = parts[0][0].upper()  # R, C, L, V, etc.
        name = parts[0]
        nodes = parts[1:-1]
        value = parts[-1]

        components.append({
            'type': comp_type,
            'name': name,
            'nodes': nodes,
            'value': value
        })

    return components

# Example usage
if __name__ == "__main__":
    netlist_file = 'circuit.spice'
    parsed = parse_netlist(netlist_file)

    for comp in parsed:
        print(f"{comp['name']} ({comp['type']}): Nodes {comp['nodes']} -> Value: {comp['value']}")

