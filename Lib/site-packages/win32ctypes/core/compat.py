import sys

if sys.version_info[0] >= 3:
    PY3 = True
    PY2 = False
else:
    PY3 = False
    PY2 = True

if PY3:
    def is_unicode(s):
        return isinstance(s, str)

    str = str
else:
    def is_unicode(s):
        return isinstance(s, str)

    str = str
