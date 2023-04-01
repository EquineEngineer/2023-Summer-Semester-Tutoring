import pytest

# Function definition for type
@pytest.mark.skip(reason="no way of currently testing this")
def test_type_of_triangle():
	from triangle import type_of_triangle

	expected_type = 'Equilateral'
	actual_type = type_of_triangle(1, 1, 1)
	assert actual_type == expected_type