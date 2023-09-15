import os
import yaml
import codecs
from pypugjs.utils import process
from pypugjs.ext import jinja


"""
By adding python functions here and then adding them to `on_env`, the functions will become available filters in jinja2.
"""


def filter_data(data, criteria):
    k = criteria['key']
    v = criteria['value']
    if criteria['type'] == 'match':
        return [x for x in data if x[k] == v]
    elif criteria['type'] == 'contains':
        return [x for x in data if v in x[k]]
    else:
        raise NotImplementedError()


def load_data(name, filters=None):
    with open('data/{}.yaml'.format(name)) as f:
        data = yaml.safe_load(f)
    if filters:
        for f in filters:
            data = filter_data(data, f)
    return data


def on_env(env, config, files, **kwargs):
    env.filters['load_data'] = load_data
    env.filters['filter_data'] = filter_data
    return env


def on_pre_build(config):
    for theme_dir in config['theme'].dirs:
        for root, dirs, files in os.walk(theme_dir):
            for fname in files:
                fname = os.path.join(root, fname)
                if fname.endswith('.pug'):
                    fout = fname.replace('.pug', '.html')
                    if os.path.isfile(fout) and os.path.getmtime(fout) > os.path.getmtime(fname):
                        continue
                    with codecs.open(fname, 'r', encoding='utf-8') as f:
                        template = f.read()
                    output = process(
                        template,
                        compiler=jinja.Compiler,
                        staticAttrs=True,
                        extension='.html',
                    )
                    with codecs.open(fout, 'w', encoding='utf-8') as f:
                        f.write(output)
