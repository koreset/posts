from uuid import uuid1

import grpc
from concurrent import futures
from datetime import datetime

import posts_pb2_grpc
from models import ConcretePost
from posts_pb2 import Post


class PostServicer(posts_pb2_grpc.PostServiceServicer):
    def CreatePost(self, request, context):
        cpost = ConcretePost()
        cpost.author = request.author
        cpost.text = request.text
        cpost.id = uuid1()
        cpost.creationdate = datetime.now()
        cpost.lastmodified = datetime.now()
        cpost.save()

        post = Post()
        post.author = cpost.author
        post.id = str(cpost.id)
        post.creationdate.FromDatetime(cpost.creationdate)
        post.lastmodified.FromDatetime(cpost.lastmodified)
        post.text = cpost.text

        return post


def serve():
    import time
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    posts_pb2_grpc.add_PostServiceServicer_to_server(PostServicer(), server)
    server.add_insecure_port('[::]:50000')
    server.start()

    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        server.stop(0)



if __name__=="__main__":
    serve()