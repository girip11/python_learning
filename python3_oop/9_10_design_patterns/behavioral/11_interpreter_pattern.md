# Interpreter Design Pattern

The Interpreter pattern defines a grammatical representation for a language and an interpreter to interpret the grammar.

> The Interpreter pattern discusses: defining a domain language (i.e. problem characterization) as a simple language grammar, representing domain rules as language sentences, and interpreting these sentences to solve the problem. The pattern uses a class to represent each grammar rule. And since grammars are usually hierarchical in structure, an inheritance hierarchy of rule classes maps nicely.

## Structure

> Interpreter suggests modeling the domain with a recursive grammar. Each rule in the grammar is either a 'composite' (a rule that references other rules) or a terminal (a leaf node in a tree structure). Interpreter relies on the recursive traversal of the Composite pattern to interpret the 'sentences' it is asked to process.

**NOTE**: **This pattern doesn't address parsing**. When the grammar is very complex, other techniques (such as a parser) are more appropriate.

---

## References

- [Interpreter Design Pattern](https://sourcemaking.com/design_patterns/interpreter)
