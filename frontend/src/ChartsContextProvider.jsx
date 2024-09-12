import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

export const ChartsDataContext = createContext();

export const ChartsDataProvider = ({ children }) => {
    const [data, setData] = useState(null);

    useEffect(() => {
        axios.get("http://127.0.0.1:5000/")
            .then((res) => {
                console.log(res.data);
                setData(res.data);
            })
            .catch((error) => console.error(error));
    }, []);

    return (
        <ChartsDataContext.Provider value={{data,setData}}>
            {children}
        </ChartsDataContext.Provider>
    );
};
