import os
import shutil
import argparse

from platform import python_branch, python_build, python_compiler, python_implementation, python_revision, python_version, python_version_tuple

SetupDir = os.path.realpath(__file__).replace('tmplsetup.py', '')

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
        It is a small tool for copying template files for "scrapy genspider".
        
        After you put your own template files in the tmpl folder, you can send the files to scrapy with tmplsetup.py.
        
        After copying, you can use it as follows.
        
        scrapy genspider -t YOURTEMPNAME <name> <domain>
    ''',
    epilog="""All is well that ends well.""")
args = parser.parse_args()

if 'VIRTUAL_ENV' in os.environ:
    VENV = os.environ['VIRTUAL_ENV']
    for filename in os.listdir(VENV+'/lib/'):
        if ".".join(python_version_tuple()) in filename:
            PythonDir = filename
        elif ".".join(python_version_tuple()[0:2]) in filename:
            PythonDir = filename
        elif ".".join(python_version_tuple()[0:1]) in filename:
            PythonDir = filename

        if PythonDir is not None:
            ScrapyDir = VENV+'/lib/' + PythonDir + '/site-packages/scrapy'
            scTemplateDir = ScrapyDir+'/templates/spiders'
            if os.path.isdir(ScrapyDir):
                if os.path.isdir(scTemplateDir):
                    for TMPLFile in os.listdir(SetupDir+'/'+'tmpl'):
                        if os.path.isfile(scTemplateDir+'/'+TMPLFile) is False:
                            if os.path.isfile(SetupDir+'/tmpl/'+TMPLFile):
                                if shutil.copyfile(SetupDir+'/tmpl/'+TMPLFile, scTemplateDir+'/'+TMPLFile):
                                    print(
                                        'The template named {} was copied successfully.'.format(TMPLFile))
                                else:
                                    print(
                                        'The template named {} could not be copied.'.format(TMPLFile))
                            else:
                                print('I couldn\'t find the template files.')
                        else:
                            print('There is a template named {}.'.format(TMPLFile))
                else:
                    print('The scrapy templates folder could not be reached.')
            else:
                print('Scrapy  not found.')
        else:
            print('Python not found.')
else:
    print('VirtualEnv not found.')
