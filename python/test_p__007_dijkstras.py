from p__007_dijkstras import dijkstra


def test_basic_path():
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    results = dijkstra(graph, "A")
    assert results["A"] == 0
    assert results["B"] == 1
    assert results["C"] == 3  # A -> B -> C
    assert results["D"] == 4  # A -> B -> C -> D


def test_disconnected_graph():
    graph = {"A": {"B": 2}, "B": {"A": 2}, "C": {"D": 1}, "D": {"C": 1}}
    results = dijkstra(graph, "A")
    assert results["A"] == 0
    assert results["B"] == 2
    assert results["C"] == float("inf")


def test_single_node():
    graph = {"A": {}}
    results = dijkstra(graph, "A")
    assert results == {"A": 0}


def test_linear_graph():
    graph = {1: {2: 10}, 2: {3: 10}, 3: {4: 10}, 4: {}}
    results = dijkstra(graph, 1)
    assert results[4] == 30


def test_update_shorter_path():
    # Tests if the indexed heap correctly updates when a much shorter path is found later
    graph = {
        "Start": {"Slow": 10, "Fast": 1},
        "Slow": {"End": 1},
        "Fast": {"End": 20},
        "End": {},
    }
    results = dijkstra(graph, "Start")
    assert results["End"] == 11  # Start -> Slow -> End
