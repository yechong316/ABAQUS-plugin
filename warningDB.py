from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class WarningDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '\xbe\xaf\xb8\xe6\xcc\xe1\xca\xbe\xbf\xf2\xd1\xa7\xcf\xb0',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        AFXTextField(p=self, ncols=12, labelText='\xb8\xb4\xba\xcf\xb2\xc4\xc1\xcf\xc3\xdc\xb6\xc8:', tgt=form.numKw, sel=0)
