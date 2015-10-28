'''
Created on 7 oct. 2015

@author: honorelimos
'''
import random
import math
import numpy as np

class Coordonate(object):
    '''
    classdocs
    '''


    def __init__(self, W=600, L=300):
        '''
        Constructor
        '''        
        self.m_width = W
        self.m_length = L
        self.m_loc = (self.m_width, self.m_length)
        self.m_minrfRange = 5
        self.m_maxrfRange = 120
        
    def Distance (self, pA, pB):
        x0, y0 = pA
        x1, y1 = pB
        return math.sqrt((x0 - x1)**2 + (y0 - y1)**2) 
    
    def HasNextHop(self, ListNodes, node):
        conStatus = True
        for xnode in ListNodes:
            d = self.Distance (node, xnode)
            if d < self.m_minrfRange:
                conStatus = True
                return conStatus
            elif self.m_minrfRange < d < self.m_maxrfRange:
                conStatus = False
        return conStatus
    
    def RandLocGenerator (self, Width, Length, number):
        LocNodeList = []
        px = Width * 0.5
        py = Length * 1
        node = np.array([px, py])
        LocNodeList.append(node)
        
        for _ in range(number):
            px = random.randint(0, Width)
            py = random.randint(0, Length)
            node = np.array([px, py])
            while self.HasNextHop(LocNodeList, node):
                px = random.randint(0, Width)
                py = random.randint(0, Length)
                node = np.array([px, py])
            LocNodeList.append(node)     
        return LocNodeList
    
    def EdgeCreate (self, NodeList):
        number = len(NodeList)
        NodeListCopy = NodeList
        randNodeLocList = self.RandLocGenerator (self.m_width, self.m_length, number)
        nodeDict = dict(zip(NodeList, randNodeLocList))
        edgeList = []
        
        for srcNode in list (NodeListCopy):
            if len(NodeListCopy) > 1: NodeListCopy.remove(srcNode)
            for dstNode in NodeListCopy:
                d = self.Distance (nodeDict[srcNode], nodeDict[dstNode])
                if d < self.m_maxrfRange:
                    Link = (srcNode, dstNode)
                    edgeList.append(Link)
        """
        print (nodeDict)
        print (edgeList)
        """
        return edgeList, nodeDict
    
    def SetWidth (self, width):
        self.m_width = width
        
    def SetLength (self, length):
        self.m_length = length
        