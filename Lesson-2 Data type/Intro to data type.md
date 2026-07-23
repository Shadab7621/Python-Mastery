# Data Types

## What is a Data Type?

A **data type** tells Python what kind of value a variable stores.

Example:

```python
age = 20
name = "Shadab"
```

Here,
- `20` is an **Integer**
- `"Shadab"` is a **String**

---

## Types of Data in Python

### 1. Numeric
Used to store numbers.

- `int` → Whole numbers
- `float` → Decimal numbers
- `complex` → Complex numbers

Example:

```python
age = 20
pi = 3.14
z = 2 + 3j
```

---

### 2. Sequence
Used to store multiple values in an order.

- `str` (String)
- `list`
- `tuple`

Example:

```python
name = "Shadab"
marks = [90, 85, 88]
colors = ("Red", "Blue")
```

---

### 3. Boolean

Stores only two values.

- `True`
- `False`

Example:

```python
is_student = True
```

---

### 4. Dictionary (`dict`)

Stores data as **key : value** pairs.

Example:

```python
student = {
    "name": "Shadab",
    "age": 20
}
```

---

### 5. Set

Stores **unique** values.

Example:

```python
numbers = {1, 2, 3, 4}
```

---

## Check Data Type

Use `type()` to check the datatype of any variable.

```python
x = 10
print(type(x))
```

Output:

```python
<class 'int'>
```

---

## Quick Revision

- **Numeric** → `int`, `float`, `complex`
- **Sequence** → `str`, `list`, `tuple`
- **Boolean** → `True`, `False`
- **Dictionary** → `key : value`
- **Set** → Unique values
- **type()** → Checks datatype