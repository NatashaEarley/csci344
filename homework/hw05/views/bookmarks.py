import json

from flask import Response, request
from flask_restful import Resource

from models import db
from models.bookmark import Bookmark
from models.post import Post
from sqlalchemy.exc import IntegrityError
from views import can_view_post
from models.post import Post


class BookmarksListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def post(self, id):
        print("GET bookmark_id=", id)
        can_view = can_view_post(id, self.current_user)
        if (can_view):
            bookmarks = Bookmark.query.filter_by(post_id=id).all()
            if bookmarks:
                serialized_bookmarks = [bookmark.to_dict() for bookmark in bookmarks]
                return Response(
                    json.dumps(serialized_bookmarks),
                    mimetype="application/json",
                    status=200,
                )
            else:
                return Response(
                    json.dumps({"Message": f"No bookmark found for post id={id}"}),
                    mimetype="application/json",
                    status=404,
                )
        else:
            return Response(
                json.dumps({"Message": "You do not have permission to view this post's bookmark"}),
                mimetype="application/json",
                status=403,
            )


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
# I worked on the pages and added as far as I can get in the code, 
# but getting the POST to work for Bookmarks is as far as I could get besides the stuff for Posts.
# I keep getting this error: "message": "The method is not allowed for the requested URL."
def delete(self, id):
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
