import sys
from metaflac import MetaFlac

metaflac = MetaFlac(sys.argv[1])

#print(metaflac.get_streaminfo())
#print(metaflac.get_application())
#print(metaflac.get_seektable())
print(metaflac.get_vorbis_comment())
raw_data = metaflac.get_picture()["data"]

with open("test.jpg", "wb") as pic_file:

    pic_file.write(raw_data)
#print(metaflac.get_vorbis_comment())