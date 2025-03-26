def read_population_data(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            for line in file:
                name, area, population = line.strip().split(',')
                data.append((name.strip(), int(area.strip()), int(population.strip())))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return []
    except ValueError as e:
        print(f"Помилка при парсингу даних: {e}")
        return []
    return data


def sort_by_area(data):
    return sorted(data, key=lambda x: x[1])


def sort_by_population(data):
    return sorted(data, key=lambda x: x[2])
