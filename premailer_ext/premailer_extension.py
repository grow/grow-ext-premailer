import jinja2.ext
import premailer

def do_premailer(value):
    p = premailer.Premailer(value, keep_style_tags=True, remove_classes=False)
    return p.transform()

class PremailerExtension(jinja2.ext.Extension):

    def __init__(self, environment):
        super().__init__(environment)
        environment.filters['premailer'] = do_premailer
