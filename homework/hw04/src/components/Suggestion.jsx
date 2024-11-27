import React from "react";

export default function Suggestion({ suggestionData, token }) {
    return (
        <div className="mt-4">
            <p className="text-base text-gray-400 font-bold mb-4">
                Suggestions for you
            </p>

            <section className="flex justify-between items-center mb-4 gap-2">
                <img src="{suggestionData.user.thumb_url}" alt="{suggestionData.user.username}'s profile picture" />
                <div>
                    <p>{suggestionData.user.username}</p>
                    <p>suggested for you</p>
                </div>
            </section>
        </div>
    );
}