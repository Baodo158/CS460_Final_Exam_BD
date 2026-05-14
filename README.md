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

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
