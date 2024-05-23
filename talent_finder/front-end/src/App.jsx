import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [name, setName] = useState('');
    const [profile, setProfile] = useState(null);

    const handleSearch = async () => {
        try {
            const response = await axios.get(`https://8000-gayatrisj-djangospace-vxsvg4jxspd.ws-us114.gitpod.io/api/users/${name}/`);
            setProfile(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Talent Finder</h1>
            <input 
                type="text" 
                value={name} 
                onChange={(e) => setName(e.target.value)} 
                placeholder="Enter name"
            />
            <button onClick={handleSearch}>Search</button>
            {profile && (
                <div>
                    <h2>{profile.name}</h2>
                    <pre>{JSON.stringify(profile, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}

export default App;
