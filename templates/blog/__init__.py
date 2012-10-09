from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index (posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'        <div class="span8">\n'])
    for p in loop.setup(posts):
        extend_(['        ', u'    <div class="well">\n'])
        extend_(['        ', u'            <h3>', escape_((p.title), True), u'</h3>\n'])
        extend_(['        ', u'            <small>', escape_((p.created), True), u'</small>\n'])
        extend_(['        ', u'            <section class="body">\n'])
        extend_(['        ', u'                    ', escape_(p.body, False), u'\n'])
        extend_(['        ', u'            </section>\n'])
        extend_(['        ', u'    </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

index = CompiledTemplate(index, 'templates/blog/index.html')
join_ = index._join; escape_ = index._escape

