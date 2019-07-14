import React, { useState } from 'react';
import axios from 'axios';
import logo from './peterh-indeed-1.jpg';
import './App.css';

const App = () => {
  const [stem, setStem] = useState('');
  const [anagrams, setAnagrams] = useState([]);

  const refreshList = () => {
    console.log("http://localhost:5000/anagram?stem="+stem);
    axios
      .get("http://localhost:5000/anagram?stem="+stem)
      .then(res => setAnagrams(res.data))
      .catch(err => console.log(err));
    console.log(anagrams);
  };

  const updateStem = (event) => {
    setStem(event.target.value);
    console.log(stem);
    refreshList();
    
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Type in some letters to get all anagrams
        </p>
        <div>
          <input value={stem} onChange={updateStem}/>
          <button>scramble</button>
        </div>
        {/* <Anagrams /> */}
      </header>
    </div>
  );
}

export default App;
