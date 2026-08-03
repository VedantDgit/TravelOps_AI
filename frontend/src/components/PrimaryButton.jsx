import ClipLoader from "react-spinners/ClipLoader";

function PrimaryButton({ loading, children, onClick }) {
  return (
    <button
      onClick={onClick}
      disabled={loading}
      className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-xl text-white font-semibold"
    >
      {loading ? (
        <ClipLoader color="white" size={18} />
      ) : (
        children
      )}
    </button>
  );
}

export default PrimaryButton;