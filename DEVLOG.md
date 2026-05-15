# Development Log – The Torchbearer

**Student Name:** Bao Do
**Student ID:** 131987229

---

## Entry 1 – [05/11/2026]: Initial Plan

My plan is to start with Dijkstra, then make the distance table and do the recursive search after that. I think the search and pruning part will probably be the hardest part so I plan to test the code after each main step. 

---

## Entry 2 – [05/12/2026]: [Dijkstra and Distance Table]

I implemented select_sources, run_dijkstra and precompute_distances first. The main design decision was to only run Dijkstra from locations that are actually important to the route, which are the spawn node and each relic node.

This reduced unnecessary repeated shortest-path computations during the recursive search later. I also used a nested dictionary structure for the distance table so the search could access shortest-path costs with constant average-time lookup. 

---

## Entry 3 – [5/13/2026]: [Search Bug / Design Change]

While working on _explore, my first version only tracked the minimum fuel cost during recursion. Later, I realized this was not enough because the assignment also required returning the actual relic collection order.

To fix this, I added relics_visted_order to the recursive state. When a relic is chosen, it is removed from relics_remaining and appended to relics_visited_order, then after the recursive call the changes are undone using backtracking so other possible relic orders can still be explored correctly. 

---

## Entry 4 – [5/14/2026]: Post-Implementation Reflection

After finishing the implementation, I tested the shortest-path and recursive search functions using the provided test graphs to make sure the algorithm retunred both the correct fuel cost and correct relic order. I also checked cases where paths were unreachable to verify that the program handled float('inf') correctly. 

If I had more time, I would add more test graphs with larger numnbers of relics and improve the pruning strategy so the recursive search could skip more unncessary branches. 

---

## Final Entry – [05/14/2026]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 45 |
| Part 2: Precomputation Design | 120 |
| Part 3: Algorithm Correctness | 50 |
| Part 4: Search Design | 40 |
| Part 5: State and Search Space | 120 |
| Part 6: Pruning | 110 |
| Part 7: Implementation | 100 |
| README and DEVLOG writing | 90 |
| **Total** | 675 |
