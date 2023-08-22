"""Base class unnittest"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

"""Testcases below"""

class TestBase(unittest.TestCase):
    """A class for unittesting Base class"""

    def check_doc(self):
        """testing the documentation"""
        self.assertTrue(len(Base.__doc__) > 0)

    def check_doc_class(self):
        """testing the documentation"""
        self.assertTrue(len(Base.__doc__) > 0)

    def check_save_to_file(self):
        """testing the documentation"""
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def check_to_json_string(self):
        """testing the documentation"""
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    def check_create(self):
        """testing the documentation"""
        self.assertTrue(len(Base.create.__doc__) > 0)

    def check_load_from_file(self):
        """testing the documentation"""
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def check_from_json_string(self):
        """testing the documentation"""
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def check_empty_arg(self):
        """testing for no arguments"""
        test1 = Base()
        self.assertEqual(test1.id, 1)

    def check_correct_args1(self):
        """testing with correct inputs"""
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base(76)
        self.assertEqual(test2.id, 76)
        test3 = Base()
        self.assertEqual(test3.id, 2)
        test4 = Base(5)
        self.assertEqual(test4.id, 5)
        test5 = Base(-15)
        self.assertEqual(test5.id, -15)
        test6 = Base(-10)
        self.assertEqual(test6.id, -10)

    def check_correct_args2(self):
        """testing multiple arguments"""
        test1 = Base()
        test2 = Base(87)
        test3 = Base()
        self.assertEqual(test3.id, 2)

    def check_correct_args3(self):
        """testing other multiple arguments"""
        test1 = Base()
        test3 = Base(96)
        self.assertEqual(test3.id, 96)

    def check_correct_args4(self):
        """test for non-empty arguments"""
        test2 = Base(0)
        test3 = Base(22)
        self.assertEqual(test3.id, 22)

    def check_instance1(self):
        """test if it is same instance"""
        test1 = Base()
        self.assertTrue(isinstance(test1, Base))
        self.assertEqual(type(test1), Base)

    def check__nb_objects(self):
        """test for object attributes"""
        self.assertFalse(hasattr(Base, '__nb_objects'))

    def check_save_to_file_rect(self):
        """checks if file saves json"""
        instance1 = Rectangle(4, 8, 1, 4)
        instance2 = Rectangle(8, 3)
        Rectangle.save_to_file([instance1, instance2])
        with open("Rectangle.json", "r") as new_file:
            content = new_file.read()
            this_list = Base.from_json_string(content)
            self.assertDictEqual(instance1.to_dictionary(), this_list[0])
            self.assertDictEqual(instance2.to_dictionary(), this_list[1])

    def check_save_none_to_file_r(self):
        """saving none value"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as new_file:
            content = new_file.read()
            this_list = Base.from_json_string(content)
            self.assertListEqual(this_list, [])

    def check_save_empty_rect(self):
        """test for saving to empty file r"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as new_file:
            content = new_file.read()
            this_list = Base.from_json_string(content)
            self.assertListEqual(this_list, [])

    def check_save_both(self):
        """testing for json square"""
        rect = Rectangle(10, 7, 2, 8)
        sqr = Square(2)
        Square.save_to_file([rect, sqr])
        with open("Square.json", "r") as new_file:
            content = new_file.read()
            this_list = Base.from_json_string(content)
            self.assertDictEqual(rect.to_dictionary(), this_list[0])
            self.assertDictEqual(sqr.to_dictionary(), this_list[1])

    def check_save_none_to_file_s(self):
        """test for saving to empty file s"""
        Square.save_to_file(None)
        with open("Square.json", "r") as new_file:
            content = new_file.read()
            this_list = Base.from_json_string(content)
            self.assertListEqual(this_list, [])

    def chexck_save_square(self):
        """testing save square to file"""
        sq = Square(99)
        Square.save_to_file([sq])
        with open("Square.json", "r") as new_file:
            content = new_file.read()
            this_list = Base.from_json_string(content)
            self.assertDictEqual(sq.to_dictionary(), this_list[0])

    def check_rect_create(self):
        """testinf for new rectangle"""
        rect1 = Rectangle(12, 2, 6)
        dict1 = rect1.to_dictionary()
        rect2 = Rectangle.create(**dict1)
        self.assertFalse(rect1 is rect2)
        self.assertDictEqual(dict1, rect2.to_dictionary())

    def check_sq_create(self):
        """testinf for new rectangle"""
        sqr = Square(12, 2, 6)
        dict1 = sqr.to_dictionary()
        sqr1 = Square.create(**dict1)
        self.assertFalse(sqr is sqr1)
        self.assertDictEqual(dict1, sqr1.to_dictionary())

    def check_rect_load_from_file(self):
        """testing to load rectangle file"""
        rect = Rectangle(6, 9, 1, 3)
        rect1 = Rectangle(6, 9)
        new_list = [rect, rect1]
        Rectangle.save_to_file(new_list)
        read_list = Rectangle.load_from_file()
        self.assertEqual(new_list[0].__str__(),
                         "[Rectangle] (1) 1/3 - 6/9")
        self.assertEqual(read_list[0].__str__(),
                         "[Rectangle] (1) 1/3 - 6/9")
        self.assertEqual(new_list[1].__str__(),
                         "[Rectangle] (2) 0/0 - 6/9")
        self.assertEqual(read_list[1].__str__(),
                         "[Rectangle] (2) 0/0 - 6/9")

    def check_sq_load_from_file(self):
        """testing to load square file"""
        sqr = Square(7)
        sqr1 = Square(3, 2, 8)
        new_list = [sqr, sqr1]
        Square.save_to_file(new_list)
        read_list = Square.load_from_file()
        self.assertEqual(new_list[0].__str__(),
                         "[Square] (5) 0/0 - 7")
        self.assertEqual(read_list[0].__str__(),
                         "[Square] (5) 0/0 - 7")
        self.assertEqual(new_list[1].__str__(),
                         "[Square] (6) 2/8 - 3")
        self.assertEqual(read_list[1].__str__(),
                         "[Square] (6) 2/8 - 3")

    def check_wrong_values(self):
        """saving to json with wrong args"""
        check = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as err:
            Base.to_json_string([{9, 8}], [{6, 5}])
        self.assertEqual(check, str(err.exception))

        check1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as err:
            Base.to_json_string()
        self.assertEqual(check1, str(err.exception))


    def check_t_json(self):
        """testing for empty json string """
        test = Base()
        dictn = test.__dict__
        self.assertTrue(type(dictn) is dict)
        string = Base.to_json_string([dictn])
        self.assertTrue(type(string) is str)

    def check_f_json(self):
        """testing for json string with value"""
        test = Base(22)
        dictn = test.__dict__
        string = Base.to_json_string([dictn])
        new_list = Base.from_json_string(string)
        self.assertTrue(type(new_list) is list)
        self.assertTrue(type(string) is str)

if __name__ == "__main__":
    unittest.main()
