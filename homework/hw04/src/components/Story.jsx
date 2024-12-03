import React from "react";

export default function Story({ storyData, token }) {
    console.log(storyData)
    return (
            <div>
                <img src={storyData.user.thumb_url} className="rounded-full border-4 border-gray-300" alt={storyData.user.username} />
                <p>{storyData.user.username}</p>
            </div>
    );
}