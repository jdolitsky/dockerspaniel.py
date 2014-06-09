from __future__ import print_function
import json


def generateContents(spaniel, tags=[], is_child=False, root_dir=None):
    contents = []
    contents.append('FROM '+spaniel['from'])

    if spaniel.get('maintainer') is not None:
        contents.append('MAINTAINER '+spaniel['maintainer'])

    for step in spaniel['steps']:
        tmp = step['instruction'].upper()+' '
        tmp += step['arguments']
        contents.append(tmp)

    return "\n".join(contents)


def createDockerfile(options={}):
    input_file = 'Spanielfile'
    output_file = 'Dockerfile'

    with open(input_file) as json_file:
        spaniel = json.load(json_file)
        contents = generateContents(spaniel)

    f = open(output_file, 'w')
    print(contents, file=f)

    print(output_file + ' saved successfully.')
    return 1
