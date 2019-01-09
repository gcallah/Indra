"""
This is the test suite for entity.py.
"""

from unittest import TestCase, main

from entity import Entity

LEIBBYEAR = 1646
LEIBDYEAR = 1716
ANM = "age"
AGE = 141.0


def create_leibniz():
    return Entity("Leibniz",
                  {"place": 0.0, "time": LEIBBYEAR},
                  duration=20)


def create_other_leibniz():
    return Entity("Leibniz",
                  {"place": 1.0, "time": LEIBBYEAR},
                  duration=20)


def create_newton():
    return Entity("Newton",
                  {"place": 0.0, "time": 1658.0, "achieve": 43.9},
                  duration=30)


def create_hardy():
    return Entity("Hardy",
                  {ANM: AGE},
                  duration=10)


def create_ramanujan():
    return Entity("Ramanujan", duration=5)


def create_littlewood():
    return Entity("Littlewood", {"friend": 141.0, "number": 1729.0})


def create_ramsey():
    return Entity("Ramsey", {"friend": 282.9, "number": 3.14})


class EntityTestCase(TestCase):
    def test_eq(self):
        l1 = create_leibniz()
        l2 = create_leibniz()
        l3 = create_other_leibniz()
        n = create_newton()
        self.assertTrue(l1 == l2)
        self.assertNotEqual(l1, n)
        self.assertNotEqual(l1, l3)
        # change a field and see that they aren't equal:
        l2["place"] = 1.0
        self.assertNotEqual(l1, l2)

    def test_str(self):
        ent = create_ramanujan()
        self.assertEqual("Ramanujan", str(ent))

    def test_repr(self):
        ent = create_hardy()
        rep = ('{"name": "Hardy", "duration": 10,'
               + ' "attrs": {"' + ANM + '": ' + str(AGE) + '}}')
        self.assertEqual(rep, repr(ent))

    def test_len(self):
        ent = create_newton()
        self.assertEqual(len(ent), 3)

    def test_get(self):
        ent = create_leibniz()
        self.assertEqual(ent["time"], LEIBBYEAR)

    def test_set(self):
        ent = create_leibniz()
        ent["time"] = LEIBDYEAR
        self.assertEqual(ent["time"], LEIBDYEAR)

    def test_contains(self):
        ent = create_leibniz()
        s = "place"
        self.assertTrue(s in ent)

    def test_type(self):
        l1 = create_leibniz()
        l2 = create_other_leibniz()
        n = create_newton()
        self.assertTrue(l1.same_type(l2))
        self.assertFalse(l1.same_type(n))

    def test_iter(self):
        l1 = create_leibniz()
        s = ''
        for attr in l1:
            s += attr
        self.assertEqual(s, "placetime")

    def test_reversed(self):
        l1 = create_leibniz()
        s = ''
        for attr in reversed(l1):
            s += attr
        self.assertEqual(s, "timeplace")

    def test_imul(self):
        h = create_hardy()
        h *= 2.0
        self.assertEqual(h[ANM], AGE * 2.0)

    def test_iadd(self):
        h = create_hardy()
        h += 2.0
        self.assertEqual(h[ANM], AGE + 2.0)

    def test_isub(self):
        h = create_hardy()
        h -= 2.0
        self.assertEqual(h[ANM], AGE - 2.0)

    def test_magnitude(self):
        h = create_hardy()
        self.assertEqual(h.magnitude(), AGE)

    def test_sum(self):
        n = create_newton()
        tsum = sum(n[k] for k in n)
        self.assertAlmostEqual(n.sum(), tsum)


if __name__ == '__main__':
    main()