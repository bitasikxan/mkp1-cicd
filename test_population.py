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
    file.write_text("Україна, 603628, 37730000\nАмерика, 42550000, 1035298985\nКитай, 9597000, 1411000000")
    return str(file)

