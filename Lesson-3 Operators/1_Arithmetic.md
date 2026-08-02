# Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

---

## Given

```python
x = 5
y = 10
```

---

## Addition (`+`)

Adds two numbers.

```python
print(x + y)
```

---

## Subtraction (`-`)

Subtracts one number from another.

```python
print(x - y)
```

---

## Multiplication (`*`)

Multiplies two numbers.

```python
print(x * y)
```

---

## Division (`/`)

Performs normal division.

```python
print(x / y)
```

> **Note:** `/` always returns a **float**.

Example:

```python
10 / 2      # 5.0
```

---

## Floor Division (`//`)

Returns the **floor value** of the division.

```python
print(10 // 3)
```

Output

```python
3
```

> **Note:** `//` performs **floor division** (rounds down to the nearest whole number).

Example:

```python
7 // 2      # 3
9 // 4      # 2
```

---

## Modulus (`%`)

Returns the remainder after division.

```python
print(10 % 3)
```

Output

```python
1
```

### Check if a Number is Even

```python
num = int(input("Enter a number: "))

print(num % 2 == 0)
```

Output

```python
True
```

or

```python
False
```

> If the remainder is `0`, the number is **even**.

---

## Exponent (`**`)

Calculates the power of a number.

```python
print(2 ** 3)
```

Output

```python
8
```

---

# Positive & Negative Infinity

Python can represent infinity using `float()`.

```python
positive_inf = float("inf")
negative_inf = float("-inf")

print(positive_inf)
print(negative_inf)
```

Output

```python
inf
-inf
```

---

# NaN (Not a Number)

`NaN` represents an undefined or invalid numerical result.

Example

```python
nan = float("nan")

print(nan)
```

Output

```python
nan
```

Another example:

```python
import math

print(math.sqrt(-1))
```

This raises an error because the square root of a negative number is not a real number.

Some libraries (like NumPy) use `NaN` to represent missing or undefined numeric values.

---

# Operators You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `+`
- `-`
- `*`
- `/`
- `//`
- `%`
- `**`

---

# Interview Notes ⭐

- `/` always returns a **float**.
- `//` performs **floor division**.
- `%` returns the remainder.
- `**` is used for exponentiation.
- `float("inf")` represents positive infinity.
- `float("-inf")` represents negative infinity.
- `NaN` means **Not a Number** and represents an undefined numeric value.

---

# 30-Second Revision

- `+` → Addition
- `-` → Subtraction
- `*` → Multiplication
- `/` → Division (float)
- `//` → Floor Division
- `%` → Remainder
- `**` → Power
- `float("inf")` → Infinity
- `float("nan")` → Not a Number