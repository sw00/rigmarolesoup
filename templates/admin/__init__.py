from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'ADMIN\n'])

    return self

index = CompiledTemplate(index, 'templates/admin/index.html')
join_ = index._join; escape_ = index._escape

