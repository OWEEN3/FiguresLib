import math
import pytest
from lib.figures import Circle

def test_circle_area():
    c1 = Circle(1)
    c2 = Circle(5)
    c3 = Circle(12)
    
    assert math.isclose(c1.area, math.pi)
    assert math.isclose(c2.area, 78.539816339745)
    assert math.isclose(c3.area, 452.38934211693)

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)
        
    with pytest.raises(ValueError):
        Circle(-5)