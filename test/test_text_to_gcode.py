import unittest, subprocess, os

class TestTextToGcode(unittest.TestCase):

    in_file = './data/in.txt'
    nc_file = './data/out.nc'
    home_dir = os.path.expanduser('~') + '/Documents/git/label_printer'

    def setUp(self) -> None:
        if os.path.exists(self.in_file):
            os.remove(self.in_file)
        if os.path.exists(self.nc_file):
            os.remove(self.nc_file)
        return super().setUp()

    def test_all_chars(self):
        os.chdir(self.home_dir)
        with open('./data/in.txt', 'w') as f:
            f.write('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_!')
        subprocess.run(['./text_to_gcode.py', '--input', '../' + self.in_file, '--output', '../' + self.nc_file, '--line-length', '75', '--line-spacing', '8', '--padding', '0.5'], cwd=self.home_dir + '/text-to-gcode/')
        print('done')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(verbosity=2)