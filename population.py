def read_population_data(file_path):
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

def sort_by_area(data):
    """Sorts population data by area in ascending order."""
    return sorted(data, key=lambda x: x[1])

def sort_by_population(data):
    """Sorts population data by population in ascending order."""
    return sorted(data, key=lambda x: x[2])