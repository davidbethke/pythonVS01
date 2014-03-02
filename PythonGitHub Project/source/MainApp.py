import MyFirstClass
class MainApp(object):
    """description of class"""
    def __init__(self, *args, **kwargs):
        self.myList=['1','2','3']
        self.myDict={}
        self.myDict['name']='Dave'
        self.myDict['age']='44'
        self.myClass=MyFirstClass.MyFirstClass('1','2','3',**self.myDict)
def main():
    app=MainApp()
    print app.myClass
if __name__ == '__main__':
    main()


