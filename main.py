from help_dec import *
from FreelanceBase import *

data1 = "[BEGIN_PROJECTHEADER];elektrolyse;Elektrolyse;DeltaControl GmbH;;0;0;2011;9;27;8;34;1;926;Evonik Industries AG, PLT;;;1;1;1;2001;1;30;14;47;31;687;1;14;12;35;54;690;2016;1;690;0;0;0;0;0;0;3444;965;0;0;0;1"
data2 = """[BEGIN_AREADEFINITION];17
[AREA];1;!;13;Systembereich
[AREA];1;-;12;Kein Bereich
[AREA];1;A;6;Area A
[AREA];1;B;6;Area B
[AREA];1;C;6;Area C
[AREA];1;D;6;Area D
[AREA];1;E;6;Area E
[AREA];1;F;6;Area F
[AREA];1;G;6;Area G
[AREA];1;H;6;Area H
[AREA];1;I;6;Area I
[AREA];1;J;6;Area J
[AREA];1;K;6;Area K
[AREA];1;L;6;Area L
[AREA];1;M;6;Area M
[AREA];1;N;6;Area N
[AREA];1;O;6;Area O
[NOAREA];0"""

data3 = "[UID:ACCNODE];6;;0;ELY;0;GUEST;0;HUELS;0;SALZ;0;STUAK;0"
data4 = "[UID:ACCNODE];7;;0;ELY;0;GUEST;0;HUELS;0;SALZ;0;STUAK;0;test;0"
#data4 = "[UID:ACCNODE];0"

data_ = data3.split(";")
print(data_)
test = FreelanceBase()
test.User = data_
print(test.User)
test.User = data4.split(";")
print(test.User)
