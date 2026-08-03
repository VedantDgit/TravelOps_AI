import { FaPlaneDeparture } from "react-icons/fa";

function Navbar() {
  return (
    <nav className="bg-slate-900 border-b border-slate-700 h-16 flex items-center justify-between px-8 shadow-lg">

      <div className="flex items-center gap-3">
        <FaPlaneDeparture className="text-blue-400 text-3xl" />

        <div>
          <h1 className="text-white text-2xl font-bold">
            TravelOps AI
          </h1>

          <p className="text-gray-400 text-xs">
            AI Powered Travel Platform
          </p>
        </div>
      </div>

      <div className="text-right">
        <h3 className="text-white font-semibold">
          Welcome 👋
        </h3>

        <p className="text-gray-400 text-sm">
          Travel Intelligence Dashboard
        </p>
      </div>

    </nav>
  );
}

export default Navbar;