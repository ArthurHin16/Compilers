from enum import Enum
import re

class TokenType(Enum):
    Keyword = 'keyword'
    Plus = 'plus'
    Minus = 'minus'
    Multiply = 'multiply'
    Divide = 'divide'
    EOF = 'EOF'
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

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f'Token({self.token_type}, {self.value})'
    
patterns = {
    TokenType.Plus: r'\+',
    TokenType.Minus: r'-',
    TokenType.Multiply: r'\*',
    TokenType.Divide: r'/',
    TokenType.WhiteSpace: r'\s',
    TokenType.Number: r'\d+', # probably should change + to *
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
}

keywords = {
    'if',
    'else',
    'for',
    'while',
    'do',
    'break',
    'continue',
}


def main():
    text = 'for x = 3 + 4 * 5;'
    tokens = []
    i = 0
    while i < len(text):
        for token_type, pattern in patterns.items():
            match = re.match(pattern, text[i:])
            if match:
                if match.group() in keywords:
                    token_type = TokenType.Keyword
                token = Token(token_type, match.group())
                tokens.append(token)
                i += match.end()
                break
    print(tokens)

if __name__ == '__main__':
    main()