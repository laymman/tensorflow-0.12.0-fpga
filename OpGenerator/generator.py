import sys
from antlr4 import *
from OpLexer import OpLexer
from OpParser import OpParser
from OpParserListener import OpParserListener
from OpParserVisitor import OpParserVisitor

class generator(object):

    def __init__(self):
        self.incldues = []
        self.opname = ""
        self.func_name = []
        self.inputs_name = []
        self.inputs_type = []
        self.outputs_name = []
        self.outputs_type = []
        self.params_name = []
        self.params_type = []
        self.inter_params = []
        self.outputs_shape = []
        self.ret = []

    def VisitTree(self):
        text = FileStream("./test.txt")
        lexer = OpLexer(text)
        stream = CommonTokenStream(lexer)
        parser = OpParser(stream)
        tree = parser.myop()
        v = OpParserVisitor()
        v.visit(tree)

        self.includes = v.includes
        self.opname = v.opname
        self.func_name = v.func_name
        self.inputs_name = v.inputs_name
        self.inputs_type = v.inputs_type
        self.outputs_name = v.outputs_name
        self.outputs_type = v.outputs_type
        self.params_name = v.params_name
        self.params_type = v.params_type
        self.ret = v.ret

    def getIncludes(self):
        return self.includes

    def getOpName(self):
        return self.opname

    def getInputs(self):
        return zip(self.inputs_type, self.inputs_name)

    def getOutputs(self):
        return zip(self.outputs_type, self.outputs_name)

    def getOutputsShape(self):
        # called after getInterParams
        # inter_params be ready
        for param in self.inter_params:
            name = param[1]
            splits = name.split('_', 3)
            if len(splits) == 3 and splits[0] in self.outputs_name and splits[1] == "dim":
                if name not in self.outputs_shape:
                    self.outputs_shape.append(name)
        return self.outputs_shape

    def getRet(self):
        return self.ret

    def getFuncName(self):
        return self.func_name

    def getParamsName(self):
        return self.params_name

    def getParamsType(self):
        return self.params_type

    def getInterParams(self):
        collect = [] # no repeat inter params
        for i in range(len(self.params_name)):
            for j in range(len(self.params_name[i])): 
                name = self.params_name[i][j]
                if name not in self.inputs_name and name not in self.outputs_name:
                    splits = name.split('_', 3)
                    if len(splits) == 3 and splits[1] == "dim" and splits[0] in self.inputs_name :
                        self.params_name[i][j] = splits[0] + ".shape()" + ".dim_size(%s)" % splits[2]
                    elif name not in collect :
                        collect.append(name)
                        self.inter_params.append((self.params_type[i][j], name))
                    else :
                        pass
        return self.inter_params
