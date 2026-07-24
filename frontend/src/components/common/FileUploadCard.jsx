import { useState } from "react";
import { UploadCloud } from "lucide-react";



function FileUploadCard({
    selectedFile,
    onChange,
    error,
    predictionResults = [],
    modelVersion,
    onChooseDataset,
    onConfirmReplace,
}) {
   
    const [isDragging, setIsDragging] = useState(false);

    
    


    const formatFileSize = (bytes) => {

    if (bytes < 1024 * 1024) {

        return `${(bytes / 1024).toFixed(1)} KB`;

    }

    return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;

};





    return (

        <div
            onDragOver={(e) => {
                e.preventDefault();
                setIsDragging(true);
            }}

            onDragLeave={() => {
                setIsDragging(false);
            }}

            onDrop={(e) => {
                e.preventDefault();

                setIsDragging(false);

                const file = e.dataTransfer.files[0];

                if (file) {
                    onChange({
                        target: {
                            files: [file],
                        },
                    });
                }
            }}

            className={`
                bg-white
                rounded-xl
                border-2
                border-dashed
                p-10
                text-center
                shadow-sm
                transition-all
                duration-300
                ${
                    isDragging
                        ? "border-blue-600 bg-blue-50"
                        : "border-blue-300"
                }
            `}
        >

            <div className="flex justify-center mb-6">

                <div
                    className="
                        bg-blue-100
                        p-5
                        rounded-full
                    "
                >

                    <UploadCloud
                        size={48}
                        className="text-blue-600"
                    />

                </div>

            </div>

            <h2 className="text-2xl font-bold text-gray-800">

                Upload Engine Dataset

            </h2>

            <p className="text-gray-500 mt-3">

                Upload a CSV or TXT file containing engine sensor readings.

            </p>

           <div className="mt-2 space-y-1">

    <p className="text-sm text-gray-400">

        Drag & Drop CSV/TXT here

    </p>

    <p className="text-xs text-gray-400">

        Maximum file size: 10 MB

    </p>

</div>
            <input
              
                id="engine-file"
                type="file"
                accept=".csv,.txt"
               onChange={(event) => {

    onChange(event);

    event.target.value = "";

}}
                className="hidden"
            />

            <button
    type="button"
    onClick={onChooseDataset}
                className="
                    inline-block
                    bg-blue-600
                    text-white
                    px-6
                    py-3
                    rounded-lg
                    cursor-pointer
                    hover:bg-blue-700
                    transition-all
                    duration-300
                    font-medium
                    mt-6
                "
            >

                {selectedFile ? "Replace Dataset" : "Choose File"}

            </button>

            


            {error && (

    <div
        className="
            mt-6
            bg-red-50
            border
            border-red-300
            rounded-lg
            p-4
        "
    >

        <p className="text-red-700 font-medium">

            ❌ {error}

        </p>

    </div>

)}

            {selectedFile && (

                <div
    className="
        mt-6
        bg-gradient-to-r
        from-blue-50
        to-cyan-50
        border
        border-blue-200
        rounded-xl
        p-6
    "
>

                    <div className="flex items-center justify-between">

    <div>

        <p className="text-sm font-semibold text-blue-600 uppercase">

            Active Dataset

        </p>

        <h3 className="text-xl font-bold text-gray-800 mt-1">

            📄 {selectedFile.name}

        </h3>

    </div>

    <div
        className="
            px-3
            py-1
            rounded-full
            bg-green-100
            text-green-700
            text-sm
            font-semibold
        "
    >

        Prediction Ready

    </div>

</div>

                    <div
    className="
        grid
        grid-cols-1
        md:grid-cols-3
        gap-4
        mt-6
    "
>

    <div>

        <p className="text-xs text-gray-500 uppercase">

            Model

        </p>

        <p className="font-semibold">
    {modelVersion === "v2"
        ? "Generalized GRU (V2)"
        : "GRU (Version 1)"}
</p>

    </div>

    <div>

        <p className="text-xs text-gray-500 uppercase">

            File Type

        </p>

        <p className="font-semibold">

            {selectedFile.type || "TXT / CSV"}

        </p>

    </div>

    <div>

        <p className="text-xs text-gray-500 uppercase">

            Size

        </p>

        <p className="font-semibold">

            {formatFileSize(selectedFile.size)}

        </p>

    </div>

</div>

                    <div
    className="
        mt-6
        flex
        flex-wrap
        items-center
        justify-between
        gap-4
        pt-4
        border-t
    "
>

    <div className="text-sm text-gray-600">

        {predictionResults.length > 0
            ? `${predictionResults.length} engine(s) analyzed`
            : "Prediction not executed"}

    </div>

    <button
    type="button"
    onClick={onChooseDataset}
    className="
        cursor-pointer
        bg-blue-600
        hover:bg-blue-700
        text-white
        px-5
        py-2
        rounded-lg
        font-medium
        transition
    "
>
    Change Dataset
</button>

</div>

                </div>

            )}

            

        </div>

    );

}

export default FileUploadCard;