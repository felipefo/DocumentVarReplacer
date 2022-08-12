"""
Class responsable for convert a docx documento to pdf
"""
from docx2pdf import convert

from file.writer.strategy.GenericExporter import GenericExporter
from file.ConfigurationReader import ConfigurationReader


class DOCxToPDFExport(GenericExporter):

    def __init__(self, configuration: ConfigurationReader, document_path: str, document_name: str) -> object:
        super().__init__(configuration, document_path, document_name)

    def export(self):

        old_name = self.output_base_path + "\\" + self.document_name
        new_file_name= old_name.replace("docx", "pdf")
        print("old_name:" + new_file_name)
        convert(old_name, new_file_name)


