import json

from flask import Response, request
from flask_restful import Resource

from models import db
from models.like_post import LikePost
from models.post import Post
from views import can_view_post


class PostLikesListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
        
    def get(self, id):
        print("POST id=", id)
        can_view = can_view_post(id, self.current_user)
        if (can_view):
            like = LikePost.query.get(id)
            return Response(
                json.dumps(like.to_dict(user=self.current_user)),
                mimetype="application/json",
                status=200,
            )
        else:
             return Response(
                json.dumps({"Message": f"Post id={id} not found"}),
                mimetype="application/json",
                status=404,
            )

class PostLikesDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def delete(self, id):
        print("DELETE id=", id)
        
        like = LikePost.query.get(id)
        if not like:
            return Response(
                json.dumps({"Message": f"This post has not been liked"}),
                mimetype="application/json",
                status=404,
            )

        if Post.user_id != self.current_user.id:
            return Response(
                json.dumps({"Message": "You do not have permission to delete this like"}),
                mimetype="application/json",
                status=403,
            )

        db.session.delete(like)
        db.session.commit()
        return Response(
            json.dumps({"message": f"Like deleted successfully"}),
            mimetype="application/json",
            status=200,
        )




def initialize_routes(api, current_user):
    api.add_resource(
        PostLikesListEndpoint,
        "/api/likes",
        "/api/likes/",
        resource_class_kwargs={"current_user": current_user},
    )

    api.add_resource(
        PostLikesDetailEndpoint,
        "/api/likes/<int:id>",
        "/api/likes/<int:id>/",
        resource_class_kwargs={"current_user": current_user},
    )
