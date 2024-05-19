import { extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
  fonts: {
    heading: 'sans-serif',
    body: 'sans-serif',
  },
  styles: {
    global: {
      body: {
        fontFamily: 'sans-serif',
      },
    },
  },
});

export default theme;
