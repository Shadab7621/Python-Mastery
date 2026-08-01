# Type Casting

## What is Type Casting?

**Type Casting** is the process of converting one data type into another.

Python provides **two types** of type casting:

1. Implicit Type Casting
2. Explicit Type Casting

---

# 1. Implicit Type Casting

Python automatically converts one data type into another when needed.

Example

```python
x = 5
y = 4.5

result = x + y

print(result)
print(type(result))
```

Output

```python
9.5
<class 'float'>
```

> Here, Python automatically converts `5` (int) to `5.0` (float), so the result is a `float`.

---

# 2. Explicit Type Casting

The programmer manually converts the data type using built-in functions.

---

## int()

Converts a value to an integer.

```python
x = int(4.8)

print(x)
```

Output

```python
4
```

---

## float()

Converts a value to a float.

```python
x = float(10)

print(x)
```

Output

```python
10.0
```

---

## str()

Converts a value to a string.

```python
x = str(100)

print(x)
print(type(x))
```

Output

```python
100
<class 'str'>
```

---

# Invalid Type Casting

Not every conversion is possible.

Example

```python
int("Python")
```

Output

```python
ValueError
```

Because `"Python"` is **not a valid integer**.

> ✅ Numeric strings can be converted.

```python
int("123")
```

Output

```python
123
```

---

# When Do We Use Type Casting?

- Convert user input to numbers.
- Perform mathematical operations.
- Convert data into the required format.

Example

```python
age = int(input("Enter your age: "))
```

---

# Methods You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `int()`
- `float()`
- `str()`

That's all for now.

---

# Interview Notes ⭐

- Type casting = Converting one data type into another.
- **Implicit** → Done automatically by Python.
- **Explicit** → Done manually by the programmer.
- `input()` always returns a string, so type casting is often required.
- Invalid conversions raise an error.

---

# 30-Second Revision

- Type Casting = Data type conversion
- Implicit → Automatic
- Explicit → Manual
- `int()` → Integer
- `float()` → Float
- `str()` → String
- `int("123")` ✅
- `int("Python")` ❌ (`ValueError`)