import unittest
import os

import dockerspaniel as ds

class AllTestCase(unittest.TestCase):

    def test_generateContents_works(self):
        data = {
            'from': 'ubuntu:12.04',
            'maintainer': 'John Smith',
            'steps': [
                {
                    'instruction': 'run',
                    'arguments': 'apt-get update'
                },
                {
                    'instruction': 'run',
                    'arguments': 'apt-get install -y nodejs',
                    'only': ['nodejs']
                },
                {
                    'instruction': 'run',
                    'arguments': 'apt-get install -y mysql-server mysql-client',
                    'unless': ['no_database']
                }
            ]
        }

        contents = ds.generateContents(data)
        self.assertEquals(contents, 'FROM ubuntu:12.04\nMAINTAINER John Smith\nRUN apt-get update\nRUN apt-get install -y mysql-server mysql-client')

    def test_createDockerfile_works(self):
        options = {
            'input': './data/Spanielfile'
        }

        ds.createDockerfile(options)

        f = open('./Dockerfile', 'r')
        contents = f.read()
        os.remove('./Dockerfile')

        self.assertEquals(contents, 'FROM ubuntu:12.04\nMAINTAINER John Smith\nRUN apt-get update\nRUN apt-get install -y mysql-server mysql-client\n')





