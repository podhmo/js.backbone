from fanstatic import Library, Resource
from js.underscore import underscore

library = Library('backbone.js', 'resources')
backbone = Resource(library, 'backbone-min.js', depends=[underscore])
