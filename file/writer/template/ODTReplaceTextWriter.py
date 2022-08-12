"""
Class responsable for open, save and replace all variables in files with ODT format input and output
"""

import odf
from odf.opendocument import load
from odf import text, teletype
from file.ConfigurationReader import ConfigurationReader
from file.writer.template.GenericTextWriterTemplate import GenericTextWriterTemplate


class ODTReplaceTextWriter(GenericTextWriterTemplate):
    document: odf.opendocument

    def __init__(self, configuration: ConfigurationReader, document_path: str, document_name: str):
        super().__init__(configuration, document_path, document_name)

    def check_document_type(self):
        if not self.document_path.endswith("odt") and not not self.document_path.endswith("ODT"):
            raise TypeError("Type not supported")

    def open_document(self):
        self.document = load(self.document_path)
        pass

    def save_document(self):
        new_file_name = self.configuration.get_output_base_path() + "\\" + self.document_name
        print("Saving file on " + new_file_name)
        self.document.save(new_file_name)

    def replace_variable_document(self):
        texts = self.document.getElementsByType(text.P)

        input_variables_keys = self.configuration.get_input_variables_keys()
        length = len(texts)
        for i in range(length):
            try:
                old_text = teletype.extractText(texts[i])
                update_document: bool = False
                for variable_key in input_variables_keys:
                    if variable_key in old_text:
                        new_text = old_text.replace(variable_key,
                                                    self.configuration.get_variable_value(variable_key))
                    old_text = new_text
                    update_document = True

                if update_document:
                    texts[i].setText(new_text)
            except:
                pass

