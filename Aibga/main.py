from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

kod_1 = ["a = ( 5 + 3 * ( 5 - 3 ) - 2 ) * 2 - 8 ; ",
         "PRINT ( a ) ;",
         "b = 20 / a ;",
         "PRINT ( b ) ;",
         "WHILE ( a < 1 ) { a = a + 1 ; PRINT ( a ) ; } ;",
         "IF ( 22 > b ) { PRINT ( b ) ; } ;",
         ]

kod_2 = ["LinkedList link_list = { 1 , 3 , 4 } ;",
         "link_list .insertAtEnd ( 2 ) ;",
         "link_list .insertAtHead ( 1 ) ;",
         "link_list .delete ( 2 ) ;",
         "link_list .deleteAtHead ( ) ;",
         "link_list .search ( 2 ) ;",
         "link_list .isEmpty ( ) ;"]


def get_kod():
    kod = list()
    while True:
        line = input("Введите строку кода: ")
        if line:
            kod.append(line)
        else:
            break
    print(f"Введено строк: {len(kod)}\n")
    return kod


def main():

    # kod = get_kod()  # Input new kod

    lexer = Lexer(kod_1)  # Search lexemes
    # print(kod)  # Show lines of the kod
    lexer.analise()  # Analise lexemes
    lexemes = lexer.get()  # Get list of lexemes
    # lexer.show()  # Show all lexemes

    parser = Parser(lexemes)  # Object for parsing
    parser.parse()  # Start parsing for search nodes
    node_list = parser.getNodeList()  # Get list of nodes

    inter = Interpreter(node_list)  # Object for execute
    inter.execute()  # Start execute

    print(inter.linkedlist_values)  # Show all variables
    # print(inter.variables_values)  # Show all LinkedList variables


if __name__ == '__main__':
    main()
