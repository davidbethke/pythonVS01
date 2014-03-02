class MyFirstClass(object):
    """description of class"""
    
    def __init__(self, *args, **kwargs):
        self.myList=[]
        self.myDict={}
        self.myList=args
        self.myDict=kwargs
       
    def __repr__(self):
        print self.myList
        print self.myDict
    def __str__(self):
        print 'List length:',len(self.myList)
        for item in self.myList:
            print 'Item',item
        print type(self.myDict)   
        for k,v in self.myDict.iteritems():
            print k,v
        return 'Done'
    


