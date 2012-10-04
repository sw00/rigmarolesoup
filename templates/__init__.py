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
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html lang="en">\n'])
    extend_([u'  <head>\n'])
    extend_([u'    <meta charset="utf-8">\n'])
    extend_([u'    <title>rigmarole soup</title>\n'])
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
    extend_([u'    <link rel="shortcut icon" href="favicon.ico">\n'])
    extend_([u'    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/bootstrap/ico/apple-touch-icon-144-precomposed.png">\n'])
    extend_([u'    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/bootstrap/ico/apple-touch-icon-114-precomposed.png">\n'])
    extend_([u'    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/bootstrap/ico/apple-touch-icon-72-precomposed.png">\n'])
    extend_([u'    <link rel="apple-touch-icon-precomposed" href="/static/bootstrap/ico/apple-touch-icon-57-precomposed.png">\n'])
    extend_([u'  </head>\n'])
    extend_([u'\n'])
    extend_([u'  <body>\n'])
    extend_([u'\n'])
    extend_([u'    <div class="navbar navbar-inverse navbar-fixed-top">\n'])
    extend_([u'      <div class="navbar-inner">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">\n'])
    extend_([u'            <span class="icon-bar"></span>\n'])
    extend_([u'            <span class="icon-bar"></span>\n'])
    extend_([u'            <span class="icon-bar"></span>\n'])
    extend_([u'          </a>\n'])
    extend_([u'          <a class="brand" href="#">rigmarole soup</a>\n'])
    extend_([u'          <div class="nav-collapse collapse">\n'])
    extend_([u'            <ul class="nav">\n'])
    extend_([u'              <li class="active"><a href="#">Home</a></li>\n'])
    extend_([u'              <li><a href="#about">About</a></li>\n'])
    extend_([u'              <li><a href="#contact">Contact</a></li>\n'])
    extend_([u'            </ul>\n'])
    extend_([u'          </div><!--/.nav-collapse -->\n'])
    extend_([u'        </div>\n'])
    extend_([u'      </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'\n'])
    extend_([u'    <div class="container">\n'])
    extend_([u'\n'])
    extend_([u'      ', escape_(content, False), u'\n'])
    extend_([u'\n'])
    extend_([u'    </div> <!-- /container -->\n'])
    extend_([u'\n'])
    extend_([u'    <!-- Le javascript\n'])
    extend_([u'    ================================================== -->\n'])
    extend_([u'    <!-- Placed at the end of the document so the pages load faster -->\n'])
    extend_([u'    <script src="static/js/jquery-1.8.2.min.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-transition.js"></script>\n'])
    extend_([u'    <script src="/static/bootstrap/js/bootstrap-alert.js"></script>\n'])
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
    extend_([u'\n'])
    extend_([u'  </body>\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

layout = CompiledTemplate(layout, 'templates/layout.html')
join_ = layout._join; escape_ = layout._escape

