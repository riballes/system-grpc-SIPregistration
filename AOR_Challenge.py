
#AOR Challenge
#Ricardo Morales Ballesteros
#Email: ricardo.morales.b@gmail.com


#ObjectPath Library https://github.com/adriank/ObjectPath

import json
import sys
from objectpath import *

output = ''
a = 0

#loading json file
try:
	with open('/home/riballes/LogMeIn_Jive/aor_reg_correct.json', 'r') as reg_json:
		reg_obj = json.load(reg_json)
except ValueError:
    print "error loading JSON"
    sys.exit()

tesing = '01499acbbaaba2c163000100620005'
string = "$..*[@.addressOfRecord is '" + tesing + "']"

#building a tree to search
reg_data_tree = Tree(reg_obj)
print reg_data_tree
result = reg_data_tree.execute(string)
#print result
#for entry in result:
print json.dumps(result.next())
print type(json.dumps(result.next()))


