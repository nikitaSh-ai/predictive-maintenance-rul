import { useState } from "react";
import { UploadCloud } from "lucide-react";

function FileUploadCard({
    selectedFile,
    onChange,
    error,
}) {

    const [isDragging, setIsDragging] = useState(false);

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
                onChange={onChange}
                className="hidden"
            />

            <label
                htmlFor="engine-file"
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

                Choose File

            </label>

            {!selectedFile && (

                <p className="mt-4 text-gray-500">

                    No file selected

                </p>

            )}


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
                        bg-blue-50
                        rounded-lg
                        p-4
                    "
                >

                    <p className="font-medium text-blue-700">

                        ✅ Selected File

                    </p>

                    <p className="font-semibold text-gray-800 mt-1">

                        {selectedFile.name}

                    </p>

                    <p className="text-sm text-gray-600 mt-2">

                        Type : {selectedFile.type || "Unknown"}

                    </p>

                    <p className="text-sm text-gray-600">

                        Size : {(selectedFile.size / (1024 * 1024)).toFixed(2)} MB

                    </p>

                </div>

            )}

        </div>

    );

}

export default FileUploadCard;