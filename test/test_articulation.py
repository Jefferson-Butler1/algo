from src.articulation import ArticulationPointFinder
from src.space_disagreement import generate_map


def test_finds_articulation_points():
    p, g = generate_map(10, random_seed=0)
    a = ArticulationPointFinder(g)
    assert a.is_articulation_point == [True, False, True, False, True, False, False, False, False, True]
