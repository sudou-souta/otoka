import load
import parser
import sys
tokens = load.loader()
parser.parser(tokens)