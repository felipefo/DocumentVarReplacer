"""
Class responsable for reading user configurations
"""
import configparser
import os


class ConfigurationReader:
    CONFIGURATION_FILE = "./Configuration.properties"
    input_files = {}
    input_file_path = ""
    output_files = {}
    input_variables = {}
    output_base_path=""
    config: configparser.ConfigParser

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIGURATION_FILE)
        self.input_file_path = self.config['INPUT']['files.path.in']
        self.output_base_path = self.config['OUTPUT']['files.path.out']
        self.input_variables = self.config['INPUT_VARIABLES']

        self.load_file_names()

    def load_file_names(self):
        if not self.input_file_path:
            raise BaseException("Input file path is empty")
        else:
            self.input_files = os.listdir(self.input_file_path)

    def get_input_base_path(self):
        return self.input_file_path

    def get_input_files(self):
        return self.input_files

    def get_variable_value(self, name):
        return self.input_variables[name]

    def get_input_variables_keys(self):
        return self.input_variables.keys()

    def get_output_base_path(self):
        return self.output_base_path

    def get_exporter(self):
        return  self.config['OUTPUT']['export.to.format']