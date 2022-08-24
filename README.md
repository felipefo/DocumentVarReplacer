# DocumentVarReplacer
 Replaces variables inside docx documents and exports do pdf.
 This project has the main objectives to get a bunch of docx files annotated with 
variables(template), in order to produce docx and pdf files, replacing those variables driven by a configuration file   

# Cofiguration.properties file 

You need to set variable “file.path.in” to an appropriated path where your documents are located

```
[INPUT]
files.path.in=D:\python\input\com_coorientador
```

"Input Variables" section are all variables that you want to replace in the exported document, 
for instance, if you want to replace from the input variable "c_1" in the exported document
to "Bacharelado de Sistemas de Informação", just declare it as depicted bellow.

*The library used to replace reflects docsx structure, so we used names like c_1, c_2 in order to RUN/SPAN do not split by word spell checks. Then you should not use labels to variables that are words, if you do that, word will break the works in more than one RUN and python library used will not be able to acomplish the replacement in the document. 

```
[INPUT_VARIABLES]
c_1=Bacharelado de Sistemas de Informação
c_2=Bacharel em Sistemas de Informação
```

You need to set variable “file.path.out” to an appropriated path where you want that the created documents needs to be saved.
Also you can set if you want to export to a PDF format, for now PDF is the only one supported
```
[OUTPUT]
#FOLDER WITH OUTPUT FILES 
files.path.out=D:\python\output\documents
# only pdf avaliable for now
export.to.format = PDF
```
Use python3 main.py to run
```
pip install -r requirements.txt
python main.py
```

An example of how to use variables in a template is depcited in the images bellow

![Input template with variables](https://github.com/felipefo/DocumentVarReplacer/blob/main/example_documentation.png)

And the results of that follows:

![Input template with variables](https://github.com/felipefo/DocumentVarReplacer/blob/main/output_example_documentation.png)