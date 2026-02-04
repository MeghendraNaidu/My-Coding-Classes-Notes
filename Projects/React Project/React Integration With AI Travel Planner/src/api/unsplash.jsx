import axios from "axios";

export const getPlaceImage = async (placeName) => {
  try {
    const res = await axios.get(
      "https://api.unsplash.com/search/photos",
      {
        params: {
          query: placeName,
          per_page: 1,
          client_id: import.meta.env.VITE_UNSPLASH_KEY,
        },
      }
    );

    return res.data.results?.[0]?.urls?.regular || null;
  } catch (err) {
    console.error("Unsplash error", err);
    return null;
  }
};
