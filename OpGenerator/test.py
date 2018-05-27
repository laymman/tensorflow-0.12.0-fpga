import sys

from antlr4 import *
from OpLexer import OpLexer
from OpParser import OpParser
from OpParserListener import OpParserListener
from OpParserVisitor import OpParserVisitor


incldues = []
func_name = []
inputs_name = []
inputs_type = []
outputs_name = []
outputs_type = []
params_name = []
params_type = []
inter_param = []
ret = []
outputs_shape = []

def VisitTree():
    global incldues
    global func_name
    global inputs_name
    global inputs_type
    global outputs_name
    global outputs_type
    global params_name
    global params_type
    global ret
    text = FileStream("./test.txt")
    lexer = OpLexer(text)
    stream = CommonTokenStream(lexer)
    parser = OpParser(stream)
    tree = parser.myop()
    v = OpParserVisitor()
    v.visit(tree)
    includes = v.includes
    func_name = v.func_name
    inputs_name = v.inputs_name
    inputs_type = v.inputs_type
    outputs_name = v.outputs_name
    outputs_type = v.outputs_type
    params_name = v.params_name
    params_type = v.params_type
    ret = v.ret


#def getIncludes() :

#def getOpName() :

#def getInputs() :

#def getOutputs() :


def getOutputsShape() :
    # called after getInterParams
    # inter_param be ready
    global inter_param
    global outputs_name
    global outputs_shape
    for name in inter_param :
        splits = name.split('_', 3)
        if len(splits) == 3 and splits[0] in outputs_name and splits[1] == "dim" :
            if name not in outputs_shape :
                outputs_shape.append(name)

#def getRet() :

#def getFuncName() :

#def getParamsName() :

def getInterParams() :
    global params_name
    global inputs_name
    global outputs_name
    global inter_param
    global outputs_shape
    for i in range(len(params_name)) :
        for j in range(len(params_name[i])) :
            name = params_name[i][j]
            if name not in inputs_name and name not in outputs_name :
                splits = name.split('_', 3)
                if len(splits) == 3 and splits[1] == "dim" and splits[0] in inputs_name :
                    params_name[i][j] = splits[0] + ".shape()" + ".dim_size(%s)" % splits[2]
                elif name not in inter_param :
                    inter_param.append(name)
                else :
                    pass

VisitTree()
getInterParams()
getOutputsShape()
print ret
print outputs_shape
print inter_param