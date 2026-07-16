function ErrorCard({

    title = "Something went wrong",

    message = "Please try again."

}) {

    return (

        <div
            className="
                mt-8
                bg-red-50
                border
                border-red-200
                rounded-2xl
                p-8
                text-center
                shadow
            "
        >

            <div className="text-5xl">

                ⚠️

            </div>

            <h2
                className="
                    text-2xl
                    font-bold
                    text-red-700
                    mt-5
                "
            >

                {title}

            </h2>

            <p
                className="
                    mt-3
                    text-gray-600
                "
            >

                {message}

            </p>

        </div>

    );

}

export default ErrorCard;