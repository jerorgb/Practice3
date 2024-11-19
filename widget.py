import sys, re, io
from nltk import CFG, ChartParser, Nonterminal, Tree
from PySide6.QtWidgets import QApplication, QWidget

# Import the generated UI
from ui_form import Ui_Widget

# Define the grammar
gramatica = CFG.fromstring("""
    E -> E '+' T | E '-' T | T
    T -> T '*' F | T '/' F | F
    F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

# Create a parser using the grammar
parser = ChartParser(gramatica)

def tokenize_expression(expression):
    tokens = re.findall(r'[a-zA-Z0-9]+|[()+\-*/]', expression)
    return tokens


def grammarBreaker(lhs, rhs, seen):
    rhs_str = [str(symbol) if isinstance(symbol, str) else str(symbol) for symbol in rhs]

    # Solo imprimir si esta combinación aún no ha sido vista
    if (lhs, tuple(rhs)) not in seen:
        seen.add((lhs, tuple(rhs)))
        print(f"{lhs} -> {' '.join(rhs_str)}")

# Función para hacer un seguimiento del paso a paso
def stepperTree(parser, expression):
    chart = parser.chart_parse(expression)

    seen = set()  # Conjunto para evitar imprimir combinaciones repetidas

    # Iterar por todas las derivaciones del chart
    for edge in chart:
        lhs = edge.lhs()
        rhs = edge.rhs()

        # Solo procesamos si el LHS es un Nonterminal
        if isinstance(lhs, Nonterminal):
            grammarBreaker(lhs, rhs, seen)

def ast(tree):
    """Simplifies the parse tree to an AST representation."""
    if len(tree) == 1 and isinstance(tree[0], str):
        if tree[0] == '(' or tree[0] == ')':
            return None  # Ignore parentheses
        return Tree(tree[0], [tree[0]])  # Leaf node
    lhs = tree.label()
    if lhs in ['E', 'T', 'F']:
        if len(tree) == 1:
            return ast(tree[0])  # Simplify single child
        if len(tree) == 3:
            operator = tree[1] if isinstance(tree[1], str) else None
            if operator:
                left = ast(tree[0])
                right = ast(tree[2])
                return Tree(operator, [left, right])

class StreamToTextBrowser(io.StringIO):
    def __init__(self, text_browser):
        super().__init__()
        self.text_browser = text_browser

    def write(self, text):
        super().write(text)
        self.text_browser.setPlainText(self.getvalue())  # Update QTextBrowser with the new output


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.okBtn.clicked.connect(self.check)

    def check(self):
        userIn = self.ui.lineEdit.text()  # Get text from lineEdit
        expresion_objetivo = str(userIn)
        butchered_expresion = tokenize_expression(expresion_objetivo)

        # Redirect print to QTextEdit
        stream = StreamToTextBrowser(self.ui.derivationTxt)

        # Set sys.stdout to the custom stream
        sys.stdout = stream

        # Run the process and capture the output
        stepperTree(parser, butchered_expresion)

        stream = StreamToTextBrowser(self.ui.syntaxTree)
        sys.stdout = stream

        # Step 1: Generate the parse tree
        for tree in parser.parse(butchered_expresion):
            print("Original Derivation Tree:")
            tree.pretty_print()  # Display the tree in the console
            tree.draw()  # Open a window with the syntactic tree

            stream = StreamToTextBrowser(self.ui.astTree)
            sys.stdout = stream

            # Now simplify the tree to get the AST
            simplified_ast = ast(tree)
            print("Simplified AST:")
            simplified_ast.pretty_print()  # This will print the AST if it's a valid tree
            simplified_ast.draw()

        # Reset sys.stdout to its original value
        sys.stdout = sys.__stdout__


    def on_tree_drawn(self):
        print("Tree drawing complete!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

