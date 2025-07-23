import sys
import logging
def errormd(error,errordetail:sys):
    _,_,exctb=errordetail.exc_info()
    filename=exctb.tb_frame.f_code.co_filename
    errormsg="error ocuured in python script name [{0}] line number [{1}] error message [{2}]".format(
     filename,exctb.tb_lineno,str(error))
    return errormsg
    
class CustomException(Exception):
    def __init__(self,errormsg,errordetail:sys):
        super().__init__(errormsg)
        self.errormsg=errormd(errormsg,errordetail=errordetail)
    def __str__(self):
        return self.errormsg

     
    

