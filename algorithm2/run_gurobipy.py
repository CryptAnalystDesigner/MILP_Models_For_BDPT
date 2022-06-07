from gurobipy import *
import json

cipher = "SIMON"
filename = "test_L.sol"
read_file = cipher + "_select.lp"
m = read(read_file)
m.optimize()
m.write(filename)
f = open(filename, 'r')                  
MILP_Reduce_result = {}
for line in f.readlines():
    line = line.strip()
    if not len(line):
        continue
    MILP_Reduce_result[line.split()[0]] = line.split()[1]
f.close()


Z_list = []
for k, v in MILP_Reduce_result.items():
    if v == '1':
        Z_list.append(k)


file_name = cipher+"_Inequalities.txt"
fileobj = open(file_name, "r")
ine = []   
for i in fileobj:
    ine.append(json.loads(i.strip("\n")))
fileobj.close()

file_MILP = cipher+"_MILPReduce_Inequalities.txt"
file = open(file_MILP, "w")
for z in Z_list:
    z = int(z[1:])
    file.write(str(ine[z]) + "\n")
file.close()

