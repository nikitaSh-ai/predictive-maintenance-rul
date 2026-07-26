
import { useState } from "react";

import { Menu } from "lucide-react";

import Navbar from "../components/common/Navbar";
import Sidebar from "../components/common/Sidebar";

function MainLayout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  

    return (

        <div className="h-screen flex flex-col bg-gray-100">

            <Navbar />

            <div className="flex flex-1 overflow-hidden flex-col lg:flex-row">


{
    sidebarOpen && (
        <div
            className="
                fixed
                inset-0
                bg-black/40
                z-40
                lg:hidden
            "
            onClick={() => setSidebarOpen(false)}
        />
    )
}
               <Sidebar
    sidebarOpen={sidebarOpen}
    setSidebarOpen={setSidebarOpen}
/>
<button
    onClick={() => setSidebarOpen(true)}
    className="
        lg:hidden
        m-4
        w-fit
        p-2
        rounded-lg
        bg-blue-600
        text-white
        shadow
    "
>
    <Menu size={24} />
</button>
<main
    className="
        flex-1
        overflow-y-auto
        p-4
        md:p-8
        transition-all
        duration-300
    "
>
                
                    {children}
                </main>

            </div>

        </div>

    );

}

export default MainLayout;