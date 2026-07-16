function PageHeader({ title, description }) {

    return (

        <div className="mb-8">
            <h1 className="text-3xl font-bold text-gray-800">

                {title}

            </h1>

            {

                description && (

                    <p className="mt-2 text-gray-500">

                        {description}

                    </p>

                )

            }

        </div>

    );

}

export default PageHeader;