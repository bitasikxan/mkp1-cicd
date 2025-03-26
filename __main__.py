from population import read_population_data, sort_by_area, sort_by_population

def main():
    file_path = "population.txt"
    data = read_population_data(file_path)

    if not data:
        print("Дані відсутні.")
        return

    print("Sorted by area:")
    for entry in sort_by_area(data):
        print(f"Country: {entry[0]}, Area: {entry[1]}, Population: {entry[2]}")

    print("\nSorted by population:")
    for entry in sort_by_population(data):
        print(f"Country: {entry[0]}, Area: {entry[1]}, Population: {entry[2]}")


if __name__ == "__main__":
    main()