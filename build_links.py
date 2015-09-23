#!/usr/bin/env python

import json
import os
import sys

from jinja2 import Environment, Template, FileSystemLoader

this_dir = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader = FileSystemLoader(os.path.join(this_dir, 'templates')))
template = env.get_template('index.html')
links = json.load(open(os.path.join(this_dir, 'links.json'), 'r'))
html = template.render(links=links)

open('index.html', 'w').write(html)
