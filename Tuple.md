# Tuples

## What is a Tuple?

A **tuple** is an ordered, immutable collection that can store multiple values of different data types.

```python
t = (10, "Python", 3.14, True)
```

---

## List vs Tuple ⭐

| List | Tuple |
|------|-------|
| Mutable ✅ | Immutable ❌ |
| Uses `[]` | Uses `()` |
| Can add, remove or modify elements | Cannot modify elements after creation |
| Slightly slower | Slightly faster |

> **Rule of Thumb:** Use a **list** when data needs to change, and a **tuple** when data should remain constant.

---

## Properties

- Ordered ✅
- Immutable ✅
- Allows duplicate values ✅
- Accessed using index ✅

---

# Creating a Tuple

Using parentheses

```python
t = (1, 2, 3, 4)
```

---

## Using `tuple()` Constructor

### From a List

```python
l = [1, 2, 3]

t = tuple(l)
```

---

### From a String

```python
t = tuple("Sam")

print(t)
```

Output

```python
('S', 'a', 'm')
```

---

# Single Element Tuple ⭐

This is **NOT** a tuple.

```python
t = (34)
```

Output

```python
<class 'int'>
```

Correct way:

```python
t = (34,)
```

Output

```python
<class 'tuple'>
```

> A comma `,` is required for a single-element tuple.

---

# Tuple Methods

## count()

Returns how many times an element appears.

```python
t = (1, 2, 2, 3)

print(t.count(2))
```

Output

```
2
```

---

## index()

Returns the index of the first occurrence.

```python
t = (10, 20, 30)

print(t.index(20))
```

Output

```
1
```

---

# Useful Built-in Functions

## len()

Returns the number of elements.

```python
print(len(t))
```

---

# Accessing Elements

Use indexing.

```python
t = (10, 20, 30)

print(t[1])
```

Output

```
20
```

Negative indexing also works.

```python
print(t[-1])
```

---

# Updating Elements

Tuples are immutable.

```python
fruits = ("Apple", "Banana", "Orange")

fruits[1] = "Mango"
```

Output

```
TypeError
```

---

# Slicing

Slicing works exactly like lists.

```python
t = (10, 20, 30, 40, 50)

print(t[1:4])
```

Output

```
(20, 30, 40)
```

Rule:

- Start → Included ✅
- End → Excluded ❌

---

# Methods You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `len()`
- `count()`
- `index()`

That's it!

Unlike lists, tuples have **only two built-in methods**.

---

# Interview Notes ⭐

- Tuples are **immutable**.
- Use `()` to create tuples.
- A single-element tuple **must** have a comma.
- Tuples support indexing and slicing.
- Tuples have only **two methods**: `count()` and `index()`.

---

# 30-Second Revision

- Ordered & Immutable
- Uses `()`
- Can store different data types
- Single element → `(value,)`
- `count()` → Count occurrences
- `index()` → Find first index
- `len()` → Number of elements
- Supports indexing & slicing