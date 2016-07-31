import logging
import unittest

from module import widgets

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s [%(filename)s:%(funcName)s]')
log = logging.getLogger(__name__)


class TestDuck(unittest.TestCase):
    def setUp(self):
        self.duck = widgets.Duck()

    def test_add(self):
        log.info('Testing add')
        r = self.duck.add()
        self.assertEqual(r, 3)

    def test_custom_add(self):
        log.info('Ensuring custom adds word')
        a = 3
        b = 39
        self.duck.a = a
        self.duck.b = b
        e = a + b
        r = self.duck.add()
        self.assertEqual(r, e)

    def test_throw(self):
        log.info('Lets make sure things get thrown')
        with self.assertRaises(widgets.RabbitSeason) as cm:
            self.duck.throw_rabbit()

    def test_evade_friend(self):
        p = widgets.PORKY
        log.info('Testing evasion of {}'.format(p))
        r = self.duck.evade(pursuer=p)
        self.assertEqual(r, False)

    def test_evade_foe(self):
        p = widgets.BUGS
        log.info('Testing evasion of {}'.format(p))
        r = self.duck.evade(pursuer=p)
        self.assertEqual(r, True)

    def test_evade_hunter(self):
        p = widgets.FUDD
        log.info('Testing evasion of {}'.format(p))
        with self.assertRaises(widgets.RabbitSeason) as cm:
            r = self.duck.evade(pursuer=p)


class TestFuncs(unittest.TestCase):
    def test_args(self):
        r = widgets.foobar(1, 2, 3)
        self.assertEqual(r, None)