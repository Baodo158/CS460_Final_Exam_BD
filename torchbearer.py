"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Bao Do
Student ID:   131987229

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    return (
        "Question 1: \n"
        "A single shortest-path run from S is not enough because it's only gives the cheapest cost from S to every reachable node. It does not determine which order the relics should be collected in. \n"
        "Question 2: \n"
        "After the shortest-path distances are known, the remaining decision is choosing the best order to visit the relics before reaching the exit. \n"
        "Question 3: \n"
        "Different relic orders can produce different total fuel costs so the algorithm must search over possible orders to find the cheapest overall route."
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    sources = []
    for node in [spawn] + relics:
        if node not in sources:
            sources.append(node)
    return sources
    pass


def run_dijkstra(graph, source):
    nodes =set(graph.keys())
    for edges in graph.values():
        for neighbor, cost in edges:
            nodes.add(neighbor)
    nodes.add(source)

    dist= {node: float('inf') for node in nodes}
    dist[source] = 0

    heap = [(0, source)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > dist[current_node]:
            continue
        for neighbor, cost in graph.get(current_node, []):
            new_dist = current_dist + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist
    pass


def precompute_distances(graph, spawn, relics, exit_node):
    dist_table = {}
    for source in select_sources(spawn, relics, exit_node):
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table
    pass


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    return (
        "For nodes already finalized (in S): \n"
        "These nodes already store their true shortest-path distance from the source node. \n\n"
        "For nodes not yet finalized (not in S): \n"
        "These nodes currently store the best distance discovered so far but their values may still improve later. \n\n"
        "Initialization : why the invariant holds before iteration 1: \n"
        "The source node starts with distance 0 while all other nodes start at infinity.\n"
        "At this point, no incorrect distances have been finalized.\n\n"
        "Maintenance : why finalizing the min-dist node is always correct: \n"
        "The smallest tentative node can safely be finalized because all edge weights are nonnegative. \n"
        "Any later path reaching that node would not produce a smaller distance. \n\n"
        "Termination : what the invariant guarantees when the algorithm ends: \n"
        "When the algorithm finishes, every reachable node has the correct shortest-path distance stored in the table. \n\n"
        "Why This Matters for the Route Planner \n"
        "The recursive route planner depends on accurate shortest-path distances when comparing different relic orders because incorrect distances could cause the algorithm to choose a non-optimal route."
    )

# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    return (
        "**The failure mode:**\n"
        "A greedy strategy may choose the closet next relic without considering future travel costs. \n\n"
        "**Counter-example setup:**\n"
        "In the example, S to B costs 1 and S to C costs 2, but the later connections between relics affect the total route cost.\n\n"
        "**What greedy picks:**\n"
        "Greedy would likely to choose the nearest relic first because it only considers the next immediate move.\n\n"
        "**What optimal picks:**\n"
        "The optimal solution chooses the relic order with the minimum overall fuel cost.\n\n"
        "**Why greedy loses:**\n"
        "A locally cheap move can force more expensive travel later in the route.\n\n"
        "What the Algorithm Must Explore\n"
        "The algorithm must explore multiple relic orders because the best route depends on the entire order of decisions."
    )
        
    
# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    best = [float('inf'), []]
    relics_remaining = set(relics)
    relics_visited_order = []

    _explore(
        dist_table,
        spawn,
        relics_remaining,
        relics_visited_order,
        0,
        exit_node,
        best
    )
    return best[0], best[1]
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    # Pruning is safe because a branch is only stopped when its current cost
    # is already greater than or equal to the best route found.
    # Since all edge weights are nonnegative, contiuning that branch cannot
    # produce a cheaper route. 
    if cost_so_far >= best[0]:
        return
    
    if not relics_remaining:
        exit_cost = dist_table[current_loc].get(exit_node, float('inf'))
        total_cost = cost_so_far + exit_cost

        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = list(relics_visited_order)
        return
    
    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc].get(relic, float('inf'))

        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )
        relics_visited_order.pop()
        relics_remaining.add(relic)
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table,spawn, relics, exit_node)
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
