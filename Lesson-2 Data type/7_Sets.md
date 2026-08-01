# Sets

## What is a Set?

A **set** is an unordered collection of **unique** elements.

```python
numbers = {1, 2, 3, 4}
```

---

## Properties

- Unique elements only (No duplicates) ✅
- Unordered (No indexing) ✅
- Mutable ✅
- Can store different data types (Heterogeneous) ✅

Example

```python
s = {1, "Python", 3.14, True}
```

---

# Creating a Set

Using `{}`

```python
numbers = {10, 20, 30}
```

---

## Empty Set

```python
s = set()

print(s)
```

Output

```python
set()
```

> **Note:** `{}` creates an **empty dictionary**, not an empty set.

---

## Using `set()` Constructor

Create a set from another iterable.

### From another Set

```python
s1 = {1, 2, 3}

s2 = set(s1)

print(s2)
```

Output

```python
{1, 2, 3}
```

You can also create a set from a list, tuple, or string.

---

# Adding Elements

## add()

Adds a single element.

```python
numbers = {1, 2, 3}

numbers.add(4)
```

---

# Removing Elements

## discard()

Removes an element if it exists.

```python
numbers.discard(2)
```

If the element is not present, **no error** is raised.

---

## remove()

Removes an element.

```python
numbers.remove(2)
```

If the element is not present, Python raises a **KeyError**.

---

# discard() vs remove() ⭐

| discard() | remove() |
|-----------|----------|
| No error if element is missing | Raises `KeyError` if element is missing |
| Safer | Use when you're sure the element exists |

---

# Frozen Set

A **frozenset** is an **immutable set**.

Once created, its elements cannot be added or removed.

```python
fs = frozenset({1, 2, 3})

print(fs)
```

---

# Methods You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `add()`
- `discard()`
- `remove()`

⭐⭐⭐ Good to Know

- `frozenset()`

---

# Interview Notes ⭐

- Sets store **unique** elements.
- Sets are **unordered**, so indexing is **not supported**.
- Sets are mutable.
- `{}` creates an empty **dictionary**.
- Use `set()` to create an empty set.
- `discard()` does **not** raise an error if the element is missing.
- `remove()` **does** raise a `KeyError`.
- `frozenset` is immutable.

---

# 30-Second Revision

- Unique elements
- Unordered
- Mutable
- `set()` → Empty set
- `add()` → Add element
- `discard()` → Remove safely
- `remove()` → Remove (raises error if missing)
- `frozenset()` → Immutable set