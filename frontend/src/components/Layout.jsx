import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

function Layout({ children }) {
  return (
    <div className="bg-slate-900 min-h-screen">

      <Navbar />

      <div className="flex">

        <Sidebar />

        <main className="flex-1 p-8 overflow-auto">

          {children}

        </main>

      </div>

    </div>
  );
}

export default Layout;