from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def layout (content, title='rigmarole soup'):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'  <head>\n'])
    extend_([u'    <meta charset="utf-8">\n'])
    extend_([u'        <title>', escape_((title), True), u'</title>\n'])
    extend_([u'        <meta name="robots" content="noindex, nofollow">\n'])
    extend_([u'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'])
    extend_([u'    <meta name="description" content="">\n'])
    extend_([u'    <meta name="author" content="">\n'])
    extend_([u'\n'])
    extend_([u'    <!-- Le styles -->\n'])
    extend_([u'    <link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">\n'])
    extend_([u'    <style>\n'])
    extend_([u'      body {\n'])
    extend_([u'        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */\n'])
    extend_([u'      }\n'])
    extend_([u'    </style>\n'])
    extend_([u'    <link href="/static/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">\n'])
    extend_([u'\n'])
    extend_([u'    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->\n'])
    extend_([u'    <!--[if lt IE 9]>\n'])
    extend_([u'      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>\n'])
    extend_([u'    <![endif]-->\n'])
    extend_([u'\n'])
    extend_([u'    <!-- Le fav and touch icons -->\n'])
    extend_([u'<!--    <link rel="shortcut icon" href="favicon.ico">\n'])
    extend_([u'    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/bootstrap/ico/apple-touch-icon-144-precomposed.png">\n'])
    extend_([u'    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/bootstrap/ico/apple-touch-icon-114-precomposed.png">\n'])
    extend_([u'    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/bootstrap/ico/apple-touch-icon-72-precomposed.png">\n'])
    extend_([u'        <link rel="apple-touch-icon-precomposed" href="/static/bootstrap/ico/apple-touch-icon-57-precomposed.png">-->\n'])
    extend_([u'  </head>\n'])
    extend_([u'\n'])
    extend_([u'  <body>\n'])
    extend_([u'\n'])
    extend_([u'      ', escape_(content, False), u'\n'])
    extend_([u'\n'])
    extend_([u'    <!-- Le javascript\n'])
    extend_([u'    ================================================== -->\n'])
    extend_([u'    <!-- Placed at the end of the document so the pages load faster -->\n'])
    extend_([u'    <script src="static/js/jquery-1.8.2.min.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-transition.js"></script>\n'])
    extend_([u'<!--    <script src="/static/bootstrap/js/bootstrap-alert.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-modal.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-dropdown.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-scrollspy.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-tab.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-tooltip.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-popover.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-button.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-collapse.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-carousel.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-typeahead.js"></script>\n'])
    extend_([u'        -->\n'])
    extend_([u'  </body>\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

layout = CompiledTemplate(layout, 'templates/shared/layout.html')
join_ = layout._join; escape_ = layout._escape

# coding: utf-8
def post_form (form, action):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<form action="POST">\n'])
    extend_([u'        ', escape_(form.render(), True), u'\n'])
    extend_([u'</form>\n'])
    extend_([u'<script type="text/javascript" src="/static/tiny_mce/tiny_mce.js></script>\n'])

    return self

post_form = CompiledTemplate(post_form, 'templates/shared/post_form.html')
join_ = post_form._join; escape_ = post_form._escape

# coding: utf-8
def footer():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'                <div class="span10 offset2" style="text-align:center">\n'])
    extend_([u'                                <hr/>\n'])
    extend_([u'                                View this site on <a href="http://github.com/sw00/rigmarolesoup">GitHub</a></div>\n'])
    extend_([u'                                                                            </div>\n'])

    return self

footer = CompiledTemplate(footer, 'templates/shared/footer.html')
join_ = footer._join; escape_ = footer._escape

# coding: utf-8
def header (title, menus):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    
    user = users.get_current_user()
    if user:
            logout_url = users.create_logout_url('/blog')
    else:
            login_url = users.create_login_url('/blog')
    
    
    extend_([u'<div class="navbar navbar-inverse navbar-fixed-top">\n'])
    extend_([u'      <div class="navbar-inner">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'          <a class="brand" href="#">', escape_(title, False), u'</a>\n'])
    extend_([u'          <div class="nav-collapse collapse">\n'])
    extend_([u'                          <ul class="nav">\n'])
    for m in loop.setup(menus):
        extend_(['                                ', u'    <li ><a href="', escape_(m, False), u'">', escape_(m, False), u'</a></li>\n'])
        extend_(['                                ', u'\n'])
    if user:
        extend_(['                                ', u'    <li><a href="', escape_(logout_url, False), u'">logout</a></li>\n'])
    else:
        extend_(['                                ', u'    <li><a href="', escape_(login_url, False), u'">login</a></li>\n'])
    extend_([u'            </ul>\n'])
    extend_([u'                </div><!--/.nav-collapse -->\n'])
    extend_([u'          </div>\n'])
    extend_([u'      </div>\n'])
    extend_([u'  </div>\n'])

    return self

header = CompiledTemplate(header, 'templates/shared/header.html')
join_ = header._join; escape_ = header._escape

