"""
A generic class forces the concrete writer to implement a specific  writer like ODT.
"""

from abc import ABC, abstractmethod

from src.file.ConfigurationReader import ConfigurationReader


class GenericTextWriterTemplate(ABC):

    configuration: ConfigurationReader
    document_path = ""
    output_base_path = ""

    def __init__(self, configuration: ConfigurationReader, document_path: str, document_name: str) -> object:
        self.configuration = configuration
        self.document_path = document_path
        self.document_name = document_name
        self.output_base_path = configuration.get_output_base_path()

    # template method
    def build_document_with_variables(self):
        self.check_document_type()
        self.open_document()
        self.replace_variable_document()
        self.save_document()

    @abstractmethod
    def open_document(self):
        pass

    @abstractmethod
    def check_document_type(self):
        pass

    @abstractmethod
    def save_document(self):
        pass

    # replaces all variables from the input document
    @abstractmethod
    def replace_variable_document(self):
        pass
