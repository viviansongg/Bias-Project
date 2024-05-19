import React from 'react';
import './App.css';

function App() {
  return (
    <div>
      <h1 className="title">bias.io</h1>
      <div className="App" style={{
        backgroundImage: `url('assets/background.png')`,
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        height: '100vh',
      }}>
      <input
        className= "searchbar"
        type="text"
        placeholder="type a keyword to get started"
      />
      </div>
    </div>
  );
}

export default App;
