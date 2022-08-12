from file.ConfigurationReader import ConfigurationReader
from file.factory.ExporterFactory import ExporterFactory
from file.factory.WriterFactory import WriterFactory
import logging

from file.writer.strategy.GenericExporter import GenericExporter

""" 
getting the class that handles all configurations like input path, output path and variables that
needs to be replaced into the new document
"""
configuration = ConfigurationReader()
file_names = configuration.get_input_files()

# looping all files in the input directory
for file_name in file_names:

    print("Processing file: " + file_name)
    document_path = configuration.get_input_base_path() + "\\" + file_name
    writer_factory = WriterFactory()

    # getting the Writer based on the document name extension type
    writer_document = writer_factory.get_writer(configuration, document_path, file_name)
    writer_document.build_document_with_variables()

    if configuration.get_exporter() != "":
        exporter_factory = ExporterFactory()
        exporter: GenericExporter
        exporter = exporter_factory.get_exporter(configuration, document_path, file_name)
        exporter.export()
