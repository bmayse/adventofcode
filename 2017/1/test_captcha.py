import unittest

from captcha import captcha_next, captcha_across


class TestCaptchaFunctions(unittest.TestCase):
    def test_captcha_next_no_hits(self):
        self.assertEqual(0, captcha_next('12345'))

    def test_captcha_next_one_hit(self):
        self.assertEqual(3, captcha_next('123345'))

    def test_captcha_next_hit_on_wrap(self):
        self.assertEqual(9, captcha_next('9121212129'))

    def test_captcha_next_multiple_hits(self):
        self.assertEqual(6, captcha_next('1223445'))

    def test_captcha_next_empty_string(self):
        self.assertEqual(0, captcha_next(''))

    def test_captcha_across_no_hits(self):
        self.assertEqual(0, captcha_across('1221'))

    def test_captcha_across_one_hit(self):
        self.assertEqual(4, captcha_across('123425'))

    def test_captcha_across_multiple_hits(self):
        self.assertEqual(6, captcha_across('1212'))

    def test_captcha_across_empty_string(self):
        self.assertEqual(0, captcha_across(''))

