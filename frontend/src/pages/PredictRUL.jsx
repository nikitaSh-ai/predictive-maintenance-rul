import ConfirmationDialog from "../components/common/ConfirmationDialog";
import { useState } from "react";
import { useContext } from "react";
import { PredictionContext } from "../context/PredictionContext";
import {
    predictRUL,
    predictRULV2
} from "../services/api";

import FileUploadCard from "../components/common/FileUploadCard";
import Button from "../components/common/Button";
import PredictionCard from "../components/prediction/PredictionCard";
import LoadingSpinner from "../components/common/LoadingSpinner";
import FleetSummary from "../components/prediction/FleetSummary";
import EngineTable from "../components/prediction/EngineTable";

function PredictRUL() {

    const {

    predictionResults,
    setPredictionResults,

    selectedEngine,
    setSelectedEngine,

    selectedFile,
    setSelectedFile,

    modelVersion,
    setModelVersion

    } = useContext(PredictionContext);

    
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    
    const [success, setSuccess] = useState("");
    const [showConfirmDialog, setShowConfirmDialog] = useState(false);

    const handleFileChange = (event) => {

        

    const file = event.target.files[0];

    setPredictionResults([]);

setSelectedEngine(null);

setSuccess("");

setError("");

    if (!file) return;
    const MAX_FILE_SIZE = 10 * 1024 * 1024;

    if (file.size > MAX_FILE_SIZE) {

    setSelectedFile(null);

    setError("File size must not exceed 10 MB.");

    return;

}

    const allowedExtensions = [".csv", ".txt"];

    const fileName = file.name.toLowerCase();

    const isValid = allowedExtensions.some(extension =>
        fileName.endsWith(extension)
    );

    if (!isValid) {

        setSelectedFile(null);

        setError("Only CSV and TXT files are allowed.");

        return;

    }

    setError("");
    setSelectedFile(file);
};




const handleChooseDataset = () => {

    if (selectedFile) {

        setShowConfirmDialog(true);

    } else {

        document.getElementById("engine-file").click();

    }

};




const handlePredict = async () => {

    if (!selectedFile) {

        setError("Please select a CSV or TXT file.");

        return;

    }

    setError("");

    setIsLoading(true);
    try {
console.log(selectedFile);
console.log(selectedFile instanceof File);
    const result =
    modelVersion === "v2"
        ? await predictRULV2(selectedFile)
        : await predictRUL(selectedFile);

    
    console.log(result.predictions[0]);


    setPredictionResults(result.predictions);


    setSuccess(
    `Prediction completed successfully using ${
        modelVersion === "v2"
            ? "Version 2 (Generalized Model)"
            : "Version 1 (FD001 Model)"
    }.`
);
setTimeout(() => {

    setSuccess("");

}, 3000);

}
    catch (error) {

      setError(
        error.message ||
        "Prediction failed."
      );

    }

    
    
    finally {

      setIsLoading(false);

    }
};



    return (

        <div className="space-y-8">

            <div>

                <h1 className="text-3xl font-bold">

                    Predict Remaining Useful Life

                </h1>

                {
    success && (
        <div
            className="
                mt-6
                mb-6
                p-4
                rounded-xl
                border
                border-green-300
                bg-green-50
                text-green-700
                font-medium
            "
        >
            ✅ {success}
        </div>
    )
}

                <p className="text-gray-500 mt-2">

                    Upload engine sensor data to estimate Remaining Useful Life.

                </p>

            </div>


            <div className="mt-6">
    <label className="block text-sm font-medium mb-2">
        Model Version
    </label>

    <select
        value={modelVersion}
        onChange={(e) => setModelVersion(e.target.value)}
        className="
            w-full
            max-w-xs
            border
            rounded-lg
            px-3
            py-2
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
        "
    >
        <option value="v2">
            Version 2 (Generalized)
        </option>

        <option value="v1">
            Version 1 (FD001)
        </option>
    </select>
</div>

           <FileUploadCard
    selectedFile={selectedFile}
    onChange={handleFileChange}
    error={error}
    predictionResults={predictionResults}
    modelVersion={modelVersion}
    onChooseDataset={handleChooseDataset}
/>


            <Button
    onClick={handlePredict}
    disabled={isLoading}
>

    {isLoading ? "Predicting..." : "Predict RUL"}

</Button>




{
    isLoading && <LoadingSpinner />
}
  {
    predictionResults.length > 0 && (

        <>
<FleetSummary
    predictions={predictionResults}
/>

{
    selectedEngine && (
        <PredictionCard
            prediction={selectedEngine}
        />
    )
}

<EngineTable
    predictions={predictionResults}
    onView={(engine) => {
        console.log(engine);
        setSelectedEngine(engine);
    }}
/>
          
        </>

    )
}



<ConfirmationDialog
    open={showConfirmDialog}
    title="Change Active Dataset?"
    message="Changing the dataset will clear the current prediction session."
    itemName={selectedFile?.name}
    confirmText="Change Dataset"
    cancelText="Cancel"
    onCancel={() => setShowConfirmDialog(false)}
    onConfirm={() => {

    setShowConfirmDialog(false);

    document.getElementById("engine-file").click();

}}
/>


  </div>

    );

}

export default PredictRUL;