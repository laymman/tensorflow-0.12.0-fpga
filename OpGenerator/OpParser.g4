parser grammar OpParser;

options
	{ tokenVocab = OpLexer; }

myop
	: includes inputlist outputlist declare define ;

includes
	: ( INCLUDES header )* ;

inputlist
	: INPUT COLON parameter ;

outputlist
	: OUTPUT COLON parameter ;

declare
	: kernelop COLON method1 ( ADD method1 )* ;

define
	: function* ;

function
	: method2 COLON ret funcname LPAREN parameter RPAREN ;

parameter
	: argument ( COMMA argument )* ;

argument
	: argtype argname ;

ret
	: TYPE ;

argtype
	: TYPE ;

header
	: STRING ;

kernelop
	: ID ;

method1
	: ID ;

method2
	: ID ;

funcname
	: ID ;

argname
	: ID ;