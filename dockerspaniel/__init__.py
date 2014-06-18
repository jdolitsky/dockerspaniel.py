from __future__ import print_function
import copy
import json
import os


def generateContents(spaniel, tags=[], is_child=False, root_dir=None):
    contents = []

    if not is_child and not spaniel['from']:
        raise Exception('\'from\' attribute does not exist.')

    if spaniel['from']:
        contents.append('FROM '+spaniel['from'])

    if isinstance(tags, basestring):
        tags = [tags] 

    if spaniel.get('maintainer'):
        contents.append('MAINTAINER '+spaniel['maintainer'])

    data = {}
    if spaniel.get('defaults'):
        data = copy.deepcopy(spaniel['defaults'])
    
    for key in os.environ.keys():
        if len(key) > 3 and key[:3] == 'DS_':
            data[key[3:].lower()] = os.environ[key]

    if not spaniel.get('steps'):
        return "\n".join(contents)

    for step in spaniel['steps']:
        if step.get('unless'):
            skip = False
            for tag in step['unless']:
                if tag in tags:
                    skip = True
                    break
            if skip:
                continue

        if step.get('only'):
            skip = False
            for tag in step['only']:
                if tag not in tags:
                    skip = True
                    break
            if skip:
                continue

        if step.get('comment') or step.get('newline'):
            contents.append('')
        
        if step.get('comment'):
            contents.append('# '+step['comment'])

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
