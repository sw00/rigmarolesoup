from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'BLOG\n'])

    return self

index = CompiledTemplate(index, 'templates/blog/index.html')
join_ = index._join; escape_ = index._escape

