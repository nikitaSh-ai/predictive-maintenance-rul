import { createContext, useEffect, useState } from "react";

export const PredictionContext = createContext();

export function PredictionProvider({ children }) {

    const [predictionResults, setPredictionResults] = useState(() => {
      return JSON.parse(localStorage.getItem("predictionResults")) || [];
    });

    const [selectedEngine, setSelectedEngine] = useState(() => {
      return JSON.parse(localStorage.getItem("selectedEngine")) || null;
    });

    
    const [modelVersion, setModelVersion] = useState(() => {
      return localStorage.getItem("modelVersion") || "v2";
    });


    const clearPredictionSession = () => {

    setPredictionResults([]);

    setSelectedEngine(null);

    

    setModelVersion("v2");

    localStorage.removeItem("predictionResults");

    localStorage.removeItem("selectedEngine");

    

    localStorage.removeItem("modelVersion");

};



    useEffect(() => {

    localStorage.setItem(
        "predictionResults",
        JSON.stringify(predictionResults)
    );

}, [predictionResults]);

useEffect(() => {

    localStorage.setItem(
        "selectedEngine",
        JSON.stringify(selectedEngine)
    );

}, [selectedEngine]);



useEffect(() => {

    localStorage.setItem(
        "modelVersion",
        modelVersion
    );

}, [modelVersion]);
    return (

        <PredictionContext.Provider
            value={{
                predictionResults,
                setPredictionResults,

                selectedEngine,
                setSelectedEngine,

                
                modelVersion,
                setModelVersion,

                clearPredictionSession
            }}
        >

            {children}

        </PredictionContext.Provider>

    );

}