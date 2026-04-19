# test_sample.py
# Sample test file demonstrating TDD workflow
# This is a template showing how solutions should be tested
# before implementation is considered complete

import pytest


# ============================================================
# EXAMPLE: Two Sum Problem
# Given an array of integers and a target number,
# return the indices of the two numbers that add up to target
# ============================================================

def two_sum(nums: list, target: int) -> list:
    """
    Two Sum solution.
    Uses a hashmap for O(n) time complexity.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ============================================================
# TESTS — written before implementation per TDD workflow
# ============================================================

class TestTwoSum:

    def test_basic_case(self):
        """Standard case — two numbers add up to target."""
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_middle_elements(self):
        """Target pair is not at the start of the array."""
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_duplicate_numbers(self):
        """Array contains duplicate numbers."""
        assert two_sum([3, 3], 6) == [0, 1]

    def test_negative_numbers(self):
        """Array contains negative numbers."""
        assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    def test_empty_array(self):
        """Edge case — empty array returns empty list."""
        assert two_sum([], 0) == []

    def test_large_input(self, large_input):
        """Performance test — solution works on large input."""
        nums = large_input["array"]
        result = two_sum(nums, 1)
        assert result == [0, 1]