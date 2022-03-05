import pytest
from metaflac import MetaFlac


@pytest.fixture
def load_fixture():
    """The file below can be obtained from https://archive.org/details/MusopenCollectionAsFlac"""
    return MetaFlac("JohannSebastianBach-03-GoldbergVariationsBwv.988-Variation2.flac")


def test_get_stream_info(load_fixture):

    stream_info = load_fixture.get_streaminfo()

    assert 'minimum_blocksize' in stream_info.keys()
    assert 'maximum_blocksize' in stream_info.keys()
    assert 'minimum_framesize' in stream_info.keys()
    assert 'minimum_framesize' in stream_info.keys()
    assert 'total_samples_in_stream' in stream_info.keys()
    assert 'bits_per_sample' in stream_info.keys()
    assert 'number_of_channels' in stream_info.keys()
    assert 'sample_rate' in stream_info.keys()
    assert 'md5' in stream_info.keys()


def test_get_application_data(load_fixture):

    assert load_fixture.get_application() is None


def test_get_seektable(load_fixture):

    seektable_data = load_fixture.get_seektable()
    stream_info = load_fixture.get_streaminfo()
    
    assert isinstance(seektable_data, list) 

    for data in seektable_data:

        assert data[-1] == stream_info["minimum_blocksize"]


def test_get_picture(load_fixture):

    picture_data = load_fixture.get_picture()
    assert picture_data is None


def test_get_vorbic_comment(load_fixture):

    metadata_fixture = load_fixture.get_vorbis_comment()
    assert "title" in metadata_fixture.keys()
    assert "album" in metadata_fixture.keys()
    assert "genre" in metadata_fixture.keys()
