import React from "react";

export default function Profile({ token }) {

    return (
        <header className="flex gap-4 items-center">
            <div>
                <img src="{profile.user.thumb_url}" alt="{profile.user.username}'s profile picture" />
                <h2>{profile.user.username}</h2>
            </div>
        </header>
    );
}
