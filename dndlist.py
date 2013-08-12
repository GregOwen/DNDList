"""
 "  File: dndlist.py
 "  Written By: Gregory Owen
 "
 "  A Tkinter-based drag-and-drop list module. Objects in the list may contain
 "  any type of Tkinter widget (the widget is passed to the constructor, and its
 "  master is changed to be the widget's canvas).
""" 

from Tkinter import *

class DNDNode():

    def __init__(self, dndlist, widget):
        """ Creates a new DNDNode that is a part of the given DNDlist and
            contains the given widget. """

        self.list = dndlist
        self.widget = widget
        self.widget.master = self.list.canvas

        self.window = self.list.canvas.create_window(self.list.center,
                                                     self.list.depth, 
                                                     window=self.widget,
                                                     anchor=N)

    def getY(self):
        """ Returns the y-coordinate of the top of the node's widget in the 
            coordinate system of the DNDList's canvas. """

        bbox = self.list.canvas.bbox(self.window)
        return bbox[1]

    def __lt__(self, other):
        """ Compares DNDNode objects based on their y-coordinate (as defined by
            getY(). Necessary for sorting the elements of a DNDList. """

        return self.getY() < other.getY()


class DNDList():

    def __init__(self, frame, width, height, items=None):
        """ Create a new DNDList object that fits into the given frame and has
            the specified width and height. If a list is passed as items, set
            the dndlist to contain the widgets in items. """

        # The size of the offset, in pixels, between two adjacent items
        self.OFFSET = 10

        self.width = width
        self.center = self.width/2
        self.height = height
        self.frame = Frame(frame, width=self.width, height=self.height)
        self.canvas = self.makeCanvas()
        self.depth = 0
        self.dragData = {"x":0, "y":0, "item":None}
        self.elements = {}

        self.frame.pack()

        self.getOrdered()

        if items is not None:
            for item in items:
                self.addItem(item)

    def makeCanvas(self):
        """ Initialize the canvas, including scrollbar. """

        canvas = Canvas(self.frame, width=self.width, height=self.height,
                        scrollregion=(0, 0, self.width, self.height))
        scroll = Scrollbar(self.frame, command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        canvas.pack(side=LEFT, fill="both", expand=True)
        scroll.pack(side=RIGHT, fill=Y)

        return canvas

    def addItem(self, item):
        """ Add a new entry to the list containing the widget item. """
        
        node = DNDNode(dndlist=self, widget=item)

        self.elements[node.window] = node

        # Bounding box for the node's window (used to get height)
        bbox = self.canvas.bbox(node.window)

        self.depth += self.OFFSET
        self.depth += (bbox[3] - bbox[1])

        self.bindDragDrop(node.widget)
        for widget in node.widget.winfo_children():
            self.bindDragDrop(widget)

    def bindDragDrop(self, widget):
        """ Bind drag and drop capabilities to widget. """

        widget.bind("<Button-1>", self.onClick)
        widget.bind("<ButtonRelease-1>", self.onRelease)
        widget.bind("<B1-Motion>", self.onMotion)

    """ ------------------------------------------------------------------------- """
    """                         Pointer Coordinate method                         """
    """   Courtesy of Bryan Oakley, http://stackoverflow.com/questions/16640747   """
    """ ------------------------------------------------------------------------- """

    def getClickCoords(self):
        """ Translate the position of the mouse to canvas coordinates. Returns
            a tuple (x,y) of the resulting coordinates. """

        wx, wy = self.canvas.winfo_rootx(), self.canvas.winfo_rooty()
        x, y = self.frame.winfo_pointerxy()
        cx = self.canvas.canvasx(x-wx)
        cy = self.canvas.canvasy(y-wy)

        return (cx, cy)

    """ ------------------------------------------------------------------------- """
    """                           Click and Drag methods                          """
    """    Courtesy of Bryan Oakley, http://stackoverflow.com/questions/6740855   """
    """ ------------------------------------------------------------------------- """

    def onClick(self, event):
        """ Begin dragging an item. """
        
        x, y = self.getClickCoords()

        self.dragData["item"] = self.canvas.find_closest(x, y)[0]
        self.elements[self.dragData["item"]].widget.lift()
        self.dragData["x"] = x
        self.dragData["y"] = y
        
    def onRelease(self, event):
        """ Finish dragging an item. """

        self.dragData["item"] = None
        self.dragData["x"] = 0
        self.dragData["y"] = 0

    def onMotion(self, event):
        """ Handle dragging an item. """

        x, y = self.getClickCoords()

        deltaX = x - self.dragData["x"]
        deltaY = y - self.dragData["y"]
        self.canvas.move(self.dragData["item"], deltaX, deltaY)
        self.dragData["x"] = x
        self.dragData["y"] = y

    def getOrdered(self):
        """ Returns the elements of the DNDList sorted by y-coordinate, with the
            top element first. This is an order nlogn operation, since the list
            does not maintain any state about the order of its elements. """

        nodes = [self.elements[id] for id in sorted(self.elements, 
                                                    key=self.elements.get)]
        return nodes

if __name__ == "__main__":
    """ Test the methods. """

    root = Tk()
    #frame = Frame(root)
    #frame.pack()
    list = DNDList(root, 700, 800)

    args = {"wraplength": 500, "relief": RAISED, "borderwidth": 2}
    contents = ["First", "Second", "Third", "Really really really really really really really really really really really really really really really really really really really really really really really really long text."]

    for c in contents:
        label = Label(text=c, **args)
        list.addItem(label)

    print list.getOrdered()

    root.mainloop()
