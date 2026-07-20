
import { useState } from "react";
import {
    predictRUL,
    predictRULV2
} from "../services/api";

import FileUploadCard from "../components/common/FileUploadCard";
import Button from "../components/common/Button";
import PredictionCard from "../components/prediction/PredictionCard";
import LoadingSpinner from "../components/common/LoadingSpinner";



function PredictRUL() {

    const [selectedFile, setSelectedFile] = useState(null);
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [predictionResult, setPredictionResult] = useState(null);
    const [success, setSuccess] = useState("");
    const [modelVersion, setModelVersion] = useState("v2");


    

    const handleFileChange = (event) => {

    const file = event.target.files[0];

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


const handlePredict = async () => {

    if (!selectedFile) {

        setError("Please select a CSV or TXT file.");

        return;

    }

    setError("");

    setIsLoading(true);
    try {

    const result =
    modelVersion === "v2"
        ? await predictRULV2(selectedFile)
        : await predictRUL(selectedFile);

    setPredictionResult({
    engine_id: result.engine_id,
    predicted_rul: result.predicted_rul,
    risk: result.risk,
    priority: result.priority,
    confidence: result.confidence,
    healthScore: result.health_score,
    recommendation: result.recommendation,
    inspection: result.inspection,
    focus: result.focus,
    summary: result.summary,
    uncertainty: result.uncertainty,
    reason: result.reason,
});

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
    predictionResult && (

        <PredictionCard
            prediction={predictionResult}
        />

    )
}
        </div>

    );

}

export default PredictRUL;