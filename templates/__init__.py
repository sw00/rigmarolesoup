from web.template import CompiledTemplate, ForLoop, TemplateResult

import admin, shared, blog
# coding: utf-8
def index (self):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<section id="content">\n'])
    extend_([u'<div class="row pull-left">\n'])
    extend_([u'        <div class="span4">\n'])
    extend_([u'                <img src="" class="img-roundeed" />\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div class="row pull-left">\n'])
    extend_([u'        <div class="span10 offset2">\n'])
    extend_([u'                <h1>rigmarole soup</h1>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="span10 offset2">\n'])
    extend_([u'                <ul class="thumbnails">\n'])
    extend_([u'                        <li class="span4">\n'])
    extend_([u'                        <div class="thumbnail">\n'])
    extend_([u'                                <h3><a href="/blog">blog</a></h3>\n'])
    extend_([u'                                <p>Lots of malarkey and opinions.</p>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                        </li>\n'])
    extend_([u'                        <li class="span4">\n'])
    extend_([u'                                <div class="thumbnail">\n'])
    extend_([u'                                        <h3><a href="http://www.github.com/sw00">code</a></h3>\n'])
    extend_([u'                                        <p>My Github repositories.</p>\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                                </li>\n'])
    extend_([u'                                <li class="span4">\n'])
    extend_([u'                                <div class="thumbnail">\n'])
    extend_([u'                                        <h3><a href="http://flickr.com/settface">photos</a></h3>\n'])
    extend_([u'                                        <p>My flickr</p>\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                                </li>\n'])
    extend_([u'                                <li class="span4">\n'])
    extend_([u'                                <div class="thumbnail">\n'])
    extend_([u'                                        <h3><a href="/social">social</a></h3>\n'])
    extend_([u'                                        <p>Twitter, Facebook, Google+, Last.fm.</p>\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                                </li>\n'])
    extend_([u'                </ul>                   \n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<section id="content">\n'])
    extend_([u'<footer>\n'])
    extend_([u'    <div class="row">\n'])
    extend_([u'        <div class="span10 offset2" style="text-align:center">\n'])
    extend_([u'            Copyright 2012 &copy; Sett Wai\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</footer>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

