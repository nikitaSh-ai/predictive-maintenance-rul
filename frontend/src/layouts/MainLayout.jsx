import Navbar from "../components/common/Navbar";
import Sidebar from "../components/common/Sidebar";

function MainLayout({ children }) {
  return (
      <div className="h-screen flex flex-col bg-gray-100">

      <Navbar />

    <div className="flex flex-1 overflow-hidden">

        <Sidebar />

         <main className="flex-1 overflow-y-auto p-8">

          {children}

        </main>

      </div>

    </div>
  );
}

export default MainLayout;