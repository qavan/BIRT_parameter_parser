import unittest
from birter import CascadeParameter


class MyTestCase(unittest.TestCase):
    def test__init__(self):
        with self.assertRaises(TypeError):
            CascadeParameter(parameters=1)
        with self.assertRaises(TypeError):
            CascadeParameter(parameters='s')
        with self.assertRaises(TypeError):
            CascadeParameter(parameters={})
        with self.assertRaises(TypeError):
            CascadeParameter(parameters={1: 2})
        with self.assertRaises(TypeError):
            CascadeParameter(parameters={1: ""})

    def test_addAttr(self):
        b = CascadeParameter()
        b.addAttr("t", "t")
        self.assertEqual(b.getAttr("t"), "t")
        b.addAttr("te")
        self.assertEqual(b.getAttr("te"), None)

    def test_getAttr(self):
        b = CascadeParameter()
        self.assertEqual(b.getAttr("name"), None)
        self.assertEqual(b.getAttr("description"), None)
        self.assertEqual(b.getAttr("type"), None)
        self.assertEqual(b.getAttr("format"), None)
        self.assertEqual(b.getAttr("hidden"), None)
        self.assertEqual(b.getAttr("required"), None)

    def test_delAttr_raises(self):
        with self.assertRaises(KeyError):
            CascadeParameter().delAttr("xxx")

    def test_updateAttr_raises(self):
        with self.assertRaises(KeyError):
            CascadeParameter().updateAttr("X", '')


if __name__ == '__main__':
    unittest.main()
