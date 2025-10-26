# MIT 6.824 — Lecture 1: Introduction to Distributed Systems

## 1. What is a Distributed System?

A **distributed system** is a set of cooperating computers communicating over a network to achieve a common goal.

### Examples
- Distributed storage (e.g., GFS, S3)
- Large-scale computations (e.g., MapReduce)
- Peer-to-peer systems (e.g., file sharing)

### Why Build Distributed Systems?
1. **Performance / Parallelism**
   - To achieve higher throughput by leveraging multiple CPUs, disks, and memory in parallel.
2. **Fault Tolerance**
   - To tolerate failures by replicating computations or data across multiple nodes.
3. **Geographical Distribution**
   - To coordinate between physically distant entities (e.g., global banking systems).
4. **Security Isolation**
   - To separate untrusted components or computations for safety.

> If a problem can be solved on a single computer, it’s usually better to do so. Distributed systems are inherently more complex.

---

## 2. Why Distributed Systems are Hard

1. **Concurrency**
   - Multiple nodes execute simultaneously, introducing timing dependencies.
2. **Partial Failures**
   - Some components can fail while others continue to operate, leading to inconsistent system states.
3. **Performance Challenges**
   - Achieving expected speed-up is non-trivial due to communication, coordination, and contention.

---

## 3. Course Overview

### Components
- **Lectures:** Conceptual foundations and case studies.
- **Readings:** Classic and modern distributed systems papers.
- **Labs:** Practical implementation of distributed systems.
- **Exams:** Midterm and final exam.
- **Optional Project:** Replace Lab 4 with a team-based distributed system project.

### Lab Sequence
| Lab | Focus | Description |
|------|--------|-------------|
| 1 | MapReduce | Implement a simple MapReduce framework. |
| 2 | Fault Tolerance | Implement Raft consensus algorithm. |
| 3 | Replicated KV Store | Build a fault-tolerant key/value store using Raft. |
| 4 | Sharding | Implement sharded, fault-tolerant KV store for parallelism. |

---

## 4. Infrastructure for Applications

Distributed systems act as **infrastructure** for higher-level applications, providing:
- **Storage**
- **Communication**
- **Computation**

### Design Goal
To hide distributed complexity from the application layer and expose **simple abstractions**:
- Appears like a single, local system.
- Internally distributed, fault-tolerant, and scalable.

> Example: A distributed storage system that behaves like a simple key-value store or file system.

---

## 5. Major Themes in Distributed Systems

### 5.1 Implementation Tools
- **RPC (Remote Procedure Call):** Abstracts inter-machine communication.
- **Threads:** Enables concurrency and parallelism.
- **Locks:** Coordinates concurrent access to shared resources.

### 5.2 Scalability
- **Definition:** Doubling the number of machines should (ideally) double throughput.
- **Goal:** Linear speed-up — performance grows proportionally with added resources.

#### Example: Web Service Architecture
- Users → Web Servers → Database
- Scaling web servers improves performance until the **database** becomes the bottleneck.
- Solution: **Partitioning / Sharding** data and adding more databases.

---

### 5.3 Fault Tolerance
With thousands of machines, some component will **always** be failing.

#### Key Concepts
- **Availability:** System continues to function despite some failures.
- **Recoverability:** System can restart and recover state after repair.
- **Replication:** Keeps multiple copies of data to tolerate failures.
- **Non-Volatile Storage:** Persistent storage for recovery after crashes.

#### Techniques
- **Checkpointing:** Save system state periodically.
- **Replication Management:** Keep copies consistent across nodes.

---

### 5.4 Consistency

#### Example: Key-Value Store
- Operations: `put(key, value)` and `get(key)`
- Challenge: Multiple copies of data (replicas) may become inconsistent.

#### Consistency Models
| Type | Description |
|------|--------------|
| **Strong Consistency** | Every read returns the result of the latest write. |
| **Weak Consistency** | Reads may return stale data. |
| **Eventual Consistency** | All replicas converge to the same state eventually. |

#### Tradeoff
- **Strong consistency** requires coordination across replicas → **high latency**.
- **Weak consistency** improves performance but sacrifices immediacy.

#### Real-World Challenge
- Replicas placed far apart (for fault tolerance) → long communication delays.
- Network latency limits strong consistency in geo-distributed systems.

---

## 6. Key Trade-offs in Distributed Systems

| Goal | Often Conflicts With |
|------|----------------------|
| Scalability | Strong Consistency |
| Fault Tolerance | Performance |
| Simplicity | Flexibility |

Building distributed systems requires balancing these constraints.

---

## 7. Case Study: MapReduce (Google, 2004)

### Motivation
Google needed to process **terabytes of web data** efficiently on thousands of machines.

### Problem
Running large-scale computations manually required distributed systems expertise.

### Solution
**MapReduce Framework**:
- Allows programmers to define two functions: **Map** and **Reduce**.
- System handles:
  - Data distribution
  - Parallel execution
  - Fault tolerance

### Workflow
1. **Input Splitting:** Data divided into multiple chunks.
2. **Map Phase:** Each map worker processes a chunk and emits (key, value) pairs.
3. **Shuffle Phase:** Framework groups all values by key.
4. **Reduce Phase:** Reduce workers aggregate all values for each key.
5. **Output:** Written to a distributed file system (e.g., GFS).

### Example: Word Count
- **Map:** For each word → emit `(word, 1)`
- **Reduce:** For each word → sum all counts

### Advantages
- Simplifies programming large-scale jobs.
- Provides fault tolerance and scalability transparently.

### Limitations
- Designed for **batch processing**, not streaming.
- Requires multiple MapReduce stages for complex pipelines.

---

## 8. Design Lessons from MapReduce

1. **Data Locality**
   - Schedule computation on nodes that already store the required input.
2. **Network Bottlenecks**
   - Minimize cross-rack data transfers.
3. **Fault Recovery**
   - Re-run failed tasks automatically.
4. **Abstraction**
   - Simplified interface enables non-experts to utilize distributed systems.

---

## 9. Summary of Core Distributed Systems Principles

| Principle | Description |
|------------|-------------|
| **Performance via Parallelism** | Distribute workload across many nodes. |
| **Fault Tolerance** | Use replication and recovery mechanisms. |
| **Scalability** | Increase throughput by adding nodes. |
| **Consistency** | Define and manage how updates propagate. |
| **Abstraction** | Hide distributed complexity from users. |

---

## 10. Key Takeaways

- Distributed systems enable scale, reliability, and performance.
- They introduce complexity due to concurrency, failures, and coordination.
- Core design goals: **Scalability, Fault Tolerance, Consistency, and Abstraction.**
- Frameworks like **MapReduce** demonstrate how well-chosen abstractions simplify distributed computing.