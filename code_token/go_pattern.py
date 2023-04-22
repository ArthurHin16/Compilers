from enum import Enum

class TokenType(Enum):
    Text = 'text'
    Comment = 'comment'
    Keyword = 'keyword'
    Plus = 'plus'
    Minus = 'minus'
    Multiply = 'multiply'
    Divide = 'divide'
    EOF = 'EOF'
    NewLine = 'new_line'
    WhiteSpace = 'whitespace'
    Number = 'number'
    Indentifier = 'identifier'
    Assignment = 'assignment'
    Operator = 'operator'
    Semicolon = 'semicolon'
    OpenParen = 'open_paren'
    CloseParen = 'close_paren'
    OpenCurly = 'open_curly'
    CloseCurly = 'close_curly'
    Equal = 'equal'
    NotEqual = 'not_equal'
    DoubleQuote = 'double_quote'
    Colon = 'colon'
    OpenBracket = 'open_bracket'
    CloseBracket = 'closeBracket'
    Comma = 'comma'
    Period = 'period'
    And = 'and'
    Percentage = 'percentage'
    Quote = 'quote'
    
patterns = {
    TokenType.Text: r'\".*\"',
    TokenType.Comment: r'//.*',
    TokenType.Plus: r'\+',
    TokenType.Minus: r'-',
    TokenType.Multiply: r'\*',
    TokenType.Divide: r'/',
    TokenType.NewLine: r'\n',
    TokenType.WhiteSpace: r'\s',
    TokenType.Number: r'\d+', 
    # probably should change + to *
    TokenType.Indentifier: r'[a-zA-Z_][a-zA-Z0-9_]*',
    TokenType.Assignment: r'=',
    TokenType.Operator: r'[><]',
    TokenType.Semicolon: r';',
    TokenType.OpenParen: r'\(',
    TokenType.CloseParen: r'\)',
    TokenType.OpenCurly: r'\{',
    TokenType.CloseCurly: r'\}',
    TokenType.Equal: r'==',
    TokenType.NotEqual: r'!=',
    TokenType.DoubleQuote: r'"',
    TokenType.Colon: r':',
    TokenType.OpenBracket: r'\[',
    TokenType.CloseBracket: r'\]',
    TokenType.Comma: r',',
    TokenType.Period: r'\.',
    TokenType.And: r'\&',
    TokenType.Percentage: r'\%',
    TokenType.Quote: r'\'',
}

keywords = {
    'if',
    'else',
    'for',
    'while',
    'do',
    'break',
    'continue',
    'package',
    'import',
    'type',
    'struct',
    'string',
    'func',
    'Println'
}