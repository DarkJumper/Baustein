import pytest

from MsrData import *


def test_para_data_parameter():
    """
    test_para_data_parameter Test der Zerteilung der Liste in Richtige einheiten
    """
    test_para = MsrData()
    test_para.Parameter = ['ParaData', '2', 'test', '1', '2', '3', '4', 'test1', '10', '11', '12', '13']
    assert test_para.Parameter == {
        'test': ('test', '1', '2', '3', '4'),
        'test1': ('test1', '10', '11', '12', '13')
        } and test_para.status == 1


def test_para_data_none():
    """
    test_para_data_none Test rückgabe wert bei übergabe von None
    """
    test_para = MsrData()
    test_para.Parameter = None
    assert test_para.Parameter == {} and test_para.status == -1


def test_para_data_wrong_input():
    """
    test_para_data_wronge_input Test rückgabe wert bei übergabe falsche parameter satztes
    """
    test_para = MsrData()
    test_para.Parameter = ['ParaData', '1', 'test', '1', '2', '3', '4', 'test1', '10', '11', '12', '13']
    assert test_para.Parameter == {} and test_para.status == -2


def test_access():
    """
    test_access Test der Zerteilung der Liste in Richtige einheiten
    """
    test_access = MsrData()
    test_access.Access = ["[UID:ACCMSR]", "3", "ADMIN", "3", "GUEST", "1", "NORMALER USER", "3"]
    assert test_access.Access == {"ADMIN": 3, "GUEST": 1, "NORMALER USER": 3} and test_access.status == 1


def test_access_none():
    """
    test_access_none Test rückgabe wert bei übergabe von None
    """
    test_access = MsrData()
    test_access.Access = None
    assert test_access.Access == {} and test_access.status == -1


def test_access_wronge_input():
    """
    test_access_wronge_input Test rückgabe wert bei übergabe falsche parameter satztes
    """
    test_access = MsrData()
    test_access.Access = ["[UID:ACCMSR]", "2", "ADMIN", "3", "GUEST", "1", "NORMALER USER", "3"]
    assert test_access.Access == {} and test_access.status == -2


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
        } and test_record.status == 1


def test_record_none():
    """
    test_record_none Test rückgabe wert bei übergabe von None
    """
    test_record = MsrData()
    test_record.Record = None
    assert test_record.Record == {} and test_record.status == -1


def test_record_wrong_input():
    """
    test_record_wronge_input Test rückgabe wert bei übergabe falsche parameter satztes
    """
    test_record = MsrData()
    test_record.Record = [
        "[MSR:RECORD]", "0", "G11000", "BST_LIB_MSR", "M_ANA", "B-2", "Hub P-10", "", "256", "1", "", "", "", "", "2"
        ]
    assert test_record.Record == {} and test_record.status == -2
