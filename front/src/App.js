import React , { useState } from 'react';
import Popup from './Popup';
import './App.css';

function App() {
  const [isPopupOpen, setPopupOpen] = useState(false);

  const togglePopup = () => {
    setPopupOpen(!isPopupOpen);
  };
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

      <button onClick={togglePopup}>
          Open Pop-up
      </button>

      <Popup isOpen={isPopupOpen} onClose={togglePopup}>
        <div id="HASH" class="blue-msg">
          <div id="left">
            <span id="time-HASH" class="source">Source</span>
          </div>
          <div id="right">
            <span class="date">Date Published</span>
          </div>
        </div>
        <p className="url">https://docs.python.org/3/library/html.parser.html</p>
        <h1 className="title">Title of Article</h1>
        <p className="desc">This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML.</p>
        <h2>Article Summary</h2>
        <p className="desc">Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups. Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups. Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups. Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups.</p>
        <h2 className="summary">Credibility Rating Summary</h2>
        <div class="square1"></div>
        <div class="square2"></div>
        
      </Popup>
    </div>
  );

}

export default App;
