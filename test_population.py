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

def test_read_population_data(temp_file):
    data = read_population_data(temp_file)
    assert len(data) == 3
    assert data[0] == ("Україна", 603628, 37730000)

@pytest.mark.parametrize("file_path, expected_len", [
    ("nonexistent.txt", 0),
    (temp_file, 3),
])


