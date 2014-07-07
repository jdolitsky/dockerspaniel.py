from __future__ import print_function
import six
import copy
import json
import os
import sys
import inspect

CALLER_DIR = os.path.dirname(inspect.getfile(sys._getframe(1)))
if sys.argv[0].endswith('nosetests'):
    CALLER_DIR = os.path.dirname(os.path.realpath(__file__))+'/test'

file_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
with open(file_dir+'/../defaults.json') as defaults_raw:
    DEFAULTS = json.load(defaults_raw)

def generateContents(spaniel, tags=[], is_child=False, root_dir=None):
    contents = []

    if not is_child and not spaniel.get('from'):
        raise Exception('\'from\' attribute does not exist.')

    if spaniel.get('from'):
        contents.append('FROM '+spaniel['from'])

    if isinstance(tags, six.string_types):
        tags = [tags]

    if spaniel.get('maintainer'):
        contents.append('MAINTAINER '+spaniel['maintainer'])

    if not spaniel.get('steps'):
        return "\n".join(contents)

    data = {}
    if spaniel.get('defaults'):
        data = copy.deepcopy(spaniel['defaults'])

    for key in os.environ.keys():
        if len(key) > 3 and key[:3] == 'DS_':
            data[key[3:].lower()] = os.environ[key]

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
    input_file = DEFAULTS['input_file']
    if options.get('input'):
        input_file = os.path.join(CALLER_DIR, options['input'])

    output_file = DEFAULTS['output_file']
    if options.get('output'):
        output_file = os.path.join(CALLER_DIR, options['output'])

    with open(input_file) as json_file:
        spaniel = json.load(json_file)
        contents = generateContents(spaniel)

    f = open(output_file, 'w')
    print(contents, file=f)

    return 1

    if not spaniel.get('steps'):
        return "\n".join(contents)
