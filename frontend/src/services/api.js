import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const predictRUL = async (file) => {

    try {

        const formData = new FormData();

        formData.append("file", file);

        const response = await api.post(
            "/predict",
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );

        return response.data;

    } catch (error) {

    throw new Error(
        error.response?.data?.detail ||
        "Prediction failed.",
        {
            cause: error,
        }
    );

}

};







export const predictRULV2 = async (file) => {

    try {

        const formData = new FormData();

        formData.append("file", file);

        const response = await api.post(
            "/version2/predict",
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );

        return response.data;

    } catch (error) {

        throw new Error(
            error.response?.data?.detail ||
            "Version 2 prediction failed."
        );

    }

};
export default api;


export const getExplainability = async () => {

    const response = await api.get(
        "/explain"
    );

    return response.data;

};


export const getUncertainty = async () => {

    const response = await api.get(
        "/uncertainty"
    );

    return response.data;

};