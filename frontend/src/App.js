import React, { useState } from 'react';
import axios from 'axios';
import logo from './peterh-indeed-1.jpg';
import './App.css';

const DisplayAnagrams = (words) => {
  const sortedKeys = Object.keys(words).sort().reverse();
  const listItems = sortedKeys.map((key) => <div><h3>{key} letter words</h3><ul>{words[key].map((word) => <li>{word}</li>)}</ul></div>)
  return (listItems)
}

const App = () => {
  const [stem, setStem] = useState('');
  const [anagrams, setAnagrams] = useState([]);

  const refreshList = (value) => {
    axios
      .get("http://localhost:5000/anagram?stem="+value)
      .then(res => setAnagrams(res.data))
      .catch(err => console.log(err));
  };

  const updateStem = (event) => {
    setStem(event.target.value);
    refreshList(event.target.value);
    
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
        </div>
        {DisplayAnagrams(anagrams)}
      </header>
    </div>
  );
}

export default App;
