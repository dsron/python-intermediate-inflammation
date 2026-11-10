"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean
from inflammation.models import daily_max, daily_min

import pytest

@pytest.mark.parametrize(
	"test, expected",
	[
		([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
		([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
	])

def test_daily_mean(test, expected):
	"""Test mean function works for array of zeroes and positive integers."""
	npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
	"test, expected",
	[
		([ [1,2], [3,4], [5,6] ], [5,6]),
		([ [0,0], [0,0], [0,0] ], [0,0]),
	    ([ [1,1], [1,1], [1,1] ], [1,1]),
	])

def test_daily_max(test,expected):
	"""Test that the function returns the highest number. Only the general case, there should be testing for cases in which values are repeated etc"""

	npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
        "test, expected",
        [
	        ([ [1,2], [3,4], [5,6] ], [1,2]),
	        ([ [0,0], [0,0], [0,0] ], [0,0]),
	        ([ [1,1], [1,1], [1,1] ], [1,1]),
        ])

def test_daily_min(test,expected):

	npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

def test_daily_min_string():
	"""Test for TypeError when passing strings"""

	with pytest.raises(TypeError):
		error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])
