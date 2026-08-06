# Logical Operators

Logical operators are used to **combine or modify conditions**.

The result is always **True** or **False**.

Python has **three logical operators**:

- `and`
- `or`
- `not`

---

## AND (`and`)

Returns **True** only if **both conditions are True**.

Syntax

```python
condition1 and condition2
```

Example

```python
x = 10

print(x > 5 and x < 20)
```

Output

```python
True
```

Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

> **Rule:** If **even one condition is False**, the result is **False**.

---

## OR (`or`)

Returns **True** if **at least one condition is True**.

Syntax

```python
condition1 or condition2
```

Example

```python
x = 10

print(x > 20 or x < 15)
```

Output

```python
True
```

Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

> **Rule:** If **at least one condition is True**, the result is **True**.

---

## NOT (`not`)

Reverses (flips) the result.

Syntax

```python
not condition
```

Example

```python
x = 10

print(not (x > 5))
```

Output

```python
False
```

Because

```python
x > 5
```

is

```python
True
```

and

```python
not True
```

becomes

```python
False
```

---

# Quick Examples

```python
print(True and True)      # True
print(True and False)     # False

print(True or False)      # True
print(False or False)     # False

print(not True)           # False
print(not False)          # True
```

---

# Operators You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `and`
- `or`
- `not`

---

# Interview Notes ⭐

- Logical operators work with **Boolean values** (`True` and `False`).
- `and` → All conditions must be `True`.
- `or` → At least one condition must be `True`.
- `not` → Flips the Boolean value.

---

# 30-Second Revision

- `and` → Both must be `True`
- `or` → Any one can be `True`
- `not` → Flips `True` ↔ `False`
- Result is always **True** or **False**