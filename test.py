from __future__ import print_function
import dockerspaniel as ds


print("\n----- generateContents() -----\n")

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
print(contents)


print("\n\n----- createDockerfile() -----\n")
ds.createDockerfile()

print("\n")
