import unittest

from tarakanov_kirill_lab1.model.modify_stack import ModifyStack


class TestModifyStack(unittest.TestCase):
    def test_can_create_empty_modify_stack(self):
        stack = ModifyStack()
        self.assertTrue(isinstance(stack, ModifyStack))

    def test_is_empty(self):
        stack = ModifyStack()
        self.assertTrue(stack.is_empty(), True)

    def test_size_return_zero_for_empty_stack(self):
        stack = ModifyStack()
        self.assertEqual(stack.size(), 0)

    def test_push_in_empty_stack_and_look_top_then(self):
        stack = ModifyStack()
        stack._push_empty(2)
        self.assertEqual(stack.look_top(), 2)

    def test_can_push_one_elem_in_stack(self):
        stack = ModifyStack()
        stack._push_empty(2)
        stack._push_one(-5)
        self.assertEqual(stack.look_top(), -5)

    def test_can_pop_from_stack(self):
        stack = ModifyStack()

        stack.push([20, 7, 56, 23])

        stack.pop()
        stack.pop()

        self.assertEqual(stack.look_top(), 7)

    def test_can_find_min_in_stack(self):
        stack = ModifyStack()

        stack.push([10, 20])

        self.assertEqual(stack.find_min(), 10)
