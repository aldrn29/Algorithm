'''
모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
'''
import re

def check(str) :
    p = re.compile('[a|e|i|o|u]')
    m = p.match(str)
    
    if m != None :
        p = re.compile('[a|e|i|o|u]{3}|^[a|e|i|o|u]{3}')
        m = p.match(str)
        
        # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        # if m != None :
            

    return False

str = input()
if check(str) :
    print("<", str, "> is acceptable.", sep='')
else :
    print("<", str, "> is not acceptable.", sep='')
