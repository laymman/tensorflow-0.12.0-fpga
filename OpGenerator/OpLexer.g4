lexer grammar OpLexer;

ADD
	: '+' ;

COLON
	: ':' ;

COMMA
	: ',' ;

LPAREN
	: '(' ;

RPAREN
	: ')' ;

INCLUDES
	: '#include' ;

INPUT
	: 'INPUT' ;

OUTPUT
	: 'OUTPUT' ;

TYPE
	: ( 'void'  | 'char'  | 'int'  | 'float'  | 'double' | 
		'void*' | 'char*' | 'int*' | 'float*' | 'double*' ) ;

ID
	: [a-zA-Z] [a-zA-Z0-9_]* ;

WS
	: [ \t\n\r]+ -> skip ;

LQUOTE 
	: '"' -> more, mode(STR) ;

mode STR;

STRING 
	: '"' -> mode(DEFAULT_MODE) ; // token we want parser to see

TEXT 
	: . -> more ; // collect more text for string
