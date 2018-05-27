# Generated from OpParser.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by OpParser.

class OpParserVisitor(ParseTreeVisitor):
    def __init__(self):
        self.includes = []
        self.opname = ""
        self.inputs_type = []
        self.inputs_name = []
        self.outputs_type = []
        self.outputs_name = []
        self.params_type = []
        self.params_name = []
        self.func_name = []
        self.ret = []
        self.state = 0

    # Visit a parse tree produced by OpParser#myop.
    def visitMyop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#includes.
    def visitIncludes(self, ctx):
        self.state = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#inputlist.
    def visitInputlist(self, ctx):
        self.state = 2
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#outputlist.
    def visitOutputlist(self, ctx):
        self.state = 3
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#declare.
    def visitDeclare(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#define.
    def visitDefine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#function.
    def visitFunction(self, ctx):
        self.state = 4
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#argument.
    def visitArgument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#ret.
    def visitRet(self, ctx):
        self.ret.append(ctx.TYPE().getSymbol().text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#argtype.
    def visitArgtype(self, ctx):
        if self.state == 2:
            self.inputs_type.append(ctx.TYPE().getSymbol().text)
        if self.state == 3:
            self.outputs_type.append(ctx.TYPE().getSymbol().text)
        if self.state == 4:
            self.params_type[-1].append(ctx.TYPE().getSymbol().text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#header.
    def visitHeader(self, ctx):
        self.includes.append(ctx.STRING().getSymbol().text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#kernelop.
    def visitKernelop(self, ctx):
        self.opname = ctx.ID().getSymbol().text
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#method1.
    def visitMethod1(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#method2.
    def visitMethod2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#funcname.
    def visitFuncname(self, ctx):
        self.func_name.append(ctx.ID().getSymbol().text)
        self.params_type.append([])
        self.params_name.append([])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpParser#argname.
    def visitArgname(self, ctx):
        if self.state == 2:
            self.inputs_name.append(ctx.ID().getSymbol().text)
        if self.state == 3:
            self.outputs_name.append(ctx.ID().getSymbol().text)
        if self.state == 4:
            self.params_name[-1].append(ctx.ID().getSymbol().text)
        return self.visitChildren(ctx)


