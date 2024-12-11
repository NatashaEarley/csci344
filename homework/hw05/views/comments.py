import json

from flask import Response, request
from flask_restful import Resource
from models.post import Post
from models import db
from models.comment import Comment
from views import can_view_post


class CommentListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def post(self):
        print("COMMENTS post_id=", id)
        can_view = can_view_post(id, self.current_user)
        if (can_view):
            comments = Comment.query.filter_by(post_id=id).all()
            if comments:
                serialized_comments = [comment.to_dict() for comment in comments]
                return Response(
                    json.dumps(serialized_comments),
                    mimetype="application/json",
                    status=200,
                )
            else:
                return Response(
                    json.dumps({"Message": f"No comments found for post id={post_id}"}),
                    mimetype="application/json",
                    status=404,
                )
        else:
            return Response(
                json.dumps({"Message": "You do not have permission to view this post's comments"}),
                mimetype="application/json",
                status=403,
            )
        


class CommentDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def delete(self, id):
        # TODO: Add DELETE logic...
        print(id)

        return Response(
            json.dumps({}),
            mimetype="application/json",
            status=200,
        )


def initialize_routes(api, current_user):
    api.add_resource(
        CommentListEndpoint,
        "/api/comments",
        "/api/comments/",
        resource_class_kwargs={"current_user": current_user},
    )
    api.add_resource(
        CommentDetailEndpoint,
        "/api/comments/<int:id>",
        "/api/comments/<int:id>/",
        resource_class_kwargs={"current_user": current_user},
    )
