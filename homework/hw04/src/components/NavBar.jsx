import React from "react";
import { getDataFromServer } from "../server-requests";

export default function NavBar({ username }) {
    const [navBar, setNavBar] = useState([]);

    async function getNavBar() {
        const data = await getDataFromServer(token, "/api/profile");
        setNavBar(data);
    
    }
    useEffect(() => {
        getNavBar();
    }, []);

    function outputNavBar(profileObj) {
        return <NavBar token={token} key={profileObj.id} postData={profileObj} />
    }

    return (
        <div>
            {
                navBar.map(outputNavBar)
            }
        </div>
        );

    return (
        <nav className="flex justify-between py-5 px-9 bg-white border-b fixed w-full top-0">
            <h1 className="font-Comfortaa font-bold text-2xl">Photo App</h1>
            <ul className="flex gap-4 text-sm items-center justify-center">
                <li>
                    <span>{username}</span>
                </li>
                <li>
                    <button className="text-blue-700 py-2">Sign out</button>
                </li>
            </ul>
        </nav>
    );
}
