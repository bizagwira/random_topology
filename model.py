'''
Created on 26 juin 2015

@author: info
'''
from PyQt4 import QtCore

class MytableModel(QtCore.QAbstractTableModel): 
    def __init__(self, in_data, headerdata, parent=None, *args): 
        """ in_data: a list of lists
            headerdata: a list of strings
        """
        QtCore.QAbstractTableModel.__init__(self, parent, *args) 
        self.arraydata = in_data
        self.headerdata = headerdata
 
    def flags(self, index):
        if index.column() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable  | QtCore.Qt.ItemIsEditable
        
        elif index.column() == 1:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

        return QtCore.QAbstractTableModel.flags(index)
    
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
        return len(self.headerdata) 
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QtCore.QVariant() 
        elif role != QtCore.Qt.DisplayRole: 
            return QtCore.QVariant() 
        return QtCore.QVariant(self.arraydata[index.row()][index.column()]) 

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[col])
        return QtCore.QVariant()
    
    
    def setData(self, index, value, role):
        if not index.isValid() or index.row() < 0 or index.row() > len(self.arraydata):
            return False
        row_index = index.row()
        col_index = index.column()
        if role:
            self.arraydata[row_index][col_index] = value
            self.dataChanged.emit(index, index)
    
    def insertRows(self, row, count, parent):
        record = [None] * self.headerdata.__len__()
        self.beginInsertRows(QtCore.QModelIndex(), row, row + count - 1)
        self.arraydata.append(record)
        self.endInsertRows()
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
        return True
     
     
            
    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        #self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        if order == QtCore.Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))