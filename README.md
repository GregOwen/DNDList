DNDList
=======

A drag and drop list module implemented using Tkinter

## Creating a new DNDList

<code>
root = Tk()
width = 700
height = 800
list = DNDList(root, width, height)
root.mainloop()
<\code>

## Creating a DNDList from an existing list

<code>
root = Tk()
width = 700
height = 800
strings = ["First", "Second", "Third"]
list = DNDList(root, width, height, items=strings)
root.mainloop()
<\code>

## Adding items to a DNDList

<code>
root = Tk()
width = 700
height = 800
list = DNDList(root, width, height)
list.addItem("Primero")
list.addItem("Segundo")
list.addItem("Tercero")
root.mainloop()
</code>

## Getting the items in the DNDList from top to bottom

<code>
list.getOrdered()
</code>