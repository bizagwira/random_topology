'''
Created on 8 juin 2015

@author: info
'''

from PyQt4.QtGui import QGraphicsItem, QPainter, QBrush, QPainterPath, QFont, QPen
from PyQt4.QtCore import QPointF, QRectF, QObject, Qt
from PyQt4 import QtCore

#import numpy as np

count = 0
def status(message):
    global count
    count += 1
    print (count, message)

class NodeSignal (QObject):
    nodeItemSignal = QtCore.pyqtSignal (str, list)
        
class NodeItem (QGraphicsItem):
    '''
    classdocs
    '''
    def __init__(self, scene, pos, node, radius=15, **args):
        '''
        Constructor
        '''
        QGraphicsItem.__init__(self, **args)

        self.node = node
        self.radius = radius
        self.pos = pos
        self.scene = scene
        
        self.m_signalLinkNode = NodeSignal ()

        x, y = self.pos[node]
        self.setPos(QPointF(x, y))

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        
    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange :
            point = value.toPointF()
            self.pos[self.node] = [point.x(), point.y()]
            self.scene.update()
            
            self.m_signalLinkNode.nodeItemSignal.emit (self.node, self.pos[self.node])
        return QGraphicsItem.itemChange(self, change, value)

    def update(self, *__args):
        self.setPos(*self.pos[self.node])

    def boundingRect(self):
        return QRectF(-2*self.radius, -2*self.radius, 4*self.radius, 4*self.radius)

    def paint (self, painter, style, widget=None):
        assert isinstance(painter, QPainter)

        if self.isSelected():
            brush = QBrush(Qt.green)
        else:
            brush = QBrush(Qt.white)

        pen = QPen(Qt.black)

        circle_path = QPainterPath()
        circle_path.addEllipse(self.boundingRect())
        painter.fillPath(circle_path, brush)
        painter.strokePath(circle_path, pen)

        text_path = QPainterPath()
        text_path.addText(0, 0, QFont(), str(self.node))
        box = text_path.boundingRect()
        text_path.translate(-box.center())

        painter.fillPath(text_path, QBrush(Qt.black))