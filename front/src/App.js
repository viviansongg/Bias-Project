import React from 'react';
import { Image, Box, Flex, Heading } from '@chakra-ui/react'
import { ChakraProvider } from '@chakra-ui/react'
import Theme from './components/Theme';

import SearchBar from './components/SearchBar';

import BGImage from './assets/background.png'

// import './App.css';

function App() {
  return (
    <ChakraProvider theme={Theme}>
      <Box w='100vw' h='100vh'>
        <Image
          w='100%'
          h='100%'
          src={BGImage}
          backgroundImage="linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.8))"
          position='absolute'
          zIndex='-5' 
          opacity='0.7'
          filter='`brightness(50%)`'
        />
        <Flex 
          h='100%'
          w='100%'
          alignItems='center' 
          justifyContent='center' 
          direction='column'
          gap='1.25rem'
        >
          <Heading fontSize='52px' fontWeight='400' letterSpacing='1px'>bias.io</Heading>
          <SearchBar />
        </Flex>
      </Box>
    </ChakraProvider>
  );
}

export default App;
