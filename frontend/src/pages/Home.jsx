import Layout from "../components/Layout";
import StatsCard from "../components/StatsCard";
import StatusCard from "../components/StatusCard";
import QuickActionCard from "../components/QuickActionCard";
import PredictionChart from "../components/PredictionChart";

function Home() {
  return (
    <Layout>
      {/* Welcome Section */}

      <div className="mb-10">

        <h1 className="text-5xl font-bold text-white">
          Welcome Back 👋
        </h1>

        <p className="text-gray-400 mt-3 text-lg">
          Manage your AI powered travel platform from one dashboard.
        </p>

      </div>

      {/* Statistics */}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">

        <StatsCard
          title="ML Models"
          value="3"
          color="#38bdf8"
        />

        <StatsCard
          title="REST APIs"
          value="3"
          color="#22c55e"
        />

        <StatsCard
          title="Deployment"
          value="K8s"
          color="#f97316"
        />

      </div>

      {/* Status */}

      <div className="mb-10">

        <StatusCard />

      </div>

      {/* Quick Actions */}

      <h2 className="text-white text-3xl font-bold mb-6">
        Quick Actions
      </h2>

      <div className="grid md:grid-cols-3 gap-6">

        <QuickActionCard
          title="✈ Flight Prediction"
          path="/flight"
          color="bg-blue-600"
        />

        <QuickActionCard
          title="👤 Gender Prediction"
          path="/gender"
          color="bg-green-600"
        />

        <QuickActionCard
          title="🏨 Hotel Recommendation"
          path="/recommendation"
          color="bg-orange-600"
        />
        
        <PredictionChart />

      </div>

    </Layout>
  );
}

export default Home;