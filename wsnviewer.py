'''
Created on 27 oct. 2015

@author: info
'''
import math
from PyQt4.QtGui import QGraphicsScene, QPainter
from PyQt4 import QtGui, QtCore
import networkx as nx
from Node import NodeItem
from Edge import EdgeItem

from data import Data
import parameterWin
from window1 import Ui_WsnViewerUI
from rfSetting import Ui_rfSettingWindow

from macAddress import MacAddress
from coordonnes import Coordonate
 
class WsnViewer(QtGui.QMainWindow, Ui_WsnViewerUI):
    def __init__(self, parent=None):
        super(WsnViewer, self).__init__(parent)
        self.setupUi (self)
        self.m_nodeNumber = 10
        self.m_maxRfRange = 70
        self.m_macAddr = MacAddress ()
        self.m_nodeLoc = Coordonate ()
        self.m_nodeList = self.m_macAddr.GetListAddr(10)
        self.m_edgeList = 0 
        self.m_edgeDict = {}
        self.m_nodeLocDict = {}
        
        self.m_scene = QGraphicsScene (self.graphicsView)
        #self.m_paramWin = Ui_paramWindow ()
        self.m_graph = nx.Graph()
        self.m_data = list ()
        self.DataReader = Data ()
        
        self.graphicsView.setDragMode (self.graphicsView.RubberBandDrag)
        self.graphicsView.setRenderHints (QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.graphicsView.setScene (self.m_scene)
        self.ConnectActions ()
    
    def ConnectActions(self):
        self.actionQuit.triggered.connect (QtGui.qApp.quit)
        self.actionOpen.triggered.connect (self.OpenWsnTopology)
        self.actionRandom_topology.triggered.connect (self.GenerateRandWsn)
        self.actionTools.triggered.connect(self.SetRadioRange)
        self.actionSave.triggered.connect(self.Save)
        
    def OpenWsnTopology (self):
        fileName = QtGui.QFileDialog.getOpenFileName(
                        self,
                        "Ouvrir un fichier des positions des noeuds",
                        QtCore.QDir.homePath(),
                        "Fichiers texte (*.txt)"
                    )
        if (fileName):
            self.m_data = self.DataReader.ReadFile(fileName)
            
    def GenerateRandWsn (self):
        self.m_nodeList = self.m_macAddr.GetListAddr(self.m_nodeNumber)
        #print(self.m_nodeList)
        self.m_edgeList, self.m_nodeLocDict = self.m_nodeLoc.EdgeCreate (self.m_nodeList)
        #print(self.m_nodeLocDict)
        #print(self.m_edgeList)
        self.m_scene.clear()
        self.DrawGraph ()
             
    def main (self):
        self.show()
        
    def OpenDialog(self):
        self.dlg = OpenFileDialog ()
        self.dlg.show()
        
    def DrawGraph (self):
        for edge in self.m_edgeList:
            self.m_edgeDict [edge] = EdgeItem (self.m_nodeLocDict, edge[0], edge[1])
            self.m_scene.addItem(self.m_edgeDict [edge])
        for node in self.m_nodeLocDict.iterkeys():
            nodeItem = NodeItem (self.m_scene, self.m_nodeLocDict, node)
            #nodeItem.m_signalLinkNode.nodeItemSignal.connect (self.UpdateNodeLocDict)
            self.m_scene.addItem (nodeItem)
    
    def Save (self):
        filename = QtGui.QFileDialog.getSaveFileName (
                        self,
                        "Ouvrir un fichier des positions des noeuds",
                        QtCore.QDir.homePath(),
                        "Fichiers texte (*.txt)"
                    )
        if self.m_edgeList and filename:
            self.DataReader.WriteWSn(self.m_edgeList, self.m_nodeLocDict, filename)
    
    def UpdateNodeLocDict (self, nodeName, nodePos):
        self.m_nodeLocDict [nodeName] = nodePos
        for node, pos in self.m_nodeLocDict.items():
            if node != nodeName:
                edge = (nodeName, node)
                if self.Distance(nodePos, pos) <= self.m_maxRfRange:
                    if not edge in self.m_edgeList and not edge[::-1] in self.m_edgeList:
                        self.m_edgeList.append (edge)
                        self.m_edgeDict [edge] = EdgeItem (self.m_nodeLocDict, edge[0], edge[1])
                        self.m_scene.addItem(self.m_edgeDict [edge])
                        #print ("%s %s %s" % (node, pos[0], pos[1]))
                else:
                    self.RemoveLink (edge)
                    self.UpdateNodeList (edge)
                    #print ("%s %s %s" % (node, pos[0], pos[1]))
               
    def UpdateNodeList (self, edge):
        while edge in self.m_edgeList:
            self.m_edgeList.remove (edge)
        
        #while edge[::-1] in self.m_edgeList:
        #    self.m_edgeList.remove (edge[::-1])
            
    def RemoveLink (self, edge):
        if edge in self.m_edgeDict:
            self.m_scene.removeItem (self.m_edgeDict [edge])
            del self.m_edgeDict [edge]
            self.m_scene.update()
            print ("%s %s" % (edge[0], edge[1]))
            
        
    def UpdateScene (self, edge):
        self.m_scene.addItem(EdgeItem (self.m_nodeLocDict, edge[0], edge[1]))
                
    def Distance (self, u, v):
        x0, y0 = u
        x1, y1 = v
        return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
    
    def SetRadioRange (self):
        self.rfWindow = RfSettingWindow ()
        resultat = self.rfWindow.exec_()
        
        if resultat:
            self.rfWindow.SetRadioValues ()
            self.m_nodeNumber = self.rfWindow.GetNodeNumber ()
            self.m_maxRfRange = self.rfWindow.GetRfRange ()
            self.GenerateRandWsn ()
                    
class OpenFileDialog (QtGui.QDialog, parameterWin.Ui_paramWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButtonAnnuler.clicked.connect(self.close)
        self.pushButtonValider.clicked.connect (self.SetNodeNumber)
        
    def SetNodeNumber (self):
        self.m_nodeNumber = self.spinBoxNodeNumber.value()
        
    def GetNodeNumber (self):
        return self.m_nodeNumber

class RfSettingWindow (QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_rfSettingWindow ()
        self.ui.setupUi(self)
        self.m_nodeNumber = 0
        self.m_maxRfRange = 0
        self.ui.pushButtonAnnuler.clicked.connect(self.close)
        self.ui.pushButtonValider.clicked.connect(self.SetRadioValues)
        
    def SetRadioValues (self):
        self.m_maxRfRange = self.ui.rangeDoubleSpinBox.value()
        self.m_nodeNumber = self.ui.spinBoxNodeNumber.value()
        
        self.accept()
        
    def GetRfRange (self):
        return self.m_maxRfRange
    
    def GetNodeNumber (self):
        return self.m_nodeNumber       