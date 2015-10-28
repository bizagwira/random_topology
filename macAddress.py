'''
Created on 7 oct. 2015

@author: honorelimos
'''
import string
import random

class MacAddress(object):
    '''
    classdocs
    '''

    def __init__(self, addr_size=2):
        '''
        Constructor
        '''
        self.m_addr = self.SetAddressMac (addr_size)
        
    def RandStr (self, addr_size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(addr_size))
    
    def SetAddressMac (self, addr_size):
        variable = "0123456789ABCDEF"
        macAddress = ""
        for _ in range(addr_size):
            if not macAddress :
                macAddress += self.RandStr (2, variable)
            else :
                macAddress += ":" + self.RandStr (2, variable)
        return macAddress
     
    def GetListAddr(self, number, addr_size=2):
        addrList = list ()
        for _ in range(number):
            addr = self.SetAddressMac (addr_size)
            addrList.append (addr)
        return addrList      