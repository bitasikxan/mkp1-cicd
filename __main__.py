from population import read_population_data, sort_by_area, sort_by_population


def output_sorted(output, func, data):
    print(output)
    for entry in func(data):
        print(f"Країна: {entry[0]}, Площа: {entry[1]}, Населення: {entry[2]}")


def main():
    file_path = "population.txt"
    data = read_population_data(file_path)

    if not data:
        print("Дані відсутні.")
        return

    output_sorted(output="Сортування за площею:", func=sort_by_area, data=data)
    output_sorted(output="\nСорутвання за населенням:", func=sort_by_population, data=data)


if __name__ == "__main__":
    main()
