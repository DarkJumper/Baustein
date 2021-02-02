import pytest

from Baustein import *


def test_para_data_secitons():
    test_para = ParaData()
    test_para.Sections = ['test', '1', '2', '3', '4', 'test1', '10', '11', '12', '13']
    assert test_para.Sections == {'test': ('test', '1', '2', '3', '4'), 'test1': ('test1', '10', '11', '12', '13')}


def test_para_data_none():
    test_para = ParaData()
    test_para.Sections = None
    assert test_para.Sections == {}
