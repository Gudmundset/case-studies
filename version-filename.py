#print version regex
import re

teststring= "nuke_11.3v4_93.8.xml"

regex = r'(?P<beginning>\S+_)(?P<version>[a-zA-Z0-9\.]+)(?P<end>\.xml)'

result = re.search(regex, teststring)

print(result.group('version'))
