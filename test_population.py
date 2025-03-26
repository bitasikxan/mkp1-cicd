import pytest
from population import read_population_data, sort_by_area, sort_by_population


@pytest.fixture
def sample_data():
    return [
        ("Україна", 603628, 37730000),
        ("Америка", 42550000, 1035298985),
        ("Китай", 9597000, 1411000000)]


@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_data.txt"
    with open(file, 'w', encoding='utf-8') as f:
        f.write("Україна, 603628, 37730000\nАмерика, 42550000, 1035298985\nКитай, 9597000, 1411000000")
    return str(file)


def test_read_population_data(temp_file):
    data = read_population_data(temp_file)
    assert len(data) == 3
    assert data[0] == ("Україна", 603628, 37730000)


@pytest.mark.parametrize("use_existing_file, expected_len", [
    (False, 0),
    (True, 3),
])


def test_read_population_data_parametrized(use_existing_file, expected_len, temp_file):
    file_path = temp_file if use_existing_file else "nonexistent.txt"
    data = read_population_data(file_path)
    assert len(data) == expected_len


def test_sort_by_area(sample_data):
    sorted_data = sort_by_area(sample_data)
    assert sorted_data[0][1] == 603628
    assert sorted_data[-1][1] == 42550000


def test_sort_by_population(sample_data):
    sorted_data = sort_by_population(sample_data)
    assert sorted_data[0][2] == 37730000  # Poland has the smallest population
    assert sorted_data[-1][2] == 1411000000
