# Assignment Operators

Assignment operators are used to **assign** or **update** the value of a variable.

---

## Assignment (`=`)

Assigns a value to a variable.

```python
x = "me"
```

Here,

- `=` → Assignment Operator
- `"me"` is assigned to the variable `x`.

---

## Add and Assign (`+=`)

```python
x = 5

x = x + 5

print(x)
```

Output

```python
10
```

The above can be written in a shorter way:

```python
x = 5

x += 5

print(x)
```

Output

```python
10
```

> `x += 5` means **x = x + 5**.

---

## Subtract and Assign (`-=`)

```python
x = 10

x -= 3

print(x)
```

Output

```python
7
```

Equivalent to:

```python
x = x - 3
```

---

## Multiply and Assign (`*=`)

```python
x = 5

x *= 2

print(x)
```

Output

```python
10
```

Equivalent to:

```python
x = x * 2
```

---

## Divide and Assign (`/=`)

```python
x = 10

x /= 2

print(x)
```

Output

```python
5.0
```

Equivalent to:

```python
x = x / 2
```

> **Note:** `/=` always returns a **float**, just like `/`.

---

## Floor Divide and Assign (`//=`)

```python
x = 10

x //= 3

print(x)
```

Output

```python
3
```

Equivalent to:

```python
x = x // 3
```

---

## Modulus and Assign (`%=`)

```python
x = 10

x %= 3

print(x)
```

Output

```python
1
```

Equivalent to:

```python
x = x % 3
```

---

## Power and Assign (`**=`)

```python
x = 2

x **= 3

print(x)
```

Output

```python
8
```

Equivalent to:

```python
x = x ** 3
```

---

# Operators You Actually Need

⭐⭐⭐⭐⭐ Must Know

- `=`
- `+=`
- `-=`
- `*=`
- `/=`

⭐⭐⭐ Good to Know

- `//=`
- `%=`
- `**=`

---

# Interview Notes ⭐

- `=` assigns a value to a variable.
- Compound assignment operators update the value of a variable.
- `x += y` is the same as `x = x + y`.
- These operators make code shorter and easier to read.

---

# 30-Second Revision

- `=` → Assign value
- `+=` → Add and assign
- `-=` → Subtract and assign
- `*=` → Multiply and assign
- `/=` → Divide and assign
- `//=` → Floor divide and assign
- `%=` → Modulus and assign
- `**=` → Power and assign