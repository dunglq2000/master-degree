with open("book-1-chap-0.md", "rb") as f:
    data = f.read()

data = data.replace(b"\n", b"")

f.close()

with open("book-1-chap-0.md", "wb") as f:
    f.write(data)