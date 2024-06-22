import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

// Step 1: Create a context
const ChartsDataContext = createContext();

// Step 2: Create a provider component
export const ChartsDataProvider = ({ children }) => {
    const [data, setData] = useState({
        route1: null,
        route2: null,
        route3: null,
        route4: null,
        route5: null,
    });

    useEffect(() => {
        // Step 3: Fetch data for each route
        const routes = ['heatmap', 'piechart', 'linechart', 'scatterchart', 'choropleth'];
        routes.forEach(route => {
            axios.get(`http://127.0.0.1:5000/${route}`)
                .then((res) => {
                    setData(prevData => ({ ...prevData, [route]: res.data }));
                })
                .catch((error) => console.error(`Error fetching ${route}:`, error));
        });
    }, []);

    return (
        // Step 4: Provide the data
        <ChartsDataContext.Provider value={data}>
            {children}
        </ChartsDataContext.Provider>
    );
};

// Custom hook to use the context
export const useChartsData = () => useContext(ChartsDataContext);