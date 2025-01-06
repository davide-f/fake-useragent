import sys

import unittest

from fake_useragent import utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_utils_load(self):
        data = utils.load()

        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 1000)
        self.assertIsInstance(data[0], object)
        self.assertIsInstance(data[0]["percent"], float)
        self.assertIsInstance(data[0]["type"], str)
        self.assertIsInstance(data[0]["device_brand"], str)
        self.assertIsInstance(data[0]["browser"], str)
        self.assertIsInstance(data[0]["browser_version"], str)
        self.assertIsInstance(data[0]["browser_version_major_minor"], float)
        self.assertIsInstance(data[0]["os"], str)
        self.assertIsInstance(data[0]["os_version"], str)
        self.assertIsInstance(data[0]["platform"], str)

    # https://github.com/python/cpython/issues/95299
    @unittest.skipIf(
        sys.version_info >= (3, 12), "not compatible with Python 3.12 (or higher)"
    )
    def test_utils_load_pkg_resource_fallback(self):
        # By default use_local_file is also True during production
        # We will not allow the default importlib resources to be used, by triggering an Exception
        fp1 = utils.find_browser_json_path_pkg_resources()
        fp2 = utils.find_browser_json_path()

        self.assertEqual(fp1, fp2)
