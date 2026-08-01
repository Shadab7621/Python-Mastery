# Lists

## What is a List?

A **list** is an ordered, mutable collection that can store multiple values of different data types.

### Properties

- Ordered ✅
- Mutable (can be changed) ✅
- Allows duplicate values ✅
- Accessed using index ✅

---

# Creating a List

### Using `[]`

```python
numbers = [10, 20, 30]
```

### Using `list()` Constructor

```python
numbers = list([10, 20, 30])
```

### From a String

```python
name = list("Sam")

print(name)
```

Output

```python
['S', 'a', 'm']
```

### From a Tuple

```python
t = (1, 2, 3)

l = list(t)

print(l)
```

Output

```python
[1, 2, 3]
```

### Check Type

```python
numbers = [1, 2, 3]

print(type(numbers))
```

Output

```python
<class 'list'>
```

---

# Quick Comparison

## String

```python
name = "Sam"
```

Ordered ✅ | Immutable ❌

---

## List

```python
numbers = [1, 2, 3]
```

Ordered ✅ | Mutable ✅

---

## Tuple

```python
numbers = (1, 2, 3)
```

Ordered ✅ | Immutable ❌

---

# Accessing Elements

### Positive Index

Access element using its index.

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Output

```python
20
```

---

### Negative Index

Starts from the end.

```python
numbers = [10, 20, 30]

print(numbers[-1])
```

Output

```python
30
```

---

### Index Range

Positive Index

```
0 → n-1
```

Negative Index

```
-1 → Last Element
-n → First Element
```

---

# Adding Elements

## append()

Adds an element at the end.

```python
numbers.append(40)
```

---

## insert()

Adds an element at a specific index.

```python
numbers.insert(1, 15)
```

> Elements after that index shift one position to the right.

---

## extend()

Adds multiple elements from another iterable.

```python
numbers.extend([40, 50, 60])
```

---

# Removing Elements

## remove()

Removes the first occurrence of a value.

```python
numbers.remove(20)
```

If duplicates exist, only the **first occurrence** is removed.

---

## pop()

Removes and returns an element.

Last element

```python
numbers.pop()
```

Specific index

```python
numbers.pop(2)
```

---

# Updating Elements

Replace a value.

```python
numbers[1] = 100
```

---

# Slicing

Replace multiple values.

```python
numbers[1:3] = [50, 60]
```

### Slice Rule

```
[start : end]
```

- Start → Included ✅
- End → Excluded ❌

Example

```python
numbers[1:4]
```

Returns

```
Index 1, 2, 3
```

---

# reverse()

Reverses the list.

```python
numbers.reverse()
```

---

# copy()

Creates a copy of the list.

```python
new_list = numbers.copy()
```

---

# sort()

Sorts the list in ascending order.

```python
numbers.sort()
```

Descending order

```python
numbers.sort(reverse=True)
```

---

# Which Method Should I Use?

| Task | Method |
|------|---------|
| Add one element at end | `append()` ⭐ |
| Add at specific index | `insert()` |
| Add multiple elements | `extend()` ⭐ |
| Remove by value | `remove()` |
| Remove by index | `pop()` ⭐ |
| Replace element | `list[index] = value` ⭐ |
| Reverse list | `reverse()` |
| Copy list | `copy()` ⭐ |
| Sort list | `sort()` ⭐ |

⭐ = Most commonly used in real projects.

---

# Interview Notes

- Lists are **mutable**.
- Lists preserve insertion order.
- Lists allow duplicate values.
- `remove()` removes by **value**.
- `pop()` removes by **index**.
- `append()` adds one element.
- `extend()` adds multiple elements.
- Slicing includes the **start** index and excludes the **end** index.

---

# 30-Second Revision

- Ordered & Mutable
- `[]` or `list()`
- Positive & Negative Indexing
- `append()` → End
- `insert()` → Specific index
- `extend()` → Multiple elements
- `remove()` → By value
- `pop()` → By index
- `reverse()` → Reverse list
- `copy()` → Duplicate list
- `sort()` → Sort list