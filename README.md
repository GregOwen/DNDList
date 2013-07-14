DNDList
=======

A drag and drop list module implemented using Tkinter

## Creating a new DNDList

```python
root = Tk()
width = 700
height = 800
list = DNDList(root, width, height)
root.mainloop()
```

## Creating a DNDList from an existing list

```python
root = Tk()
width = 700
height = 800
strings = ["First", "Second", "Third"]
list = DNDList(root, width, height, items=strings)
root.mainloop()
```

## Adding items to a DNDList

```python
root = Tk()
width = 700
height = 800
list = DNDList(root, width, height)
list.addItem("Primero")
list.addItem("Segundo")
list.addItem("Tercero")
root.mainloop()
```

## Getting the items in the DNDList from top to bottom

```python
list.getOrdered()
```