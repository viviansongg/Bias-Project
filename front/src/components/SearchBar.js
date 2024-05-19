import React from 'react'
import { Box, InputGroup, Input, InputLeftElement } from '@chakra-ui/react'
import { SearchIcon } from '@chakra-ui/icons'

export default function SearchBar() {
    return (
        <>
            <Box w='35%'>
                <InputGroup>
                    <InputLeftElement pointerEvents='none'>
                        <SearchIcon />
                    </InputLeftElement>
                    <Input variant='filled' placeholder='type a key to get started ...' _hover={{ opacity: 0.8 }} />
                </InputGroup>
            </Box>
            
        </>
    );
}