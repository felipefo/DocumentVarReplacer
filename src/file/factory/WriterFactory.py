"""
Class responsable creating replacer for an especific format
"""
from src.file.ConfigurationReader import ConfigurationReader
from src.file.writer.template.ODTReplaceTextWriter import ODTReplaceTextWriter
from src.file.writer.template.WORDReplaceTextWriter import WORDReplaceTextWriter


class WriterFactory:

    # get writer will return the appropriated type of writer if it is implemented
    def get_writer(configuration: ConfigurationReader, document_path, file_name):
        replace_writer = None
        if file_name.endswith("ODT") or file_name.endswith("odt"):
            replace_writer = ODTReplaceTextWriter(configuration, document_path, file_name)
        elif file_name.endswith("docx") or file_name.endswith("DOCX"):
            replace_writer = WORDReplaceTextWriter(configuration, document_path, file_name)
        else:
            raise Exception("Document type not implemented yet")
        return replace_writer
