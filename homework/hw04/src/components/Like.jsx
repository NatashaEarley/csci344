import React, {useState} from "react";
import {postDataToServer, deleteDataFromServer} from "../server-requests"

export default function Like({ token, likeId, postId }) {
    const [stateLikeId, setStateLikeId] = useState(likeId);
    
    async function createLike() {
        const sendData = {
            post_id: postId,
        };
        const responseData = await postDataToServer(token, "/api/likes", sendData)
        setStateLikeId(responseData.id);
    }

    async function deleteLike() {
        const url = '/api/likes/' + stateLikeId;
        const responseData = await deleteDataFromServer(token, url);
        setStateLikeId(null);
    }


    if (stateLikeId) {
        return (
            <button aria-label="Unlike" onClick={deleteLike}><i className="fas text-red-700 fa-heart"></i></button>
        );
    } else {return (
        <button aria-label="Like" onClick={createLike}><i className="far fa-heart"></i></button>
    );

    }
}