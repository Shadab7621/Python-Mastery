# Comparison Operators

Comparison operators are used to compare two values.

The result is always either **True** or **False**.

---

## Given

```python
x = 5
y = 10
```

---

## Equal To (`==`)

Checks whether two values are equal.

```python
print(x == y)
```

Output

```python
False
```

---

## Not Equal To (`!=`)

Checks whether two values are different.

```python
print(x != y)
```

Output

```python
True
```

---

## Greater Than (`>`)

Checks if the left value is greater than the right value.

```python
print(x > y)
```

---

## Less Than (`<`)

Checks if the left value is smaller than the right value.

```python
print(x < y)
```

---

## Greater Than or Equal To (`>=`)

```python
print(x >= y)
```

---

## Less Than or Equal To (`<=`)

```python
print(x <= y)
```

---

# Comparison with NaN

```python
x = float("nan")
y = x

print(x == y)
```

Output

```python
False
```

### Why?

`NaN` stands for **Not a Number**.

It represents an **undefined or unknown** numeric value.

Since an unknown value cannot be guaranteed to be equal to anything, even itself,

```python
float("nan") == float("nan")
```

always returns

```python
False
```

> **Remember:** `NaN` is never equal to any value, including itself.

---

# Operators You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

---

# Interview Notes ⭐

- Comparison operators always return **True** or **False**.
- `==` checks value equality.
- `!=` checks inequality.
- `NaN` is **never equal** to itself.

---

# 30-Second Revision

- `==` → Equal
- `!=` → Not Equal
- `>` → Greater Than
- `<` → Less Than
- `>=` → Greater Than or Equal To
- `<=` → Less Than or Equal To
- Result is always **True** or **False**