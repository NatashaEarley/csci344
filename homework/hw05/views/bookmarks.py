import json

from flask import Response, request
from flask_restful import Resource

from models import db
from models.bookmark import Bookmark
from models.post import Post
from sqlalchemy.exc import IntegrityError
from views import can_view_post, get_authorized_user_ids
from models.post import Post


class BookmarksListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self, id):
        bookmark = Bookmark.query.get(id)
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
        
        bookmark = Bookmark.query.filter(Post.user_id.in_(bookmark)).limit(count)

        data = [item.to_dict(user=self.current_user) for item in posts.all()]
        return Response(json.dumps(bookmark.to_dict()), mimetype="application/json", status=200)


    def get(self, id):
            print("BOOKMARK id=", id)
            if can_view_post(id, self.current_user):
                bookmark = Bookmark.query.get(id)
                if bookmark:
                    return Response(
                        json.dumps(bookmark.to_dict()),
                        mimetype="application/json",
                        status=200,
                    )
                else:
                    return Response(
                        json.dumps({"Message": f"Bookmark id={id} not found"}),
                        mimetype="application/json",
                        status=404,
                    )
            else:
                return Response(
                    json.dumps({"Message": "You do not have permission to view this bookmark"}),
                    mimetype="application/json",
                    status=403,
                )


class BookmarkDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

#I'm stumped by this delete? The GET is also not working but the POST is. 
# I worked a little on other pages too, but getting the POST to work for DELETE is as far as I could get.
# I keep getting this error: "message": "The method is not allowed for the requested URL."
def delete(id):
    try:
        print("DELETE id=", id)
        
        bookmark = Bookmark.query.get(id)
        if not bookmark:
            return Response(
                json.dumps({"Message": f"Bookmark id={id} not found"}),
                mimetype="application/json",
                status=404,
            )

        # Check if the current user has permission to delete
        if bookmark.user_id != self.current_user.id:
            return Response(
                json.dumps({"Message": "You do not have permission to delete this bookmark"}),
                mimetype="application/json",
                status=403,
            )

        # Delete the bookmark
        db.session.delete(bookmark)
        db.session.commit()

        print(f"Bookmark id={id} deleted by user id={self.current_user.id}")

        return Response(
            json.dumps({"Message": f"Bookmark id={id} deleted successfully"}),
            mimetype="application/json",
            status=200,
        )
    except Exception as e:
        print(f"Error deleting bookmark id={id}: {e}")
        return Response(
            json.dumps({"Message": "An unexpected error occurred", "Error": str(e)}),
            mimetype="application/json",
            status=500,
        )


        


def initialize_routes(api, current_user):
    api.add_resource(
        BookmarksListEndpoint,
        "/api/bookmarks",
        "/api/bookmarks/",
        resource_class_kwargs={"current_user": current_user},
    )

    api.add_resource(
        BookmarkDetailEndpoint,
        "/api/bookmarks/<int:id>",
        "/api/bookmarks/<int:id>",
        resource_class_kwargs={"current_user": current_user},
    )
