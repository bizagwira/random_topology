'''
Created on 30 sept. 2015

@author: info
'''
import re
"""
import os
import time
from time import strftime
"""
import numpy as np

class Data(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
    def ReadFile(self, filename):
        data = []
        with open (filename, 'r') as f:
            for line in f:
                splitedLine = re.sub('[^A-Za-z0-9:.]+', ' ', line).strip().split(" ")
                data.append (splitedLine)
        return data
    
    def RmDeplicateItem (self, inputDict):
        result = {}    
        for key,value in inputDict.items():
            if value not in result.values():
                result[key] = value
        return result
    
    def WriteWSn (self, linkList, nodeLocDict, filename):
        content =""
        """
        directory_resulats = "LINK_"+strftime("%Y_%m_%d_%H", time.localtime())
        if not os.path.exists(directory_resulats):
            os.makedirs(directory_resulats)
        f = open(os.path.join(directory_resulats, filename), 'w')
        """
        f = open (filename, 'w')
        for link in linkList:
            nodex, nodey = link
            content += nodex+"\t"+nodey+"\t"+"\t".join(map(str, nodeLocDict[nodex]))+"\t"+"\t".join(map(str, nodeLocDict[nodey]))+"\n"
        f.write(content)
        f.close()
        
    def ReadWsn (self, filename):
        data = self.ReadFile(filename)
        linkList = [ tuple(link[:2]) for link in data]
        nodexList = [node[0] for node in data]
        nodeyList = [node[1] for node in data]
        nodexLoc = [np.array(map(float, node[2:4])) for node in data]
        nodeyLoc = [np.array(map(float, node[4:])) for node in data]
        locxDict = dict(zip(nodexList, nodexLoc))
        locyDict = dict(zip(nodeyList, nodeyLoc))
        locxDict.update(locyDict)
        
        return linkList, self.RmDeplicateItem (locxDict)