def read_population_data(file_path):
    """Reads population data from a txt file and returns a list of tuples."""
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                name, area, population = line.strip().split(',')
                data.append((name.strip(), int(area.strip()), int(population.strip())))
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except ValueError as e:
        print(f"Error parsing data: {e}")
        return []
    return data
