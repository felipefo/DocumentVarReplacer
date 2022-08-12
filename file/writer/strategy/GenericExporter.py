"""
A generic class forces the concrete writer to implement a specific  writer like DOCX.
"""
from abc import ABC, abstractmethod

from file.ConfigurationReader import ConfigurationReader


class GenericExporter(ABC):

    configuration: ConfigurationReader
    output_base_path = ""
    document_path = ""
    document_name = ""

    def __init__(self, configuration: ConfigurationReader, document_path, document_name: str) -> object:
        self.configuration = configuration
        self.document_path = document_path
        self.document_name = document_name
        self.output_base_path = self.configuration.get_output_base_path()


    @abstractmethod
    def export(self):
        pass
