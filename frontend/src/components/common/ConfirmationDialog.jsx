function ConfirmationDialog({
    open,
    title,
    message,
    itemName,
    confirmText = "Confirm",
    cancelText = "Cancel",
    onConfirm,
    onCancel,
}) {

    if (!open) return null;

    return (
        <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">

            <div className="bg-white rounded-xl shadow-xl w-full max-w-md p-6">

                <h2 className="text-2xl font-bold">
                    {title}
                </h2>

                <p className="text-gray-600 mt-4">
                    {message}
                </p>

                {itemName && (
                    <p className="mt-5 font-semibold text-blue-600">
                        {itemName}
                    </p>
                )}

                <div className="flex justify-end gap-3 mt-8">

                    <button
                        onClick={onCancel}
                        className="
                            px-4
                            py-2
                            rounded-lg
                            border
                            hover:bg-gray-100
                        "
                    >
                        {cancelText}
                    </button>

                    <button
                        onClick={onConfirm}
                        className="
                            px-4
                            py-2
                            rounded-lg
                            bg-blue-600
                            text-white
                            hover:bg-blue-700
                        "
                    >
                        {confirmText}
                    </button>

                </div>

            </div>

        </div>
    );
}

export default ConfirmationDialog;