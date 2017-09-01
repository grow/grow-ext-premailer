# /extensions/premailer.py

from jinja2.ext import Extension
import premailer

def do_premailer(value):
    p = premailer.Premailer(value, keep_style_tags=True, remove_classes=True)
    return p.transform()


class PremailerFilter(Extension):

    def __init__(self, environment):
        super(PremailerFilter, self).__init__(environment)
        environment.filters['premailer'] = do_premailer
