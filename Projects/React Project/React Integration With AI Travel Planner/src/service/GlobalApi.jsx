import axios from "axios"


export const geocodePlace = (text) =>
    axios.get("https://api.geoapify.com/v1/geocode/search", {
        params: {
            text,
            apiKey: import.meta.env.VITE_GEOAPIFY_API_KEY,
        },
    });


export const getPlaces = (lat, lon) =>
    axios.get("https://api.geoapify.com/v2/places", {
        params: {
            categories: "tourism.sights",
            filter: `circle:${lon},${lat},5000`,
            limit: 5,
            apiKey: import.meta.env.VITE_GEOAPIFY_API_KEY,
        },
    });

