import grpc

from posts_pb2 import PostRequest, PostByIdRequest, PostByAuthorRequest
from posts_pb2_grpc import PostServiceStub

channel = grpc.insecure_channel("localhost:50000")
client = PostServiceStub(channel)

def run():
    author = "jomski2009"
    text = "Yookos, eeklesia, something else? What's the answer people?"

    post = client.CreatePost(PostRequest(author=author, text=text))
    print post.creationdate
    print post.id

    post1 = client.GetPostById(PostByIdRequest(id=post.id))

    print post1.text

    posts = client.GetPostsByAuthor(PostByAuthorRequest(author="jomski2009"))

    for post in posts:
        print post.text



if __name__=="__main__":
    run()