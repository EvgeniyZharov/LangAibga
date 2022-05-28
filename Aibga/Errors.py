def errorMessage(message):
    return f"\033[31m {message}"


class FalseSyntaxe(Exception):

    def __init__(self, data, line, position):
        self.data = str(data)
        self.line = line
        self.position = position

    def __str__(self):
        text = f"Неизвестный символ в {self.line} строке, на " \
               f"{self.position} позиции: {self.data}"
        return errorMessage(text)


class FalseKod(Exception):

    def __init__(self, data, line):
        self.data = str(data)
        self.line = line

    def __str__(self):
        text = f"Неизвестная конструкция в {self.line} строке"
        return errorMessage(text)


class NotSemicolon(Exception):

    def __init__(self, line):
        self.line = line

    def __str__(self):
        text = f"Не хватает символа в {self.line} строке: ;"
        return errorMessage(text)


class NotBracket(Exception):

    def __init__(self, data, line):
        self.data = data
        self.line = line

    def __str__(self):
        text = f"Не корректное количество символов " \
               f"в {self.line} строке: {self.data}"
        return errorMessage(text)


class NotFigureBracket(Exception):

    def __init__(self, data, line):
        self.data = data
        self.line = line

    def __str__(self):
        text = f"Не корректное количество символов " \
               f"в {self.line} строке: {self.data}"
        return errorMessage(text)


class IntInStartLine(Exception):

    def __init__(self, data, line):
        self.data = data
        self.line = line

    def __str__(self):
        text = f"Не корректное значение в начале {self.line} строки: {self.data}"
        return errorMessage(text)
