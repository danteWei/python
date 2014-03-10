#!/usr/bin/python

from LinkedList import *
import sys, string, tokenize

tokens = iter( sys.stdin.read().split() )
cur_token = None
output = ""
error = False

def lookahead():
  global cur_token

  if cur_token == None:
    try:
      cur_token = tokens.next()
    except:
      cur_token = None

  return cur_token


def next_token():
  global cur_token
  n = lookahead()
  cur_token = None
  return n


def parseS():
  newList = LinkedList()
  parseAtoms(newList)
  Node.print_list(newList.head)
  

def parseAtoms(list):
  tok = lookahead()
    
  if tok == None or tok == ")":
    print "",
  else:
    parseAtom(list)
    parseAtoms(list)


def parseAtom(list):
  tok = lookahead()
    
  if tok == "(":
    newList = LinkedList()
    LinkedList.addFirst(list, newList)
    parseList(newList)
  elif tok == "'":             # quote
    next_token()
    parseAtom()
  elif( str(tok).isdigit() ):       # integer
    LinkedList.addFirst(list, tok)
    next_token()
  else:                        # identifier 
    LinkedList.addFirst(list, tok)
    next_token()
    

def parseList(list):
  global error
  tok = lookahead()
  next_token()
  parseAtoms(list)
  tok = next_token()
  if tok != ")":
    error = True
   
parseS()
tail = lookahead()
if error or tail != None:
  print "Syntax Error"
else:
  print ""


