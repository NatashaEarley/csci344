import json

from flask import Response, request
from flask_restful import Resource
from models.user import User
from models import db


def get_path():
    return request.host_url + "api/posts/"

#"message": "Did not attempt to load JSON data because the request Content-Type was not 'application/json'."
class ProfileDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self):
        data = request.json
        thumb_url = data.get("thumb_url")

        if not thumb_url:
           return Response(
                json.dumps({"message": "thumb_url is a required parameter"}),
                mimetype="application/json",
                status=400,
           )

        new_profile = User(
            thumb_url=thumb_url,
            user_id=self.current_user.id,
        )
        db.session.add(new_profile)
        db.session.commit() 
       
        return Response(
            json.dumps(new_profile.to_dict(user=self.current_user)), 
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
