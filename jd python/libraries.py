import random
import subprocess

for i in range(5):
    print(random.randint(1,100))

output = subprocess.check_output('dir',shell=True)
print(output)
output2 = subprocess.check_output('ipconfig',shell=True)
print(output2)

output3 = subprocess.check_output('cd',shell=True)
print(output3)

subprocess.Popen('mkdir test',shell=True)
