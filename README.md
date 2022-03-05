# MetaFlac

MetaFlac is a library for reading flac metadata with python

```python
import sys
from metaflac import MetaFlac

metaflac = MetaFlac(sys.argv[1])

print metaflac.get_streaminfo()
print metaflac.get_application()
print metaflac.get_seektable()
print metaflac.get_picture()
print metaflac.get_vorbis_comment()
```

You can find the same example in `main.py`

## Disclaimer

Note: This is a project forked from [a-p-z/MetaFlac](https://github.com/a-p-z/MetaFlac) and rewritten in Python3.x.
