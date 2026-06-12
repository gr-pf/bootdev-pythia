from collections import namedtuple

PageResult = namedtuple("PageResult", ["page", "next", "options"], defaults=[None])
