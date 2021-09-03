#！Python


import numpy as np
from numpy.core.numeric import count_nonzero
import pyperclip


class Subplots(object):
    '''
    多子图的绘制
    '''
    def __init__(self,arr):
        # self.n = n
        self.arr = np.array(arr)
        self.String(self.GenerateDic())
        self.ToClip()


    def GenerateDic(self):
        #value： [(行min，行max),(列min，列max)]
        d = {}

        arr_unique = np.unique(self.arr)
        for item in arr_unique:
            count = np.count_nonzero(self.arr == item, axis=1)
            count = count[count!=0]
            if  np.unique(count).size != 1:
                raise ValueError
            else:
                idx_arr = np.argwhere(self.arr == item)
                d[item] = [(np.min(idx_arr[:,0]),np.max(idx_arr[:,0])),
                    (np.min(idx_arr[:,1]),np.max(idx_arr[:,1]))]
        
        return d

    def String(self,d):
        s = '''import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

fig = plt.figure(tight_layout=True,
        #wsapce = , hspace = ,
        )
#fig.suptitle('title')

gs = gridspec.GridSpec(%d, %d,figure=fig)
'''% self.arr.shape


        for item,value in d.items():
            s +=  "ax%d = fig.add_subplot(gs[%d:%d, %d:%d])\n" % (item,
            value[0][0],value[0][1]+1,
            value[1][0],value[1][1]+1)

        self.s = s 
        
    

    def ToClip(self):
        
        pyperclip.copy(self.s)

def runSubplots(arr):
    sub = Subplots(arr)


#test
# if __name__ == "__main__":
#     a = np.array([[1,1,2],[1,1,2]])
#     runSubplots(a)
