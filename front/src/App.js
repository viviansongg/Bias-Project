import React , { useState } from 'react';
import { Flex, Box } from '@chakra-ui/react'

import Popup from './components/Popup';
import './App.css';
import Entry from './components/Entry';

function App() {
  const [isPopupOpen, setPopupOpen] = useState(false);
  const [data, setData] = useState({});
  const [search, setSearch] = useState('');

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      setData({});
      let searchedLink = 'http://127.0.0.1:8080/search?keyword=' + search;
      fetch(searchedLink)
        .then(response => response.json(response))
        .then(data => setData(data))
        .catch(error => console.error('ERROR:', error));

      console.log(data);
    }
  }

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
      <Flex direction='column' justifyContent='center' alignItems='center' gap='2rem'>
        <input
          className="searchbar"
          type="text"
          placeholder="type a keyword to get started ..."
          onKeyDown={handleKeyDown}
          onChange={(event) => {
            setSearch(event.target.value)
          }}
        />
        <Box ml='0rem'>
          <Flex direction='column' w='100%' h='20rem' fontSize='8px'>
            {Object.entries(data).map(([key, value]) => (
              <Entry wrap='wrap' key={key} name={value} desc='description' />
            ))}
          </Flex>
        </Box>
      </Flex>

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
