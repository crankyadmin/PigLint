#!/usr/bin/env python

import re
import argparse
import sys
from os import path

REGISTER = re.compile("REGISTER\s'(.*)'.+")
ALIAS = re.compile("(\w+)\s+=.*(.*)")
STREAM = re.compile("(\w+)(\s|.+)=\s(STREAM|stream)\s(\w+)\s(THROUGH|through)\s(\w+);")
DEFINE = re.compile("^(DEFINE|define)\s(\w+)\s`(\w+.+)`")
GET_ALIAS_REGEX = re.compile("(\w+)(?=\s=)")

PARSE_ALIAS = []
SEEN_ALIAS = []

KEYWORDS = { "and":"", 
    "any":"", 
    "all":"", 
    "arrange":"", 
    "as":"", 
    "asc":"", 
    "AVG":"", 
    "bag":"", 
    "BinStorage":"", 
    "by":"", 
    "bytearray":"", 
    "cache":"", 
    "cat":"", 
    "cd":"", 
    "chararray":"", 
    "cogroup":"", 
    "CONCAT":"", 
    "copyFromLocal":"", 
    "copyToLocal":"", 
    "COUNT":"", 
    "cp":"", 
    "cross":"", 
    "%declare":"", 
    "%default":"", 
    "define":"", 
    "desc":"", 
    "describe":"", 
    "DIFF":"", 
    "distinct":"", 
    "double":"", 
    "du":"", 
    "dump":"", 
    "e":"", 
    "E":"", 
    "eval":"", 
    "exec":"", 
    "explain":"", 
    "f":"", 
    "F":"", 
    "filter":"", 
    "flatten":"", 
    "float":"", 
    "foreach":"", 
    "full":"", 
    "generate":"", 
    "group":"", 
    "help":"", 
    "if":"", 
    "illustrate":"", 
    "inner":"", 
    "input":"", 
    "int":"", 
    "into":"", 
    "is":"", 
    "join":"", 
    "kill":"", 
    "l":"", 
    "L":"", 
    "left":"", 
    "limit":"", 
    "load":"", 
    "long":"", 
    "ls":"", 
    "map":"", 
    "matches":"", 
    "MAX":"", 
    "MIN":"", 
    "mkdir":"",
    "mv":"", 
    "not":"", 
    "null":"", 
    "or":"", 
    "order":"", 
    "outer":"", 
    "output":"", 
    "parallel":"", 
    "pig":"", 
    "PigDump":"", 
    "PigStorage":"", 
    "pwd":"", 
    "quit":"", 
    "register":"", 
    "right":"", 
    "rm":"", 
    "rmf":"", 
    "run":"", 
    "sample":"", 
    "set":"", 
    "ship":"", 
    "SIZE":"", 
    "split":"", 
    "stderr":"", 
    "stdin":"", 
    "stdout":"", 
    "store":"", 
    "stream":"", 
    "SUM":"", 
    "TextLoader":"", 
    "TOKENIZE":"", 
    "through":"", 
    "tuple":"", 
    "union":"", 
    "using":""}

def parse(f):
    """docstring for parse"""
    
    STREAM_DEFS = []

    for line_num, line in enumerate(f):

	if ('DEFINE' or 'define') in line:
	    matched = DEFINE.match(line)
	    STREAM_FUNC = matched.group(2)
	    STREAM_DEFS.append(STREAM_FUNC)

    	if ('REGISTER' or 'register') in line:
	    matched = REGISTER.match(line)
	    UDF_PATH = matched.group(1)
	    if path.exists(UDF_PATH):
		pass
	    else:
		print '%s:%i: %s does not exist' % (f.name, line_num+1, UDF_PATH)
	if ALIAS.match(line):
	    matched = ALIAS.match(line)
	    _ALIAS = matched.group(1)
	    if _ALIAS in PARSE_ALIAS:
		print '%s:%i: Redefining used alias %s' % (f.name, line_num+1, _ALIAS)
	    else:
		PARSE_ALIAS.append(_ALIAS)

	if ('STREAM' or 'stream') in line:
	    matched = STREAM.match(line)
	    DEFINED_STREAM_FUNCTION = matched.group(6)
	    if DEFINED_STREAM_FUNCTION in STREAM_DEFS:
		pass
	    else:
		print '%s:%i: Undefined STREAM function %s' % (f.name, line_num+1, DEFINED_STREAM_FUNCTION)
	    if matched.group(4) not in PARSE_ALIAS:
		print '%s:%i: Undefined alias %s' % (f.name, line_num+1, matched.group(4))

def alias(f):
	"""docstring for alias"""
	for line in f:
	    if GET_ALIAS_REGEX.match(line):
		x = GET_ALIAS_REGEX.match(line)
		SEEN_ALIAS.append(x.group(1))



if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='PigLint')
    ap.add_argument('--file', action='store', dest='FILENAME', help='Pig script to be linted', required=True)
    ap.add_argument('--version', action='version', version='%(prog)s 0.1')
    args = ap.parse_args()
    try:
    	f = open(args.FILENAME)
	alias(f)
    	f = open(args.FILENAME)	
	parse(f)
	f.close()
    except IOError, e:
    	print(e)
	sys.exit(-1)