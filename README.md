# The Torchbearer

**Student Name:** Bao Do 
**Student ID:** 131987229
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
A single shortest-path run from S is not enough because it's only gives the cheapest cost from S to every reachable node. It does not determine which order the relics should be collected in. 

- **What decision remains after all inter-location costs are known:**
After the shortest-path distances are known, the remaining decision is choosing the best order to visit the relics before reaching the exit. 

- **Why this requires a search over orders (one sentence):**
Different relic orders can produce different total fuel costs so the algorithm must search over possible orders to find the cheapest overall route. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| spawn | The route always starts from the spawn node so shortest-path distances are needed from this location |
| relic | After collecting a relic, the next section of the route begins from that relic node |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary |
| What the keys represent | Outer keys represent source nodes, and inner keys represent destination nodes |
| What the values represent | The values store the minimum fuel cost between two nodes |
| Lookup time complexity | O(1) average case |
| Why O(1) lookup is possible | Python dictionaries are implemented using hash tables, which allow constant average-time lookup operations |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** k + 1
- **Cost per run:** O(m log n)
- **Total complexity:** O((k + 1) m log n)
- **Justification (one line):** Dijkstra is run from the spawan node and each relic node to avoid repeated shortest-path computations during recursive search

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
These nodes already store their true shortest-path distance from the source node. 

- **For nodes not yet finalized (not in S):**
These nodes currently store the best distance discovered so far but their values may still improve later. 

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
The source node starts with distance 0 while all other nodes start at infinity.
At this point, no incorrect distances have been finalized.

- **Maintenance : why finalizing the min-dist node is always correct:**
The smallest tentative node can safely be finalized because all edge weights are nonnegative.
Any later path reaching that node would not produce a smaller distance.

- **Termination : what the invariant guarantees when the algorithm ends:**
When the algorithm finishes, every reachable node has the correct shortest-path distance stored in the table.

### Part 3c: Why This Matters for the Route Planner

The recursive route planner depends on accurate shortest-path distances when comparing different relic orders because incorrect distances could cause the algorithm to choose a non-optimal route. 


---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** A greedy strategy may choose the closet next relic without considering future travel costs. 
- **Counter-example setup:** In the example, S to B costs 1 and S to C costs 2, but the later connections between relics affect the total route cost.
- **What greedy picks:** Greedy would likely to choose the nearest relic first because it only considers the next immediate move. 
- **What optimal picks:** The optimal solution chooses the relic order with the minimum overall fuel cost. 
- **Why greedy loses:** A locally cheap move can force more expensive travel later in the route. 

### What the Algorithm Must Explore

- The algorithm must explore multiple relic orders because the best route depends on the entire order of decisions. 

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | `current_loc` | node | The node the search is currently at. |
| Relics already collected | `relics_visited_order` | list | The relics collected so far in order. |
| Fuel cost so far | `cost_so_far` | float/int | The fuel cost used so far. |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | Set, using `relics_remaining` |
| Operation: check if relic already collected | Time complexity: O(1) average case |
| Operation: mark a relic as collected | Time complexity: O(1) average case |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) average case |
| Why this structure fits | A set makes it easy to remove a relic before recursion and add it back during backtracking. |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** `k!`
- **Why:** With k relics, the algorithm may need to try every possible relic order. 

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** The algorithm tracks the best total fuel cost found so far and the relic order for that route.
- **When it is used:** It is used during recursion to compare complete routes and stop branches that cannot improve the current best route. 
- **What it allows the algorithm to skip:** It allows the algorithm to skip branches where the current cost is already greater than or equal to the best route found. 

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** The algorithm knows the current location, remaining relics, cost so far, exit node and distance table. 
- **What the lower bound accounts for:** This implementation uses cost_so_far as a simple lower bound for the current branch. 
- **Why it never overestimates:** Since edge weights are nonnegative, the final route cost can only stay the same or increase from cost_so_far. 

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- Prunning is safe because a branch is only stopped when its current cost is already greater than or equal to the best route found. 
- Since all edge weights are nonnegative, contiuning that branch cannot produce a cheaper route. 

---

## References

> Bullet list. If none beyond lecture notes, write that.

- Lecture notes 
