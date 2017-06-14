from posts_pb2 import Post, PostRequest
from services.sample_service import adding
from myexceptions import NumberFormatError
import pytest

def test_addition_works():
    assert adding(2,2) == 4

def test_only_numbers_as_args():
    with pytest.raises(NumberFormatError, message='Expecting a NumberFormatError exception'):
        adding("jome","jome")


def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 2 == 2

def test_can_create_post_with_text_and_author():
    author = "jomski2009"
    text = "Dummy text"

    post = Post()
    post.text = text
    post.author = author

    request = PostRequest()

    assert CreatePost