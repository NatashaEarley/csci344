
import React, { useState, useEffect } from "react";
import { getDataFromServer } from "../server-requests";

import Suggestion from "./Suggestion"

export default function Suggestions({ token }) {
    const [suggestions, setSuggestions] = useState([]);

    async function getPosts() {
        const data = await getDataFromServer(token, "/api/suggestions");
        setSuggestions(data);
    }

    useEffect(() => {
        getPosts();
    }, []);

    function outputSuggestion(suggestionObj) {
        return <Suggestion token={token} key={suggestionObj.id} suggestionData={suggestionObj} />
    }

    return (
        <div>
            {
                suggestions.map(outputSuggestion)
            }
        </div>
        );
}