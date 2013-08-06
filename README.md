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
labels = [Label(text=s) for s in strings]
list = DNDList(root, width, height, items=labels)
root.mainloop()
```

## Adding items to a DNDList

```python
root = Tk()
width = 700
height = 800
list = DNDList(root, width, height)
list.addItem(Label(text="Primero"))
list.addItem(Label(text="Segundo"))
list.addItem(Label(text="Tercero"))
root.mainloop()
```

## Getting the items in the DNDList ordered by y-coordinate

```python
list.getOrdered()
```