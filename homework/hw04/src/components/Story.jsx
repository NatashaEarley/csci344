import React from "react";

export default function Story({ storyData, token }) {
    console.log(storyData)
    return (
        <header className="flex gap-6 bg-white border p-2 overflow-hidden mb-6">
            <div>
                <img src="{storyData.user.thumb_url" class="pic" alt="{storyData.user.username}'s profile picture" />
                <p>{storyData.user.username}</p>
            </div>
        </header>
    );
}