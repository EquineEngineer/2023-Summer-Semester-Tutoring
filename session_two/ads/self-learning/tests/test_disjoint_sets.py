from disjoint_sets import DisjointSets

def test_init():
    ds = DisjointSets()
    assert ds.find_set(1) is None

def test_insert():
    ds = DisjointSets()
    ds.make_set(1)
    assert ds.find_set(1) is not None