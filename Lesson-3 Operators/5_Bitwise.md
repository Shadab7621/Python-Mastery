# Bitwise Operators

Bitwise operators perform operations on the **binary (bits)** representation of numbers.

Before applying a bitwise operator, Python converts the numbers into binary.

---

# Decimal to Binary

## Whole Numbers

To convert a whole number to binary:

- Divide the number by **2** repeatedly.
- Write down the remainder after each division.
- Read the remainders **from bottom to top**.

### Example 1

Convert **10** to binary.

| Division | Remainder |
|----------|-----------|
|10 ÷ 2 = 5|0|
|5 ÷ 2 = 2|1|
|2 ÷ 2 = 1|0|
|1 ÷ 2 = 0|1|

Answer

```text
10 = 1010₂
```

---

### Example 2

Convert **13** to binary.

| Division | Remainder |
|----------|-----------|
|13 ÷ 2 = 6|1|
|6 ÷ 2 = 3|0|
|3 ÷ 2 = 1|1|
|1 ÷ 2 = 0|1|

Answer

```text
13 = 1101₂
```

---

## Decimal (Fractional) Numbers

To convert the fractional part:

- Multiply the fraction by **2**.
- Write the integer part.
- Continue with the remaining fraction.

### Example 3

Convert **0.625** to binary.

| Multiplication | Integer Part |
|---------------|--------------|
|0.625 × 2 = 1.25|1|
|0.25 × 2 = 0.5|0|
|0.5 × 2 = 1.0|1|

Answer

```text
0.625 = 0.101₂
```

---

# Bitwise AND (`&`)

Bitwise AND compares each pair of bits.

Rules

```text
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
```

Example

```text
5 = 101
3 = 011
```

```
  101
& 011
-----
  001
```

```python
print(5 & 3)
```

Output

```python
1
```

---

# Bitwise OR (`|`)

Bitwise OR compares each pair of bits.

Rules

```text
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
```

Example

```text
5 = 101
3 = 011
```

```
  101
| 011
-----
  111
```

```python
print(5 | 3)
```

Output

```python
7
```

---

# Floating Point Precision

```python
print(0.9 - 3 * 0.3)
```

Output

```python
5.551115123125783e-17
```

instead of

```python
0
```

### Why?

Some decimal numbers (like **0.1**, **0.2**, **0.3**) cannot be represented exactly in binary.

Python stores the **closest possible binary value**, so after calculations a very small error remains.

This is called **Floating Point Precision Error**.

---

# Operators You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `&`
- `|`

---

# Interview Notes ⭐

- Bitwise operators work on **binary numbers**.
- `&` returns **1** only if both bits are **1**.
- `|` returns **1** if at least one bit is **1**.
- Floating-point numbers may have small precision errors because they are stored in binary.

---

# 30-Second Revision

- Bitwise operators work on binary.
- `&` → Bitwise AND
- `|` → Bitwise OR
- Divide by **2** → Convert whole number to binary.
- Multiply by **2** → Convert fractional part to binary.
- `0.9 - 3 × 0.3 ≠ 0` due to floating-point precision.