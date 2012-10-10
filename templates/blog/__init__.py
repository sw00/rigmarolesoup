from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index (posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([escape_(template.header('blog.rigmarolesoup', ['dev','pol','mus','art','sci','fil']), False), u'\n'])
    extend_([u'\n'])
    extend_([u'<section id="content">\n'])
    extend_([u'<div class="row row-fluid" id="content">\n'])
    extend_([u'        <div class="span8" id="content-blogs">\n'])
    for p in loop.setup(posts):
        extend_(['        ', u'    <article>\n'])
        extend_(['        ', u'    <header style="text-align:center">\n'])
        extend_(['        ', u'    <h3><a href="p/', escape_(p.title, True), u'" title="', escape_(p.title, False), u'">', escape_((p.title), True), u'</a></h3>\n'])
        extend_(['        ', u'    <small class="pull-right">', escape_((p.created), True), u'</small>\n'])
        extend_(['        ', u'    <div class="btn-group">\n'])
        extend_(['        ', u'            <a href="#edit" class="btn btn-mini">edit</a>\n'])
        extend_(['        ', u'            <a href="#delete" class="btn btn-mini">delete</a>\n'])
        extend_(['        ', u'    </div>\n'])
        extend_(['        ', u'    </header>\n'])
        extend_(['        ', u'    <div class="body">\n'])
        extend_(['        ', u'                    ', escape_(p.body, False), u'\n'])
        extend_(['        ', u'            </div>\n'])
        extend_(['        ', u'            <footer>\n'])
        extend_(['        ', u'            <hr/>\n'])
        extend_(['        ', u'            </footer>\n'])
    extend_([u'        </article>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div class="span2 pull-left" id="aside">\n'])
    extend_([u'        <form id="search" action="search" method="POST">\n'])
    extend_([u'                <input type="search" placeholder="search..."></input>\n'])
    extend_([u'        </form>\n'])
    extend_([u'        <hr/>\n'])
    extend_([u'        <h4>Categories</h4>\n'])
    extend_([u'        <ul>\n'])
    extend_([u'                <li>stuff</li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'</div>\n'])
    extend_([u'</div>\n'])
    extend_([u'</section>\n'])
    extend_([u'<script type="text/javascript" language="javascript">\n'])
    extend_([u'        \n'])
    extend_([u'</script>\n'])

    return self

index = CompiledTemplate(index, 'templates/blog/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def create (self):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<form action="" method="POST">\n'])
    extend_([u'        <legend>New Blog Entry</legend>\n'])
    extend_([u'        <fieldset>\n'])
    extend_([u'        <label>Title</label>\n'])
    extend_([u'        <input type="text"></input>\n'])
    extend_([u'</fieldset>\n'])
    extend_([u'<fieldset>\n'])
    extend_([u'        <label>Body</label>\n'])
    extend_([u'        <input type="textarea"></input>\n'])
    extend_([u'</fieldset>\n'])
    extend_([u'<fieldset>\n'])
    extend_([u'        <label>References</label>\n'])
    extend_([u'        <select>\n'])
    extend_([u'                <option value="">None</option>\n'])
    extend_([u'        </select>\n'])
    extend_([u'</fieldset>\n'])
    extend_([u'<fieldset>\n'])
    extend_([u'        <label>Tags</label>\n'])
    extend_([u'        <input type="text"></input>\n'])
    extend_([u'</fieldset>\n'])
    extend_([u'<input type="submit">Save</input>\n'])

    return self

create = CompiledTemplate(create, 'templates/blog/create.html')
join_ = create._join; escape_ = create._escape

