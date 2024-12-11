import json

from flask import Response
from flask_restful import Resource

from models.story import Story
from views import get_authorized_user_ids
from flask import Response, request
from models import db


class StoriesListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self):
        ids_for_me_and_my_friends = get_authorized_user_ids(self.current_user)
        try:    
            count = int(request.args.get("limit", 20))
            if count > 50:
                return Response(
                    json.dumps({"message": "The limit is 50"}),
                    mimetype="application/json",
                    status=400,
                )
        except:
            count = 20
            return Response(
                json.dumps({"message": "The limit must be an integer between 1 and 50"}),
                mimetype="application/json",
                status=400,
            )
        
        stories = Story.query.filter(Story.user_id.in_(ids_for_me_and_my_friends)).limit(count)

        data = [item.to_dict(user=self.current_user) for item in stories.all()]
        return Response(json.dumps(data), mimetype="application/json", status=200)

    def post(self):
        data = request.json
        thumb_url = data.get("thumb_url")

        if not thumb_url:
           return Response(
                json.dumps({"message": "thumb_url is a required parameter"}),
                mimetype="application/json",
                status=400,
           )

        new_story = Story(
            thumb_url=thumb_url,
            username=self.current_user.id,
        )
        db.session.add(new_story)
        db.session.commit() 
       
        return Response(
            json.dumps(new_story.to_dict(user=self.current_user)), 
            mimetype="application/json", 
            status=201,
            )



def initialize_routes(api, current_user):
    api.add_resource(
        StoriesListEndpoint,
        "/api/stories",
        "/api/stories/",
        resource_class_kwargs={"current_user": current_user},
    )
