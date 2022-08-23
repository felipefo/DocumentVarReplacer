"""
Class responsable creating exporter for an especific format
"""


from src.file.ConfigurationReader import ConfigurationReader
from src.file.writer.strategy.DOCxToPDFExport import DOCxToPDFExport


class ExporterFactory:

    # get exporter will return the appropriated type of exporter if it is implemented
    def get_exporter(configuration: ConfigurationReader, document_path, file_name):
        exporter = None
        if file_name.endswith("docx") or file_name.endswith("DOCX"):
            exporter = DOCxToPDFExport(configuration, document_path, file_name)
        else:
            raise NotImplemented("Document type not implemented yet")
        return exporter
