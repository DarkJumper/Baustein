import pytest

from Freelance import *


def test_para_data_parameter():
    """
    test_para_data_parameter Test der Zerteilung der Liste in Richtige einheiten
    """
    test_para = MsrData()
    test_para.Parameter = ['ParaData', '2', 'test', '1', '2', '3', '4', 'test1', '10', '11', '12', '13']
    assert test_para.Parameter == {
        'test': ('test', '1', '2', '3', '4'),
        'test1': ('test1', '10', '11', '12', '13')
        } and test_para.Status == 1


def test_para_data_none():
    """
    test_para_data_none Test rückgabe wert bei übergabe von None
    """
    test_para = MsrData()
    test_para.Parameter = None
    assert test_para.Parameter == {} and test_para.Status == -1


def test_para_data_wrong_input():
    """
    test_para_data_wronge_input Test rückgabe wert bei übergabe falsche parameter satztes
    """
    test_para = MsrData()
    test_para.Parameter = ['ParaData', '1', 'test', '1', '2', '3', '4', 'test1', '10', '11', '12', '13']
    assert test_para.Parameter == {} and test_para.Status == -2


def test_access():
    """
    test_access Test der Zerteilung der Liste in Richtige einheiten
    """
    test_access = MsrData()
    test_access.Access = ["[UID:ACCMSR]", "3", "ADMIN", "3", "GUEST", "1", "NORMALER USER", "3"]
    assert test_access.Access == {"ADMIN": 3, "GUEST": 1, "NORMALER USER": 3} and test_access.Status == 1


def test_access_none():
    """
    test_access_none Test rückgabe wert bei übergabe von None
    """
    test_access = MsrData()
    test_access.Access = None
    assert test_access.Access == {} and test_access.Status == -1


def test_access_wronge_input():
    """
    test_access_wronge_input Test rückgabe wert bei übergabe falsche parameter satztes
    """
    test_access = MsrData()
    test_access.Access = ["[UID:ACCMSR]", "2", "ADMIN", "3", "GUEST", "1", "NORMALER USER", "3"]
    assert test_access.Access == {} and test_access.Status == -2


def test_record():
    """
    test_record Test der Zerteilung der Liste in Richtige einheiten
    """
    test_record = MsrData()
    test_record.Record = [
        "[MSR:RECORD]", "1", "G11000", "BST_LIB_MSR", "M_ANA", "B-2", "Hub P-10", "", "256", "1", "", "", "", "", "2"
        ]
    assert test_record.Record == {
        'MN': 'G11000',
        'LB': 'BST_LIB_MSR',
        'BT': 'M_ANA',
        'KT': 'B-2',
        'LT': 'Hub P-10',
        'AB': '256',
        'ST': '1'
        } and test_record.Status == 1


def test_record_none():
    """
    test_record_none Test rückgabe wert bei übergabe von None
    """
    test_record = MsrData()
    test_record.Record = None
    assert test_record.Record == {} and test_record.Status == -1


def test_record_wrong_input():
    """
    test_record_wronge_input Test rückgabe wert bei übergabe falsche parameter satztes
    """
    test_record = MsrData()
    test_record.Record = [
        "[MSR:RECORD]", "0", "G11000", "BST_LIB_MSR", "M_ANA", "B-2", "Hub P-10", "", "256", "1", "", "", "", "", "2"
        ]
    assert test_record.Record == {} and test_record.Status == -2


def test_projekt():
    test_str = "[BEGIN_PROJECTHEADER];TEST;Test;Ich AG;;0;0;2011;9;27;8;34;1;926;Peter Schwarz;;;1;1;1;2001;1;30;14;47;31;687;1;14;12;35;54;690;2016;1;690;0;0;0;0;0;0;3444;965;0;0;0;1"
    test_proj = FreelanceBase()
    test_proj.Projekt = test_str.split(";")
    assert test_proj.Projekt == {
        'Name': 'TEST',
        'Komi': 'Test',
        'Creator': 'Ich AG',
        'Company': 'Peter Schwarz',
        'Version': '2016',
        'CDate': '27.9.2011'
        } and test_proj.Status == 1


def test_projekt_none():
    test_str = None
    test_proj = FreelanceBase()
    test_proj.Projekt = test_str
    assert test_proj.Projekt == {} and test_proj.Status == -1


def test_user():
    test_case1 = "[UID:ACCNODE];6;;0;ADMIN;0;GUEST;0;SAM;0;SALZIG;0;STUAT;0"
    test_case2 = "[UID:ACCNODE];7;;0;ADMIN;0;GUEST;0;SAM;0;SALZIG;0;STUAT;0;test;0"
    test_case3 = "[UID:ACCNODE];0"
    test_user = FreelanceBase()
    test_user.User = test_case1.split(";")
    test_user.User = test_case2.split(";")
    test_user.User = test_case3.split(";")
    assert test_user.User == ('', 'ADMIN', 'GUEST', 'SAM', 'SALZIG', 'STUAT', 'test') and test_user.Status == 1


def test_user_none():
    test_case = None
    test_user = FreelanceBase()
    test_user.User = test_case
    assert test_user.User == () and test_user.Status == -1


# Area class method muss noch bearbeitet werden!!
def test_area():
    test_list = [
        "[BEGIN_AREADEFINITION];17", "[AREA];1;!;13;Systembereich", "[AREA];1;-;12;Kein Bereich", "[AREA];1;A;6;Area A",
        "[AREA];1;B;6;Area B", "[AREA];1;C;6;Area C", "[AREA];1;D;6;Area D", "[AREA];1;E;6;Area E",
        "[AREA];1;F;6;Area F", "[AREA];1;G;6;Area G", "[AREA];1;H;6;Area H", "[AREA];1;I;6;Area I",
        "[AREA];1;J;6;Area J", "[AREA];1;K;6;Area K", "[AREA];1;L;6;Area L", "[AREA];1;M;6;Area M",
        "[AREA];1;N;6;Area N", "[AREA];1;O;6;Area O", "[NOAREA];0"
        ]
    test_area = FreelanceBase()
    for element in test_list[1:-1]:
        test_area.Area = element.split(";")
    assert test_area.Area == {
        65536: ('!', 'Systembereich'),
        32768: ('-', 'Kein Bereich'),
        16384: ('A', 'Area A'),
        8192: ('B', 'Area B'),
        4096: ('C', 'Area C'),
        2048: ('D', 'Area D'),
        1024: ('E', 'Area E'),
        512: ('F', 'Area F'),
        256: ('G', 'Area G'),
        128: ('H', 'Area H'),
        64: ('I', 'Area I'),
        32: ('J', 'Area J'),
        16: ('K', 'Area K'),
        8: ('L', 'Area L'),
        4: ('M', 'Area M'),
        2: ('N', 'Area N'),
        1: ('O', 'Area O')
        } and test_area.Status == 1


# Area class muss noch geändert werden!!!
def test_area_none():
    test_list = None
    test_area = FreelanceBase()
    test_area.Area = test_list
    assert test_area.Area == {} and test_area.Status == -1
