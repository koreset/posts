import grpc

from posts_pb2 import PostRequest
from posts_pb2_grpc import PostServiceStub


def run():
    channel = grpc.insecure_channel("localhost:50000")
    client = PostServiceStub(channel)

    author = "jomski2009"
    text = "Lorem ipsum should be the natural way to proceed abi?"

    post = client.CreatePost(PostRequest(author=author, text=text))

    print post.creationdate



if __name__=="__main__":
    run()