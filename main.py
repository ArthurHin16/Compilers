from token import go_pattern as go
import re

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f'Token({self.token_type}, {self.value})'

def get_tokens(text, patterns, TokenType, keywords):
    tokens = []
    i = 0
    while i < len(text):
        for token_type, pattern in patterns.items():
            match = re.match(pattern, text[i:])
            if match:
                if match.group() in keywords:
                    token_type = TokenType.Keyword
                token = Token(token_type, '%r' % match.group())
                print(token)
                tokens.append(token)
                i += match.end()
                break
        else:
            raise Exception(f'Invalid character: {text[i]}')
    return tokens

def main():
    text =  ""
    with open(r'test_code\go\1.go') as file:
        text = file.read()
    tokens = get_tokens(text, go.patterns, go.TokenType, go.keywords)
    
if __name__ == '__main__':
    main()