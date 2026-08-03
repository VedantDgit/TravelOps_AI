import { useState } from "react";
import { toast } from "react-toastify";

import Layout from "../components/Layout";
import PageHeader from "../components/PageHeader";
import InputField from "../components/InputField";
import PrimaryButton from "../components/PrimaryButton";
import api from "../services/api";

function HotelRecommendation() {

  const [userCode, setUserCode] = useState("");
  const [loading, setLoading] = useState(false);
  const [hotels, setHotels] = useState([]);

  const getRecommendations = async () => {

    try {

      setLoading(true);

      const response = await api.post(
        "/recommend-hotels",
        {
          userCode: Number(userCode),
        }
      );

      console.log(response.data);

      setHotels(response.data.recommendations);

      toast.success("Recommendations generated successfully!");

    } catch (error) {

      console.error(error);

      toast.error("Recommendation Failed");

    } finally {

      setLoading(false);

    }

  };

  return (

    <Layout>

      <PageHeader
        title="Hotel Recommendation"
        subtitle="Discover personalized hotel recommendations using AI."
      />

      <div className="grid md:grid-cols-2 gap-6">

        <InputField
          label="User Code"
          name="userCode"
          type="number"
          value={userCode}
          onChange={(e) => setUserCode(e.target.value)}
          placeholder="Enter User Code"
        />

      </div>

      <div className="mt-8">

        <PrimaryButton
          loading={loading}
          onClick={getRecommendations}
        >
          Get Recommendations
        </PrimaryButton>

      </div>

      {hotels.length > 0 && (

        <div className="mt-10">

          <h2 className="text-2xl font-bold text-white mb-6">
            Recommended Hotels
          </h2>

          <div className="overflow-x-auto rounded-xl">

            <table className="w-full text-left bg-slate-800 rounded-xl">

              <thead className="bg-slate-700">

                <tr>

                  <th className="p-4">Hotel</th>

                  <th className="p-4">Place</th>

                  <th className="p-4">Price</th>

                  <th className="p-4">Days</th>

                  <th className="p-4">Flight Type</th>

                  <th className="p-4">Similarity</th>

                </tr>

              </thead>

              <tbody>

                {hotels.map((hotel, index) => (

                  <tr
                    key={index}
                    className="border-b border-slate-700 hover:bg-slate-700"
                  >

                    <td className="p-4">{hotel.hotelName}</td>

                    <td className="p-4">{hotel.place}</td>

                    <td className="p-4">₹ {hotel.hotelPrice}</td>

                    <td className="p-4">{hotel.days}</td>

                    <td className="p-4">{hotel.flightType}</td>

                    <td className="p-4">
                      {hotel.similarity_score}
                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

      )}

    </Layout>

  );

}

export default HotelRecommendation;