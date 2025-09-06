import math
import pytest
from lib.figures import Triangle

def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(0, 1, 1)
    with pytest.raises(ValueError):
        Triangle(4, 3, -2)
    with pytest.raises(ValueError):
        Triangle(1, 1, 2)
    with pytest.raises(ValueError):
        Triangle(3, 3, 6)

def test_triangle_area_and_is_rectangular():
    t1 = Triangle(2, 2, 3)
    t2 = Triangle(3, 4, 5)
    t3 = Triangle(4, 5, 6)
    t4 = Triangle(5, 12, 13)
    t5 = Triangle(5, 5, 7)
    assert t1.is_rectangular == False
    assert t2.is_rectangular == True
    assert t3.is_rectangular == False
    assert t4.is_rectangular == True
    assert t5.is_rectangular == False
    assert math.isclose(t1.area, 1.984313483298)
    assert math.isclose(t2.area, 6)
    assert math.isclose(t3.area, 9.921567416492)
    assert math.isclose(t4.area, 30)
    assert math.isclose(t5.area, 12.49749974995)