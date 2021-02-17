from help_dec import *
from Freelance import MsrData, FreelanceBase

data2 = [
    "[BEGIN_AREADEFINITION];17", "[AREA];1;!;13;Systembereich", "[AREA];1;-;12;Kein Bereich", "[AREA];1;A;6;Area A",
    "[AREA];1;B;6;Area B", "[AREA];1;C;6;Area C", "[AREA];1;D;6;Area D", "[AREA];1;E;6;Area E", "[AREA];1;F;6;Area F",
    "[AREA];1;G;6;Area G", "[AREA];1;H;6;Area H", "[AREA];1;I;6;Area I", "[AREA];1;J;6;Area J", "[AREA];1;K;6;Area K",
    "[AREA];1;L;6;Area L", "[AREA];1;M;6;Area M", "[AREA];1;N;6;Area N", "[AREA];1;O;6;Area O", "[NOAREA];0"
    ]

test = FreelanceBase()
test.User = None
print(test.User)