import React from 'react';
import "./Layout.css"
import Newsbox from './Newsbox';

const Main = () => {
    return (
        <main className="main">
            <div className={'main-section politics'}>
                <h2>Politics</h2>
                <p>Content for section 1</p>
                <div >
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                </div>
            </div>
            <div className="main-section general">
                <h2>General</h2>
                <p>Content for section 2</p>
                <div>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                </div>
            </div>
            <div className="main-section sports">
                <h2>Sports</h2>
                <p>Content for section 3</p>
                <div>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                    <Newsbox/>
                </div>
            </div>
        </main>
    );
};

export default Main