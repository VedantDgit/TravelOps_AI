function ResultCard({ title, value }) {
  return (
    <div className="bg-slate-800 rounded-2xl shadow-xl p-8 mt-8">

      <h3 className="text-gray-400 text-lg">
        {title}
      </h3>

      <h1 className="text-5xl font-bold text-green-400 mt-3">
        {value}
      </h1>

    </div>
  );
}

export default ResultCard;