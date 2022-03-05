import sys
from metaflac import MetaFlac

metaflac = MetaFlac(sys.argv[1])

print(metaflac.get_streaminfo())
print(metaflac.get_application())
print(metaflac.get_seektable())
print(metaflac.get_picture())
print(metaflac.get_vorbis_comment())