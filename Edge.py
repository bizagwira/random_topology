'''
Created on 8 juin 2015

@author: info
'''
from PyQt4.QtGui import QGraphicsItem, QPainter
from PyQt4.QtCore import QRectF

class EdgeItem (QGraphicsItem):
    def __init__(self, pos, source, target,  **args):
        QGraphicsItem.__init__(self, **args)
        self.source = source
        self.target = target
        self.pos = pos

    def boundingRect (self):
        x0, y0 = self.pos[self.source]
        x1, y1 = self.pos[self.target]
        return QRectF(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))

    def paint (self, painter, style, widget=None):
        assert(isinstance(painter, QPainter))
        x0, y0 = self.pos[self.source]
        x1, y1 = self.pos[self.target]
        painter.drawLine(x0, y0, x1, y1)