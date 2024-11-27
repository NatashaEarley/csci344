import React from "react";
import { getDataFromServer } from "../server-requests";

export default function Profile({ profile, token }) {
    const [profiles, setProfile] = useState([]);

    async function getProfile() {
        const data = await getDataFromServer(token, "/api/profile");
        setProfile(data);
    
    }
    useEffect(() => {
        getProfile();
    }, []);

    function outputProfile(profileObj) {
        return <Story token={token} key={profileObj.id} postData={profileObj} />
    }

    return (
        <div>
            {
                profiles.map(outputProfile)
            }
        </div>
        );
}

    return (
        <header className="flex gap-4 items-center">
            <div>
                <img src="{profile.user.thumb_url}" alt="{profile.user.username}'s profile picture" />
                <h2>{profile.user.username}</h2>
            </div>
        </header>
    );
}
