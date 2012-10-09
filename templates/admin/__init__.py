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

# coding: utf-8
def blog (posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'        <div class="span8 offset2">\n'])
    extend_([u'                <h2>Blog Posts</h2>\n'])
    extend_([u'                <div class="pull-right">\n'])
    extend_([u'                        <button class="btn btn-action" >create</button>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <table class="table table-striped">\n'])
    extend_([u'                        <tr>\n'])
    extend_([u'                                <th>date</th>\n'])
    extend_([u'                                <th>title</th>\n'])
    extend_([u'                                <th>edit</td>\n'])
    extend_([u'                                <th>delete</td>\n'])
    extend_([u'                        </tr>\n'])
    for p in loop.setup(posts):
        extend_(['                        ', u'    <tr>\n'])
        extend_(['                        ', u'            <td>', escape_(p.created, True), u'</td>\n'])
        extend_(['                        ', u'            <td>', escape_(p.title, True), u'</td>\n'])
        extend_(['                        ', u'            <td><a href="#edit">edit</ad></td>\n'])
        extend_(['                        ', u'            <td><a href="#delete">[x]</a></td>\n'])
        extend_(['                        ', u'    </tr>\n'])
    extend_([u'                </table>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

blog = CompiledTemplate(blog, 'templates/admin/blog.html')
join_ = blog._join; escape_ = blog._escape

