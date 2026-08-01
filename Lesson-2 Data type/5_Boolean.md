# Boolean Data Type

## What is a Boolean?

A **Boolean** data type stores only **two values**:

- `True`
- `False`

It is mainly used for **decision making** (`if`, `while`, comparisons, etc.).

---

## Creating a Boolean

```python
is_student = True
is_logged_in = False
```

---

## Check Type

```python
x = True

print(type(x))
```

Output

```python
<class 'bool'>
```

---

## Boolean from Comparisons

Comparison operators return a Boolean value.

```python
print(10 > 5)
```

Output

```python
True
```

```python
print(10 < 5)
```

Output

```python
False
```

---

## Boolean Values in Python

Internally,

```python
True  = 1
False = 0
```

Example:

```python
print(True + True)
print(False + True)
```

Output

```python
2
1
```

> ⭐ Useful to know for interviews, but don't overuse this in real code.

---

# Methods You Actually Need

There are **no special methods** to memorize for Boolean values at this stage.

Just remember:

- `True`
- `False`
- `type()`

---

# Interview Notes ⭐

- Boolean has only **two values**: `True` and `False`.
- `bool` is the datatype.
- Used in conditions (`if`, `while`) and comparisons.
- Internally, `True = 1` and `False = 0`.

---

# 30-Second Revision

- Boolean → `True` or `False`
- Datatype → `bool`
- Used for decision making
- Comparison operators return Boolean values
- `True = 1`, `False = 0`