import unittest
from unittest.mock import MagicMock
from src.file.ConfigurationReader import ConfigurationReader
from src.file.writer.template.WORDReplaceTextWriter import WORDReplaceTextWriter
from mock import Mock


class TestWordReplaceTextWriter(unittest.TestCase):

    @unittest.expectedFailure
    def test_check_document_type(self):
        mock_configuration = Mock()
        word_replace = WORDReplaceTextWriter(mock_configuration, ".//teste.odt", "")
        word_replace.check_document_type()

    def test_replace_variable_document(self):

        mock_configuration = Mock()
        mock_configuration.get_input_variables_keys.return_value = {"c_1": "replace_c_1"}
        mock_configuration.get_variable_value.return_value = "replace_c_1"
        mock_configuration.output_base_path.return_value = './'
        mock_configuration.get_output_base_path.return_value = './'

        word_replace = WORDReplaceTextWriter(mock_configuration, "./teste.docx", ".//teste_out.docx")

        word_replace.open_document()
        word_replace.replace_variable_document()
        word_replace.save_document()
        error = True
        for paragraph in word_replace.document.paragraphs:
            for run in paragraph.runs:
                # if there is text on this run, replace it
                if "replace_c_1" in run.text:
                    error = False
                    continue

        self.assertEqual(False, error, "O replace não funcionou")


if __name__ == '__main__':
    unittest.main()
