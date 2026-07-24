# Numeric Data Types

Python provides **3 numeric data types**:

- `int` → Whole numbers
- `float` → Decimal numbers
- `complex` → Complex numbers

---

## 1. Integer (`int`)

Stores whole numbers.

```python
x = 5
print(type(x))
```

Output:

```python
<class 'int'>
```

---

## 2. Float (`float`)

Stores decimal numbers.

```python
y = 25.23
print(type(y))
```

Output:

```python
<class 'float'>
```

### Scientific Notation

```python
a = 3e4
print(a)
```

Output:

```python
30000.0
```

> `e` means **× 10ⁿ**.

Example:

- `3e4` → 3 × 10⁴ = 30000
- `2e3` → 2 × 10³ = 2000

---

## 3. Complex (`complex`)

Stores complex numbers.

```python
z = 4 + 3j
print(type(z))
```

Output:

```python
<class 'complex'>
```

---

# Useful Built-in Functions

## abs()

Returns the absolute (positive) value.

```python
x = -5

print(abs(x))
```

Output:

```python
5
```

---

## pow()

Returns the value of a number raised to a power.

```python
print(pow(2, 3))
```

Output:

```python
8
```

Equivalent to:

```python
2 ** 3
```

---

## round()

Rounds a number to the nearest integer.

```python
print(round(4.3))
print(round(4.6))
```

Output:

```python
4
5
```

### Important

Python uses **Banker's Rounding** when the decimal part is exactly `.5`.

```python
round(4.5)   # 4
round(5.5)   # 6
round(6.5)   # 6
round(7.5)   # 8
```

**Rule:**
- If the decimal is **less than .5** → round down.
- If the decimal is **greater than .5** → round up.
- If the decimal is **exactly .5** → round to the **nearest even integer**.

---

## max()

Returns the largest value.

```python
print(max(10, 20, 30))
```

Output:

```python
30
```

---

## min()

Returns the smallest value.

```python
print(min(10, 20, 30))
```

Output:

```python
10
```

---

## sum()

Returns the sum of all elements in an iterable.

```python
numbers = [10, 20, 30]

print(sum(numbers))
```

Output:

```python
60
```

---

# Quick Revision

- `int` → Whole numbers
- `float` → Decimal numbers
- `complex` → `a + bj`
- `abs()` → Absolute value
- `pow(a, b)` → a raised to the power b
- `round()` → Nearest integer (uses Banker's Rounding for `.5`)
- `max()` → Largest value
- `min()` → Smallest value
- `sum()` → Adds all elements of an iterable