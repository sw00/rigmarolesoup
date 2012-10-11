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
def create (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'        <div class="span10 offset2">\n'])
    if not form.valid:
        extend_(['        ', u'<p class="error"> Try again.</p>\n'])
    extend_([u'        \n'])
    extend_([u'<form name="create" method="POST">\n'])
    extend_([u'        ', escape_(form.render(), False), u'\n'])
    extend_([u'</form>\n'])
    extend_([u'</div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<script type="text/javascript" src="/static/tiny_mce/tiny_mce.js"></script>\n'])
    extend_([u'<script type="text/javascript">\n'])
    extend_([u'        tinyMCE.init({\n'])
    extend_([u'                mode : "textareas",\n'])
    extend_([u'                theme: "simple",\n'])
    extend_([u'                plugins: "autolink,spellchecker,pagebreak,save",\n'])
    extend_([u'\n'])
    extend_([u'                width : "100%",\n'])
    extend_([u'                height : "400"\n'])
    extend_([u'        });\n'])
    extend_([u'</script>\n'])

    return self

create = CompiledTemplate(create, 'templates/blog/create.html')
join_ = create._join; escape_ = create._escape

# coding: utf-8
def preview (d):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div row>\n'])
    extend_([u'        <div class="span10">\n'])
    extend_([u'                <article>\n'])
    extend_([u'                <h3>', escape_(d.title, True), u'</h3>\n'])
    extend_([u'                <small>', escape_(d.category, True), u'</small>\n'])
    extend_([u'                <section class="content">\n'])
    extend_([u'                ', escape_(d.content, False), u'\n'])
    extend_([u'                </section>\n'])
    extend_([u'                <footer>\n'])
    extend_([u'                        <p>', escape_(d.tags, True), u'</p>\n'])
    extend_([u'                </footer>\n'])
    extend_([u'                </article>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

preview = CompiledTemplate(preview, 'templates/blog/preview.html')
join_ = preview._join; escape_ = preview._escape

