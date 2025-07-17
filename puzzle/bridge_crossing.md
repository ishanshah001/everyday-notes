# Bridge Crossing Puzzle and Algorithm

I recently came across a classic puzzle that really caught my attention:

**Four people need to cross a bridge at night with one flashlight.**  
Only two can cross at a time, and the flashlight must always be carried.  
Each person walks at a different speed, and when two people cross together, they move at the slower person's pace.  
**What’s the minimum time needed to get everyone across?**

At first, it felt like a fun riddle. But then I started wondering if this can be generalized for *N* people?  
What if there were 6 people? Or 10? What’s the most efficient way?

This curiosity led me to a fascinating paper by Günter Rote titled **"Crossing the Bridge at Night"**.  
The paper dives deep into the problem and proves the optimal strategy using algorithmic thinking and graph theory.

---

## N = 4 (People: a, b, c, d)

There are two core strategies:

### Strategy 1: Fastest Person Returns

Steps:  
- a and b cross → time = b  
- a returns → time = a  
- a and c cross → time = c  
- a returns → time = a  
- a and d cross → time = d  

**Total time = 2a + b + c + d**

---

### Strategy 2: Group Two Slowest

Steps:  
- a and b cross → time = b  
- a returns → time = a  
- c and d cross → time = d  
- b returns → time = b  
- a and b cross → time = b  

**Total time = a + 3b + d**

---

## General Case for N ≥ 4

### Intuition

- The fastest two act like "shuttles" moving the flashlight back and forth.  
- The two slowest are sent together whenever possible to minimize their costly crossing times.  
- The recursive method ensures an optimal solution for any number of people.

The key is a **recursive strategy**:  
At each step, evaluate both approaches and choose the one with the lower cost.  
Then, reduce the group by **removing the two slowest who just crossed**, and repeat.

Eventually, the recursion reaches a base case (such as 2 or 3 people), which can be solved directly.

---

What looks like a simple puzzle turns out to be a study in greedy strategies, recursion, and optimization.

If you are interested in problem solving, algorithms, or graph theory, this one is worth exploring.

---
**Code:** [Bridge crossing](./bridge_cossing.py)
**Paper:** [Crossing the Bridge at Night by Günter Rote](https://www.researchgate.net/publication/220530399_Crossing_the_Bridge_at_Night)