import "./Profile.css";
import React from "react";

export default function Profile({ name }) {
    return (
        <section className="profile">
            <h3>Hello, {name}!</h3>
        </section>
    );
}