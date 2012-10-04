from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<b>well</b>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def layout (content):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE HTML>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'<head>\n'])
    extend_([u'        <meta charset="UTF-8">\n'])
    extend_([u'        <title>rigmarole soup</title>\n'])
    extend_([u'        <style type="text/css" src="/static/bootstrap/css/bootstrap.css"></style>\n'])
    extend_([u'        <script type="text/javascript" src="/static/bootstrap/js/bootstrap.js"></script>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'        ', escape_(content, False), u'       \n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

layout = CompiledTemplate(layout, 'templates/layout.html')
join_ = layout._join; escape_ = layout._escape

