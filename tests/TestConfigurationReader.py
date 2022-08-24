
import unittest
from src.file.ConfigurationReader import ConfigurationReader


class TesteConfigurationReader(unittest.TestCase):

    def test_variable_reader(self):
        configuration = ConfigurationReader("../tests/TestConfiguration.properties")
        self.assertEqual("./tests/", configuration.get_input_base_path())
        self.assertEqual("./tests/", configuration.get_output_base_path())
        self.assertEqual("Bacharelado de Sistemas de Informacao", configuration.get_variable_value("c_1"))

if __name__ == '__main__':
    unittest.main()
