import { Text, Box } from "@chakra-ui/react"
import { useState } from "react";
// import Popup from "./Popup.js"
// import './App.css';
import Popup from "./Popup";

export default function Entry({ name, desc }) {
    // const [data, setData] = useState({});
    const [isPopupOpen, setPopupOpen] = useState(false);
    const [data, setData] = useState({});
    const [data2, setData2] = useState({});
    const [data3, setData3] = useState({});
    const [data4, setData4] = useState({});
    const [data5, setData5] = useState({});

    let searchedLink = 'http://127.0.0.1:8080/positivity?url=' + name;
    fetch(searchedLink)
      .then(response => response.json(response))
      .then(data => setData(data))
      .catch(error => console.error('ERROR:', error));

    let searchedLink2 = 'http://127.0.0.1:8080/political?url=' + name;
    fetch(searchedLink2)
    .then(response => response.json(response))
    .then(data2 => setData2(data2))
    .catch(error => console.error('ERROR:', error));

    let searchedLink3 = 'http://127.0.0.1:8080/generate?url=' + name;
    fetch(searchedLink3)
    .then(response => response.json(response))
    .then(data3 => setData3(data3))
    .catch(error => console.error('ERROR:', error));

    let searchedLink4 = 'http://127.0.0.1:8080/citation?url=' + name;
    fetch(searchedLink4)
    .then(response => response.json(response))
    .then(data4 => setData4(data4))
    .catch(error => console.error('ERROR:', error));

    let searchedLink5 = 'http://127.0.0.1:8080/extension?url=' + name;
    fetch(searchedLink5)
    .then(response => response.json(response))
    .then(data5 => setData4(data5))
    .catch(error => console.error('ERROR:', error));

  
    const togglePopup = () => {
      setPopupOpen(!isPopupOpen);
    };

    return (
        <>
            <Box wrap='wrap' className= "article-body" overflowX='scroll' onClick={setPopupOpen}>
                <Text size='32px'>{ name }</Text>
                <span className= "article-description">{desc}</span>
            </Box> 

            <Popup isOpen={isPopupOpen} onClose={togglePopup}>
                <Text>{data[0]}</Text>
                <Text>{data2[0]}% {data2[1]}</Text>
                {/* <Text>{data3[0]}</Text> */}
                <Text>Source Score: {data5[0]}</Text>
                <Text>Number of citations: {data4[0]}</Text>
            </Popup>
        </>
    )
}