# Jargon Explainer Reference

## Extended Analogy Bank

| Tech concept | Analogy |
|---|---|
| API | A waiter: you tell them what you want, they go to the kitchen (the system) and bring back the result — you never see how the kitchen works |
| DevOps | When the architects and the builders work in the same team instead of throwing plans over a wall |
| Refactoring | Reorganising your wardrobe without buying new clothes — same items, much easier to find things |
| Agile | Building a house room by room and asking the family if they like it before moving to the next room |
| Technical debt | Borrowing time now by cutting corners — you'll pay it back later, with interest |
| Containerisation | Shipping containers: the goods inside don't change but they can travel by ship, train or truck without repacking |
| Load balancer | A supermarket manager who opens a new checkout when queues get too long |
| Cache | The sticky notes on your monitor — faster to glance at than to open the file again |
| Microservices | A food court: each stall specialises in one thing and works independently, unlike a single restaurant doing everything |
| CI/CD | A factory conveyor belt that checks each part automatically before it goes into the final product |
| Cloud | Renting a car instead of owning one — pay for what you use, someone else handles maintenance |
| Encryption | A lock-and-key system where only the right key can read the message, even if someone intercepts the letter |

---

## Bad Explanation Patterns to Avoid

| Anti-pattern | Example | Why it fails |
|---|---|---|
| Defining with the same word | "Microservices is a service-based architecture" | Circular — doesn't help |
| Pure abstraction | "It abstracts the complexity of distributed systems" | Nobody knows what "abstract" means here |
| Too many qualifiers | "It's sort of like, in a way, similar to..." | Signals you're not sure yourself |
| Acronym soup | "It enables SRE teams to manage SLOs via IaC" | Replaces one wall of jargon with another |
| Completeness over clarity | Covering every edge case in the explanation | An explanation isn't a spec — pick the core 80% |

---

## Scoring Rubric (used by the demo agent)

| Dimension | What to check | Score |
|---|---|---|
| **Jargon-free** | No unexplained technical terms | /3 |
| **Has an analogy** | At least one concrete real-world comparison | /3 |
| **Problem-first** | Opens with the problem, not the definition | /2 |
| **One-sentence core** | The essence fits in a single clear sentence | /2 |

**Total: /10**

A score of 7+ means someone outside IT could walk away understanding the concept.
Below 5 means the Wikipedia version is not meaningfully clearer.
