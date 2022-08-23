"""
Class responsable for open, save and replace all variables in files with ODT format input and output
"""

from docx import Document
from src.file.ConfigurationReader import ConfigurationReader
from src.file.writer.template.GenericTextWriterTemplate import GenericTextWriterTemplate
import re


class WORDReplaceTextWriter(GenericTextWriterTemplate):
    document: Document

    def __init__(self, configuration: ConfigurationReader, document_path: str, document_name: str):
        super().__init__(configuration, document_path, document_name)

    def check_document_type(self):
        if not self.document_path.endswith("doc") and not self.document_path.endswith("DOC") \
                and not self.document_path.endswith("docx") and not self.document_path.endswith("DOCX"):
            raise TypeError("Type not supported")

    def open_document(self):
        self.document = Document(self.document_path)

    def save_document(self):
        new_file_name = self.configuration.get_output_base_path() + "\\" + self.document_name
        print("Saving file on: " + new_file_name)
        self.document.save(new_file_name)

    def replace_variable_document(self):
        input_variables_keys = self.configuration.get_input_variables_keys()
        for paragraph in self.document.paragraphs:
            # Loop through runs (style spans)
            for variable_key in input_variables_keys:
                for run in paragraph.runs:
                    # if there is text on this run, replace it
                    if variable_key in run.text:
                        # get the replacement text
                        if run.text:
                            replaced_text = re.sub(variable_key, self.configuration.get_variable_value(variable_key),
                                                   run.text, 999)
                            if replaced_text != run.text:
                                run.text = replaced_text
