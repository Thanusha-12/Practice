import pytest
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed"
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"


#test sample 1

import pytest
@pytest.mark.set1
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)
@pytest.mark.set2
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"

#test sample 2

import pytest
@pytest.mark.set1
def test_file2_method1():
	x=5
	y=5
	assert x+1 == y,"test failed"
	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)
@pytest.mark.set1
def test_file2_method2():
	x=6
	y=6
	assert x+1 == y,"test failed"

