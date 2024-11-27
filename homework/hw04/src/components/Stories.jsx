import React, { useState, useEffect } from "react";
import { getDataFromServer } from "../server-requests";

import Story from "./Story"

export default function Stories({ token }) {
    const [stories, setStories] = useState([]);

    async function getStories() {
        const data = await getDataFromServer(token, "/api/stories");
        setStories(data);
    }

    useEffect(() => {
        getStories();
    }, []);

    function outputStory(storyObj) {
        return <Story token={token} key={storyObj.id} storyData={storyObj} />
    }

    return (
        <div>
            {
                stories.map(outputStory)
            }
        </div>
        );
}

