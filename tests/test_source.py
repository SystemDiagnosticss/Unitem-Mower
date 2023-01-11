import pytest
from source.source import Source


def test_img_size():
    source = Source(source_shape=(1080, 1920, 3))
    img = source.get_data()
    assert img.shape == (1080, 1920, 3)


def test_empty_img():
    with pytest.raises(TypeError):
        Source()