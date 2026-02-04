import axios from "axios"

// Google Details
// const BASE_URL = 'https://places.googleapis.com/v1/places:searchText'

//  const config = {
//     headers : {
//         "Content-Type" : "application/json",
//         "X-Geo-Api-Key" : import.meta.env.VITE_GEOAPIFY_API_KEY, 
//         "X-Geo-FieldMask" : [
//             'places.photos',
//             'places.displayName',
//             'places.id'
//         ]
//     }
//  }

//  export const GetPlaceDetails = (data) =>axios.post(BASE_URL, data, config)



// GeoApify Deails
// const BASE_URL = "https://api.geoapify.com/v2/places";

// const config = {
//   params: {
//     categories: "accommodation.hotel",
//     limit: 5,
//     apiKey: import.meta.env.VITE_GEOAPIFY_API_KEY
//   }
// };

// export const GetPlaceDetails = (data) =>
//   axios.get(BASE_URL, {
//     ...config,
//     params: {
//       ...config.params,
//       text: data // same role as your old request body
//     }
//   });


// Geoapify Optional One
// const BASE_URL = "https://api.geoapify.com/v2/places";

// const BASE_URL ="https://api.geoapify.com/v1/geocode/search"

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
            // text: data.textQuery,    
            categories: "tourism.sights",
            filter: `circle:${lon},${lat},5000`,
            limit: 5,
            // fields: "properties.name,properties.place_id,properties.datasource.raw.photos",
            apiKey: import.meta.env.VITE_GEOAPIFY_API_KEY,
        },
    });

