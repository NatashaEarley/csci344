import json
import traceback

from flask import Response, request
from flask_restful import Resource

from models import db
from models.post import Post
from views import get_authorized_user_ids, can_view_post
from models.bookmark import Bookmark


def get_path():
    return request.host_url + "api/posts/"


class PostListEndpoint(Resource):

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
        
        posts = Post.query.filter(Post.user_id.in_(ids_for_me_and_my_friends)).limit(count)

        data = [item.to_dict(user=self.current_user) for item in posts.all()]
        return Response(json.dumps(data), mimetype="application/json", status=200)

    def post(self):
       data = request.json
       image_url = data.get("image_url")
       caption = data.get("caption")
       alt_text = data.get("alt_text")

       if not image_url:
           return Response(
                json.dumps({"message": "image_url is a required parameter"}),
                mimetype="application/json",
                status=400,
           )

       new_post = Post(
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


class PostDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def patch(self, id):
        print("PATCH id={id}")
        data = request.json
        if not data:
            return Response(
                json.dumps({"Message": "Invalid data or no data provided"}),
                mimetype="application/json",
                status=400,
            )
        
        post = Post.query.get(id)
        
        if not post:
            return Response(
                json.dumps({"Message": f"Post id={id} not found"}),
                mimetype="application/json",
                status=404,
            )

        if post.user_id != self.current_user.id:
            return Response(
                json.dumps({"Message": "You do not have permission to update this post"}),
                mimetype="application/json",
                status=403,
            )
        if data.get("image_url"):
            post.image_url = data.get("image_url")
        if data.get("caption"):
            post.caption = data.get("caption")
        if data.get("alt_text"):
            post.alt_text = data.get("alt_text")
        db.session.commit()
        print(f"Post id={id} updated successfully with data={data}.")
        return Response(
            json.dumps(post.to_dict(user=self.current_user)),
            mimetype="application/json",
            status=200,
        )


    def delete(self, id):
        print("DELETE id=", id)
        
        post = Post.query.get(id)
        if not post:
            return Response(
                json.dumps({"Message": f"Post id={id} not found"}),
                mimetype="application/json",
                status=404,
            )

        if post.user_id != self.current_user.id:
            return Response(
                json.dumps({"Message": "You do not have permission to delete this post"}),
                mimetype="application/json",
                status=403,
            )
        Bookmark.query.filter_by(post_id=id).delete()
        db.session.delete(post)
        db.session.commit()
        return Response(
            json.dumps({"message": f"Post id={id} deleted successfully"}),
            mimetype="application/json",
            status=200,
        )
    #I used ChatGPT to debug the DELETE function
        
    def get(self, id):
        print("POST id=", id)
        can_view = can_view_post(id, self.current_user)
        if (can_view):
            post = Post.query.get(id)
            return Response(
                json.dumps(post.to_dict(user=self.current_user)),
                mimetype="application/json",
                status=200,
            )
        else:
             return Response(
                json.dumps({"Message": f"Post id={id} not found"}),
                mimetype="application/json",
                status=404,
            )



def initialize_routes(api, current_user):
    api.add_resource(
        PostListEndpoint,
        "/api/posts",
        "/api/posts/",
        resource_class_kwargs={"current_user": current_user},
    )
    api.add_resource(
        PostDetailEndpoint,
        "/api/posts/<int:id>",
        "/api/posts/<int:id>/",
        resource_class_kwargs={"current_user": current_user},
    )
