import json

from flask import Response, request
from flask_restful import Resource
from models.user import User


def get_path():
    return request.host_url + "api/posts/"


class ProfileDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self):
       data = request.json
       thumb_url = data.get("thumb_url")
       caption = data.get("caption")
       alt_text = data.get("alt_text")

       if not image_url:
           return Response(
                json.dumps({"message": "image_url is a required parameter"}),
                mimetype="application/json",
                status=400,
           )

       new_profile = Profile(
            image_url=image_url,
            user_id=self.current_user.id,
            caption=caption,
            alt_text=alt_text,
        )
       db.session.add(new_post)
       db.session.commit() 
       
       return Response(
            json.dumps(new_post.to_dict(user=self.current_user)), 
            mimetype="application/json", 
            status=201,
            )


def initialize_routes(api, current_user):
    api.add_resource(
        ProfileDetailEndpoint,
        "/api/profile",
        "/api/profile/",
        resource_class_kwargs={"current_user": current_user},
    )
