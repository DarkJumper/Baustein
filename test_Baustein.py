import pytest

from Baustein import *


@pytest.fixture
def example_para_data():
    return


def test_para_data_secitons():
    test_para = ParaData()
    test_para.Sections = ['test', '1', '2', '3', '4', 'test1', '10', '11', '12', '13']
    assert test_para.Sections == {'test': ('test', '1', '2', '3', '4'), 'test1': ('test1', '10', '11', '12', '13')}
