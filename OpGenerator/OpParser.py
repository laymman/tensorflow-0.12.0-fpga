# Generated from OpParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\17m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4")
        buf.write(u"\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\3\3\3\7\3-\n\3\f\3\16\3\60\13")
        buf.write(u"\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\7\6?\n\6\f\6\16\6B\13\6\3\7\7\7E\n\7\f\7\16\7H\13")
        buf.write(u"\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\tU\n")
        buf.write(u"\t\f\t\16\tX\13\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3")
        buf.write(u"\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write(u"\3\22\2\2\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write(u"\"\2\2\2_\2$\3\2\2\2\4.\3\2\2\2\6\61\3\2\2\2\b\65\3\2")
        buf.write(u"\2\2\n9\3\2\2\2\fF\3\2\2\2\16I\3\2\2\2\20Q\3\2\2\2\22")
        buf.write(u"Y\3\2\2\2\24\\\3\2\2\2\26^\3\2\2\2\30`\3\2\2\2\32b\3")
        buf.write(u"\2\2\2\34d\3\2\2\2\36f\3\2\2\2 h\3\2\2\2\"j\3\2\2\2$")
        buf.write(u"%\5\4\3\2%&\5\6\4\2&\'\5\b\5\2\'(\5\n\6\2()\5\f\7\2)")
        buf.write(u"\3\3\2\2\2*+\7\b\2\2+-\5\30\r\2,*\3\2\2\2-\60\3\2\2\2")
        buf.write(u".,\3\2\2\2./\3\2\2\2/\5\3\2\2\2\60.\3\2\2\2\61\62\7\t")
        buf.write(u"\2\2\62\63\7\4\2\2\63\64\5\20\t\2\64\7\3\2\2\2\65\66")
        buf.write(u"\7\n\2\2\66\67\7\4\2\2\678\5\20\t\28\t\3\2\2\29:\5\32")
        buf.write(u"\16\2:;\7\4\2\2;@\5\34\17\2<=\7\3\2\2=?\5\34\17\2><\3")
        buf.write(u"\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\13\3\2\2\2B@\3")
        buf.write(u"\2\2\2CE\5\16\b\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2")
        buf.write(u"\2\2G\r\3\2\2\2HF\3\2\2\2IJ\5\36\20\2JK\7\4\2\2KL\5\24")
        buf.write(u"\13\2LM\5 \21\2MN\7\6\2\2NO\5\20\t\2OP\7\7\2\2P\17\3")
        buf.write(u"\2\2\2QV\5\22\n\2RS\7\5\2\2SU\5\22\n\2TR\3\2\2\2UX\3")
        buf.write(u"\2\2\2VT\3\2\2\2VW\3\2\2\2W\21\3\2\2\2XV\3\2\2\2YZ\5")
        buf.write(u"\26\f\2Z[\5\"\22\2[\23\3\2\2\2\\]\7\13\2\2]\25\3\2\2")
        buf.write(u"\2^_\7\13\2\2_\27\3\2\2\2`a\7\16\2\2a\31\3\2\2\2bc\7")
        buf.write(u"\f\2\2c\33\3\2\2\2de\7\f\2\2e\35\3\2\2\2fg\7\f\2\2g\37")
        buf.write(u"\3\2\2\2hi\7\f\2\2i!\3\2\2\2jk\7\f\2\2k#\3\2\2\2\6.@")
        buf.write(u"FV")
        return buf.getvalue()


class OpParser ( Parser ):

    grammarFileName = "OpParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'+'", u"':'", u"','", u"'('", u"')'", 
                     u"'#include'", u"'INPUT'", u"'OUTPUT'" ]

    symbolicNames = [ u"<INVALID>", u"ADD", u"COLON", u"COMMA", u"LPAREN", 
                      u"RPAREN", u"INCLUDES", u"INPUT", u"OUTPUT", u"TYPE", 
                      u"ID", u"WS", u"STRING", u"LQUOTE" ]

    RULE_myop = 0
    RULE_includes = 1
    RULE_inputlist = 2
    RULE_outputlist = 3
    RULE_declare = 4
    RULE_define = 5
    RULE_function = 6
    RULE_parameter = 7
    RULE_argument = 8
    RULE_ret = 9
    RULE_argtype = 10
    RULE_header = 11
    RULE_kernelop = 12
    RULE_method1 = 13
    RULE_method2 = 14
    RULE_funcname = 15
    RULE_argname = 16

    ruleNames =  [ u"myop", u"includes", u"inputlist", u"outputlist", u"declare", 
                   u"define", u"function", u"parameter", u"argument", u"ret", 
                   u"argtype", u"header", u"kernelop", u"method1", u"method2", 
                   u"funcname", u"argname" ]

    EOF = Token.EOF
    ADD=1
    COLON=2
    COMMA=3
    LPAREN=4
    RPAREN=5
    INCLUDES=6
    INPUT=7
    OUTPUT=8
    TYPE=9
    ID=10
    WS=11
    STRING=12
    LQUOTE=13

    def __init__(self, input, output=sys.stdout):
        super(OpParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MyopContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.MyopContext, self).__init__(parent, invokingState)
            self.parser = parser

        def includes(self):
            return self.getTypedRuleContext(OpParser.IncludesContext,0)


        def inputlist(self):
            return self.getTypedRuleContext(OpParser.InputlistContext,0)


        def outputlist(self):
            return self.getTypedRuleContext(OpParser.OutputlistContext,0)


        def declare(self):
            return self.getTypedRuleContext(OpParser.DeclareContext,0)


        def define(self):
            return self.getTypedRuleContext(OpParser.DefineContext,0)


        def getRuleIndex(self):
            return OpParser.RULE_myop

        def enterRule(self, listener):
            if hasattr(listener, "enterMyop"):
                listener.enterMyop(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMyop"):
                listener.exitMyop(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMyop"):
                return visitor.visitMyop(self)
            else:
                return visitor.visitChildren(self)




    def myop(self):

        localctx = OpParser.MyopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_myop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.includes()
            self.state = 35
            self.inputlist()
            self.state = 36
            self.outputlist()
            self.state = 37
            self.declare()
            self.state = 38
            self.define()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.IncludesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INCLUDES(self, i=None):
            if i is None:
                return self.getTokens(OpParser.INCLUDES)
            else:
                return self.getToken(OpParser.INCLUDES, i)

        def header(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OpParser.HeaderContext)
            else:
                return self.getTypedRuleContext(OpParser.HeaderContext,i)


        def getRuleIndex(self):
            return OpParser.RULE_includes

        def enterRule(self, listener):
            if hasattr(listener, "enterIncludes"):
                listener.enterIncludes(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIncludes"):
                listener.exitIncludes(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitIncludes"):
                return visitor.visitIncludes(self)
            else:
                return visitor.visitChildren(self)




    def includes(self):

        localctx = OpParser.IncludesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_includes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OpParser.INCLUDES:
                self.state = 40
                self.match(OpParser.INCLUDES)
                self.state = 41
                self.header()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InputlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.InputlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(OpParser.INPUT, 0)

        def COLON(self):
            return self.getToken(OpParser.COLON, 0)

        def parameter(self):
            return self.getTypedRuleContext(OpParser.ParameterContext,0)


        def getRuleIndex(self):
            return OpParser.RULE_inputlist

        def enterRule(self, listener):
            if hasattr(listener, "enterInputlist"):
                listener.enterInputlist(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInputlist"):
                listener.exitInputlist(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitInputlist"):
                return visitor.visitInputlist(self)
            else:
                return visitor.visitChildren(self)




    def inputlist(self):

        localctx = OpParser.InputlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inputlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(OpParser.INPUT)
            self.state = 48
            self.match(OpParser.COLON)
            self.state = 49
            self.parameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OutputlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.OutputlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(OpParser.OUTPUT, 0)

        def COLON(self):
            return self.getToken(OpParser.COLON, 0)

        def parameter(self):
            return self.getTypedRuleContext(OpParser.ParameterContext,0)


        def getRuleIndex(self):
            return OpParser.RULE_outputlist

        def enterRule(self, listener):
            if hasattr(listener, "enterOutputlist"):
                listener.enterOutputlist(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOutputlist"):
                listener.exitOutputlist(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitOutputlist"):
                return visitor.visitOutputlist(self)
            else:
                return visitor.visitChildren(self)




    def outputlist(self):

        localctx = OpParser.OutputlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_outputlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(OpParser.OUTPUT)
            self.state = 52
            self.match(OpParser.COLON)
            self.state = 53
            self.parameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclareContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.DeclareContext, self).__init__(parent, invokingState)
            self.parser = parser

        def kernelop(self):
            return self.getTypedRuleContext(OpParser.KernelopContext,0)


        def COLON(self):
            return self.getToken(OpParser.COLON, 0)

        def method1(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OpParser.Method1Context)
            else:
                return self.getTypedRuleContext(OpParser.Method1Context,i)


        def ADD(self, i=None):
            if i is None:
                return self.getTokens(OpParser.ADD)
            else:
                return self.getToken(OpParser.ADD, i)

        def getRuleIndex(self):
            return OpParser.RULE_declare

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclare"):
                listener.enterDeclare(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclare"):
                listener.exitDeclare(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitDeclare"):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = OpParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.kernelop()
            self.state = 56
            self.match(OpParser.COLON)
            self.state = 57
            self.method1()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OpParser.ADD:
                self.state = 58
                self.match(OpParser.ADD)
                self.state = 59
                self.method1()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefineContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.DefineContext, self).__init__(parent, invokingState)
            self.parser = parser

        def function(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OpParser.FunctionContext)
            else:
                return self.getTypedRuleContext(OpParser.FunctionContext,i)


        def getRuleIndex(self):
            return OpParser.RULE_define

        def enterRule(self, listener):
            if hasattr(listener, "enterDefine"):
                listener.enterDefine(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDefine"):
                listener.exitDefine(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitDefine"):
                return visitor.visitDefine(self)
            else:
                return visitor.visitChildren(self)




    def define(self):

        localctx = OpParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_define)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OpParser.ID:
                self.state = 65
                self.function()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.FunctionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def method2(self):
            return self.getTypedRuleContext(OpParser.Method2Context,0)


        def COLON(self):
            return self.getToken(OpParser.COLON, 0)

        def ret(self):
            return self.getTypedRuleContext(OpParser.RetContext,0)


        def funcname(self):
            return self.getTypedRuleContext(OpParser.FuncnameContext,0)


        def LPAREN(self):
            return self.getToken(OpParser.LPAREN, 0)

        def parameter(self):
            return self.getTypedRuleContext(OpParser.ParameterContext,0)


        def RPAREN(self):
            return self.getToken(OpParser.RPAREN, 0)

        def getRuleIndex(self):
            return OpParser.RULE_function

        def enterRule(self, listener):
            if hasattr(listener, "enterFunction"):
                listener.enterFunction(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFunction"):
                listener.exitFunction(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFunction"):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = OpParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.method2()
            self.state = 72
            self.match(OpParser.COLON)
            self.state = 73
            self.ret()
            self.state = 74
            self.funcname()
            self.state = 75
            self.match(OpParser.LPAREN)
            self.state = 76
            self.parameter()
            self.state = 77
            self.match(OpParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.ParameterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OpParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(OpParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OpParser.COMMA)
            else:
                return self.getToken(OpParser.COMMA, i)

        def getRuleIndex(self):
            return OpParser.RULE_parameter

        def enterRule(self, listener):
            if hasattr(listener, "enterParameter"):
                listener.enterParameter(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParameter"):
                listener.exitParameter(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParameter"):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = OpParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.argument()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OpParser.COMMA:
                self.state = 80
                self.match(OpParser.COMMA)
                self.state = 81
                self.argument()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argtype(self):
            return self.getTypedRuleContext(OpParser.ArgtypeContext,0)


        def argname(self):
            return self.getTypedRuleContext(OpParser.ArgnameContext,0)


        def getRuleIndex(self):
            return OpParser.RULE_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument"):
                listener.enterArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument"):
                listener.exitArgument(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitArgument"):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = OpParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.argtype()
            self.state = 88
            self.argname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.RetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(OpParser.TYPE, 0)

        def getRuleIndex(self):
            return OpParser.RULE_ret

        def enterRule(self, listener):
            if hasattr(listener, "enterRet"):
                listener.enterRet(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRet"):
                listener.exitRet(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitRet"):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = OpParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(OpParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgtypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.ArgtypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(OpParser.TYPE, 0)

        def getRuleIndex(self):
            return OpParser.RULE_argtype

        def enterRule(self, listener):
            if hasattr(listener, "enterArgtype"):
                listener.enterArgtype(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgtype"):
                listener.exitArgtype(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitArgtype"):
                return visitor.visitArgtype(self)
            else:
                return visitor.visitChildren(self)




    def argtype(self):

        localctx = OpParser.ArgtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(OpParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeaderContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.HeaderContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(OpParser.STRING, 0)

        def getRuleIndex(self):
            return OpParser.RULE_header

        def enterRule(self, listener):
            if hasattr(listener, "enterHeader"):
                listener.enterHeader(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHeader"):
                listener.exitHeader(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitHeader"):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = OpParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(OpParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KernelopContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.KernelopContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OpParser.ID, 0)

        def getRuleIndex(self):
            return OpParser.RULE_kernelop

        def enterRule(self, listener):
            if hasattr(listener, "enterKernelop"):
                listener.enterKernelop(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKernelop"):
                listener.exitKernelop(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitKernelop"):
                return visitor.visitKernelop(self)
            else:
                return visitor.visitChildren(self)




    def kernelop(self):

        localctx = OpParser.KernelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_kernelop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(OpParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.Method1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OpParser.ID, 0)

        def getRuleIndex(self):
            return OpParser.RULE_method1

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod1"):
                listener.enterMethod1(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod1"):
                listener.exitMethod1(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMethod1"):
                return visitor.visitMethod1(self)
            else:
                return visitor.visitChildren(self)




    def method1(self):

        localctx = OpParser.Method1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(OpParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.Method2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OpParser.ID, 0)

        def getRuleIndex(self):
            return OpParser.RULE_method2

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod2"):
                listener.enterMethod2(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod2"):
                listener.exitMethod2(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMethod2"):
                return visitor.visitMethod2(self)
            else:
                return visitor.visitChildren(self)




    def method2(self):

        localctx = OpParser.Method2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(OpParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncnameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.FuncnameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OpParser.ID, 0)

        def getRuleIndex(self):
            return OpParser.RULE_funcname

        def enterRule(self, listener):
            if hasattr(listener, "enterFuncname"):
                listener.enterFuncname(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFuncname"):
                listener.exitFuncname(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFuncname"):
                return visitor.visitFuncname(self)
            else:
                return visitor.visitChildren(self)




    def funcname(self):

        localctx = OpParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(OpParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgnameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OpParser.ArgnameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OpParser.ID, 0)

        def getRuleIndex(self):
            return OpParser.RULE_argname

        def enterRule(self, listener):
            if hasattr(listener, "enterArgname"):
                listener.enterArgname(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgname"):
                listener.exitArgname(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitArgname"):
                return visitor.visitArgname(self)
            else:
                return visitor.visitChildren(self)




    def argname(self):

        localctx = OpParser.ArgnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(OpParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





