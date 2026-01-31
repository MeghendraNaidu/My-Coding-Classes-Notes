// const {
//   GoogleGenerativeAI,
//   HarmCategory,
//   HarmBlockThreshold,
// } = require("@google/generative-ai")

// const apiKey = import.meta.env.VITE_GOOGLE_GEMINI_AI_API_KEY
// const genAI = new GoogleGenerativeAI(apiKey)

// const model = genAI.getGenerativeModel({
//   model : "gemini-3-flash-preview";
// })

// const generationConfig = {
//   temperature : 1,
//   topP : 0.95,
//   topk : 64,
//   maxOutputTokens : 8192,
//   responseMimeType : "application/json",
// }

// export const chatSession = model.startChat({
//   generationConfig,
//   history : [
//     {
//       role : "user",
//       parts : [
//         {text : "Generate Travel Plan for Location: Las Vegas, for 3 Days for Couple with a Cheap budget, Give me a Hotels options list with HotelName, Hotel address, Price, hotel image url, geo coordinates, rating, descriptions and suggest itinerary with placeName, Place Details, Place Image Url, Geo Coordinates, ticket Pricing, rating, Time  travel each of the location for 3 days with each day plan with best time to visit in JSON format."},
//       ],
//     },
//     {
//       role : "model",
//       parts : [
//         {text : "```"}
//       ]
//     }
//   ]
// })




import { GoogleGenAI, } from '@google/genai';

// async function main() {
export const ai = new GoogleGenAI({
  apiKey: import.meta.env.VITE_GOOGLE_GEMINI_AI_API_KEY,
});

export const config = {
  thinkingConfig: {
    thinkingLevel: 'HIGH',
  },
};

// export const model = 'gemini-3-flash-preview';

// export const model = 'gemini-1.5-flash';

export const chat = ai.chats.create({
  model: "gemini-3-flash-preview",
  generationConfig: {
    temperature: 1,
    topP: 0.95,
    topk: 64,
    maxOutputTokens: 8192,
    responseMimeType: "application/json",
  },

});

// export const generationConfig = {
//   temperature: 1,
//   topP: 0.95,
//   topk: 64,
//   maxOutputTokens: 8192,
//   responseMimeType: "application/json",
// }

export const contents = [
  {
    role: 'user',
    parts: [
      {
        text: `Generate Travel Plan for Location: Las Vegas, for 3 Days for Couple with a Cheap budget, Give me a Hotels options list with HotelName, Hotel address, Price, hotel image url, geo coordinates, rating, descriptions and suggest itinerary with placeName, Place Details, Place Image Url, Geo Coordinates, ticket Pricing, rating, Time  travel each of the location for 3 days with each day plan with best time to visit in JSON format.`,
      },
    ],
  },
  {
    role: 'model',
    parts: [
      {
        text: `**Initiating Hotel Search**

        I'm currently focused on finding budget-friendly hotel options in Las Vegas specifically geared towards couples. I am gathering details like hotel names, addresses, price ranges, ratings, and descriptions to narrow down the search. I will also look for popular hotels.


        **Listing Vegas Hotels**

        I've got a promising start on finding affordable hotels in Las Vegas. Currently, the search has identified Circus Circus, Excalibur, and Luxor, with pricing between $58 and $59 per night. I'm noting each hotel's name, address (mostly), price, ratings, and descriptions to build a useful dataset.


        **Expanding Hotel Selection**

        I've added The STRAT, Flamingo, Silver Sevens, Main Street Station, Bposhtels, and El Cortez to the hotel list, with prices ranging from $40 to $73 per night. I'm also expanding the itinerary ideas to cover more potential options, for example, the Fremont Street Experience and a trip to Hoover Dam. Now, I'm focusing on locating precise geo-coordinates and image URLs for each location, along with exact ticket pricing, especially budget-friendly options, so I can provide precise budget guidance.


        **Gathering Initial Data**

        I have compiled a foundation of information. I've gathered hotel names, addresses, prices, ratings, and descriptions for several key budget-friendly hotels: Circus Circus, Excalibur, Luxor, The STRAT, and Flamingo. I can include more, such as Motel 6 or Silver Sevens, if needed.


        **Adding Image URLs**

        I've successfully linked representative image URLs for each hotel, enhancing the data set. Coordinates are ready for Circus Circus. I've compiled a potential itinerary, focusing on free activities and budget-conscious options, including a breakdown of day-by-day activities. My itinerary includes the Welcome to Fabulous Las Vegas Sign, Seven Magic Mountains, Bellagio Fountains, Linq Promenade, Eiffel Tower, Hoover Dam, Lake Mead, Red Rock Canyon, Fremont Street, Viva Vision, The Mob Museum, Container Park, and the Arts District, considering ticket pricing or free admission.


        **Finalizing Coordinates & Data**

        I've finished inputting the coordinates, completing a comprehensive location dataset. I am verifying those image URLs now. I also added "Visiting Duration" and "Best Time" to the data structure to improve clarity, and I'm adding cheap food option descriptions to the itinerary to match the theme. The plan is to create the final data structure, and then to synthesize the data into JSON. I will be refining hotel descriptions to ensure they are couple-oriented and budget-focused. I am also checking ticket information.


        **Verifying Ratings and Data**

        I've double-checked the ratings for both hotels and itinerary locations, pulling values from sources like Travelocity and Google/Tripadvisor, to provide the most realistic rating data. I'm verifying the image URLs now, planning to use direct links from reliable sources to avoid any issues. I'm preparing for the final structure; all the data is accurate.


        `,
      },
      {
        text: `\`\`\`json
        {
          "TravelPlan": {
            "Location": "Las Vegas, Nevada",
            "Duration": "3 Days",
            "BudgetCategory": "Cheap/Budget-Friendly",
            "TravelerType": "Couple",
            "HotelOptions": [
              {
                "HotelName": "Excalibur Hotel & Casino",
                "HotelAddress": "3850 S Las Vegas Blvd, Las Vegas, NV 89109",
                "Price": "$58 - $85 per night",
                "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Excalibur_Hotel_and_Casino_2010.jpg",
                "GeoCoordinates": {
                  "Latitude": 36.0989,
                  "Longitude": -115.1756
                },
                "Rating": 3.5,
                "Description": "A medieval-themed resort offering some of the best value on the South Strip. Ideal for couples who want a resort feel without the high price tag. Features a large pool area and multiple budget dining options."
              },
              {
                "HotelName": "Luxor Hotel and Casino",
                "HotelAddress": "3900 S Las Vegas Blvd, Las Vegas, NV 89119",
                "Price": "$59 - $90 per night",
                "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Luxor_Hotel_Las_Vegas.jpg",
                "GeoCoordinates": {
                  "Latitude": 36.0956,
                  "Longitude": -115.1758
                },
                "Rating": 3.6,
                "Description": "Iconic pyramid-shaped hotel with an Ancient Egyptian theme. It offers unique architecture and a great location near the South Strip. Very budget-friendly for couples seeking a memorable stay."
              },
              {
                "HotelName": "The STRAT Hotel, Casino & Tower",
                "HotelAddress": "2000 S Las Vegas Blvd, Las Vegas, NV 89104",
                "Price": "$63 - $95 per night",
                "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/1/15/The_Strat_tower_and_resort_2017.jpg",
                "GeoCoordinates": {
                  "Latitude": 36.1475,
                  "Longitude": -115.1554
                },
                "Rating": 3.8,
                "Description": "Located at the north end of the Strip, this hotel features the tallest observation tower in the US. It's a great pick for couples who enjoy heights and want modern, affordable rooms."
              },
              {
                "HotelName": "Flamingo Las Vegas Hotel & Casino",
                "HotelAddress": "3555 S Las Vegas Blvd, Las Vegas, NV 89109",
                "Price": "$68 - $110 per night",
                "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Flamingo_Las_Vegas_2017.jpg",
                "GeoCoordinates": {
                  "Latitude": 36.1161,
                  "Longitude": -115.1706
                },
                "Rating": 3.7,
                "Description": "The oldest operating resort on the Strip, offering a classic Vegas vibe with a center-strip location. The wildlife habitat is free to visit and perfect for couples."
              },
              {
                "HotelName": "Circus Circus Hotel & Casino",
                "HotelAddress": "2880 S Las Vegas Blvd, Las Vegas, NV 89109",
                "Price": "$52 - $75 per night",
                "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Circus_Circus_Las_Vegas_2011.jpg",
                "GeoCoordinates": {
                  "Latitude": 36.1367,
                  "Longitude": -115.1629
                },
                "Rating": 3.0,
                "Description": "Often the cheapest option on the Strip, featuring free circus acts throughout the day. While older, it is unbeatable for pure budget savings."
              }
            ],
            "Itinerary": [
              {
                "Day": 1,
                "DayPlan": "South Strip & Iconic Landmarks",
                "BestTimeToVisit": "Morning to Night",
                "Schedule": [
                  {
                    "placeName": "Welcome to Fabulous Las Vegas Sign",
                    "PlaceDetails": "The iconic neon sign marking the start of the Strip. Arrive early to beat the photo lines.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Welcome_to_Fabulous_Las_Vegas.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.0820,
                      "Longitude": -115.1728
                    },
                    "ticketPricing": "Free",
                    "rating": 4.6,
                    "TimeSpent": "30 minutes"
                  },
                  {
                    "placeName": "Seven Magic Mountains",
                    "PlaceDetails": "A colorful public art installation in the desert featuring seven towers of stacked boulders.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Seven_Magic_Mountains%2C_Las_Vegas.jpg",
                    "GeoCoordinates": {
                      "Latitude": 35.8400,
                      "Longitude": -115.2711
                    },
                    "ticketPricing": "Free",
                    "rating": 4.3,
                    "TimeSpent": "1 hour"
                  },
                  {
                    "placeName": "Bellagio Fountains & Conservatory",
                    "PlaceDetails": "Choreographed water show set to music and a stunning indoor botanical garden with seasonal displays.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Bellagio_Fountains_Las_Vegas.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1125,
                      "Longitude": -115.1741
                    },
                    "ticketPricing": "Free",
                    "rating": 4.8,
                    "TimeSpent": "1.5 hours"
                  },
                  {
                    "placeName": "The Linq Promenade",
                    "PlaceDetails": "An open-air shopping and dining district. Great for a romantic evening walk. Optional ride on the High Roller.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/32/Linq_Promenade_Las_Vegas.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1176,
                      "Longitude": -115.1684
                    },
                    "ticketPricing": "Free to walk (High Roller ~$35)",
                    "rating": 4.5,
                    "TimeSpent": "2 hours"
                  }
                ]
              },
              {
                "Day": 2,
                "DayPlan": "Adventure & Engineering Marvels",
                "BestTimeToVisit": "Morning",
                "Schedule": [
                  {
                    "placeName": "Hoover Dam (Mike O'Callaghan-Pat Tillman Memorial Bridge)",
                    "PlaceDetails": "Walk across the bypass bridge for the best aerial views of the Hoover Dam and Lake Mead.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/af/Hoover_Dam_from_bridge.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.0160,
                      "Longitude": -114.7378
                    },
                    "ticketPricing": "Free (Parking ~$10)",
                    "rating": 4.7,
                    "TimeSpent": "2 hours"
                  },
                  {
                    "placeName": "Red Rock Canyon National Conservation Area",
                    "PlaceDetails": "A scenic 13-mile loop drive through stunning red sandstone formations. Perfect for hiking or a romantic sunset drive.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Red_Rock_Canyon_Las_Vegas.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1356,
                      "Longitude": -115.4272
                    },
                    "ticketPricing": "$20 per vehicle",
                    "rating": 4.8,
                    "TimeSpent": "3-4 hours"
                  },
                  {
                    "placeName": "Eiffel Tower Viewing Deck (Paris Las Vegas)",
                    "PlaceDetails": "Experience a half-scale replica of the Eiffel Tower with panoramic views of the Strip and Bellagio Fountains.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Paris_Las_Vegas_Eiffel_Tower.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1124,
                      "Longitude": -115.1705
                    },
                    "ticketPricing": "~$25 per person",
                    "rating": 4.4,
                    "TimeSpent": "1 hour"
                  }
                ]
              },
              {
                "Day": 3,
                "DayPlan": "Downtown & Old Vegas Culture",
                "BestTimeToVisit": "Afternoon to Late Night",
                "Schedule": [
                  {
                    "placeName": "Fremont Street Experience",
                    "PlaceDetails": "The historic heart of Vegas. Famous for the Viva Vision LED canopy and free nightly concerts.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/0/09/Fremont_Street_Experience_2015.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1707,
                      "Longitude": -115.1439
                    },
                    "ticketPricing": "Free",
                    "rating": 4.5,
                    "TimeSpent": "3 hours"
                  },
                  {
                    "placeName": "Container Park",
                    "PlaceDetails": "An open-air shopping center made from shipping containers. Features a giant fire-breathing mantis and local food.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Downtown_Container_Park.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1680,
                      "Longitude": -115.1378
                    },
                    "ticketPricing": "Free",
                    "rating": 4.5,
                    "TimeSpent": "1.5 hours"
                  },
                  {
                    "placeName": "Las Vegas Arts District (18b)",
                    "PlaceDetails": "A cool neighborhood with galleries, vintage shops, and local breweries. Very walkable and romantic for an evening stroll.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Las_Vegas_Arts_District.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1555,
                      "Longitude": -115.1531
                    },
                    "ticketPricing": "Free",
                    "rating": 4.3,
                    "TimeSpent": "2 hours"
                  },
                  {
                    "placeName": "Viva Vision Light Show",
                    "PlaceDetails": "A spectacular light show on the world's largest LED screen, spanning the Fremont Street pedestrian mall.",
                    "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Viva_Vision_Light_Show.jpg",
                    "GeoCoordinates": {
                      "Latitude": 36.1707,
                      "Longitude": -115.1439
                    },
                    "ticketPricing": "Free",
                    "rating": 4.7,
                    "TimeSpent": "30 minutes"
                  }
                ]
              }
            ]
          }
        }
        \`\`\``,
      },
    ],
  },
  {
    role: 'user',
    parts: [
      {
        text: `INSERT_INPUT_HERE`,
      },
    ],
  },
];

// const response = await ai.models.generateContent({
//   model,
//   config,
//   generationConfig,
//   contents,
// });

// console.log(response.text);

// main();








// import OpenAI from "openai";

// export const client = new OpenAI({
//   apiKey: import.meta.env.VITE_OPENAI_API_KEY,
// });

// export const model = "gpt-5-nano";

// export const generationConfig = {
//   temperature: 1,
//   top_p: 0.95,
//   max_output_tokens: 8192,
//   response_format: { type: "json_object" },
// };

// export const contents = [
//   {
//     role: 'user',
//     parts: [
//       {
//         content: `Generate Travel Plan for Location: Las Vegas, for 3 Days for Couple with a Cheap budget, Give me a Hotels options list with HotelName, Hotel address, Price, hotel image url, geo coordinates, rating, descriptions and suggest itinerary with placeName, Place Details, Place Image Url, Geo Coordinates, ticket Pricing, rating, Time  travel each of the location for 3 days with each day plan with best time to visit in JSON format.`,
//       },
//     ],
//   },
//   {
//     role: "assistant",
//     parts: [
//       {
//         content: `**Initiating Hotel Search**

// I'm currently focused on finding budget-friendly hotel options in Las Vegas specifically geared towards couples. I am gathering details like hotel names, addresses, price ranges, ratings, and descriptions to narrow down the search. I will also look for popular hotels.


// **Listing Vegas Hotels**

// I've got a promising start on finding affordable hotels in Las Vegas. Currently, the search has identified Circus Circus, Excalibur, and Luxor, with pricing between $58 and $59 per night. I'm noting each hotel's name, address (mostly), price, ratings, and descriptions to build a useful dataset.


// **Expanding Hotel Selection**

// I've added The STRAT, Flamingo, Silver Sevens, Main Street Station, Bposhtels, and El Cortez to the hotel list, with prices ranging from $40 to $73 per night. I'm also expanding the itinerary ideas to cover more potential options, for example, the Fremont Street Experience and a trip to Hoover Dam. Now, I'm focusing on locating precise geo-coordinates and image URLs for each location, along with exact ticket pricing, especially budget-friendly options, so I can provide precise budget guidance.


// **Gathering Initial Data**

// I have compiled a foundation of information. I've gathered hotel names, addresses, prices, ratings, and descriptions for several key budget-friendly hotels: Circus Circus, Excalibur, Luxor, The STRAT, and Flamingo. I can include more, such as Motel 6 or Silver Sevens, if needed.


// **Adding Image URLs**

// I've successfully linked representative image URLs for each hotel, enhancing the data set. Coordinates are ready for Circus Circus. I've compiled a potential itinerary, focusing on free activities and budget-conscious options, including a breakdown of day-by-day activities. My itinerary includes the Welcome to Fabulous Las Vegas Sign, Seven Magic Mountains, Bellagio Fountains, Linq Promenade, Eiffel Tower, Hoover Dam, Lake Mead, Red Rock Canyon, Fremont Street, Viva Vision, The Mob Museum, Container Park, and the Arts District, considering ticket pricing or free admission.


// **Finalizing Coordinates & Data**

// I've finished inputting the coordinates, completing a comprehensive location dataset. I am verifying those image URLs now. I also added "Visiting Duration" and "Best Time" to the data structure to improve clarity, and I'm adding cheap food option descriptions to the itinerary to match the theme. The plan is to create the final data structure, and then to synthesize the data into JSON. I will be refining hotel descriptions to ensure they are couple-oriented and budget-focused. I am also checking ticket information.


// **Verifying Ratings and Data**

// I've double-checked the ratings for both hotels and itinerary locations, pulling values from sources like Travelocity and Google/Tripadvisor, to provide the most realistic rating data. I'm verifying the image URLs now, planning to use direct links from reliable sources to avoid any issues. I'm preparing for the final structure; all the data is accurate.


// `,
//       },
//       {
//         content: `\`\`\`json
// {
//   "TravelPlan": {
//     "Location": "Las Vegas, Nevada",
//     "Duration": "3 Days",
//     "BudgetCategory": "Cheap/Budget-Friendly",
//     "TravelerType": "Couple",
//     "HotelOptions": [
//       {
//         "HotelName": "Excalibur Hotel & Casino",
//         "HotelAddress": "3850 S Las Vegas Blvd, Las Vegas, NV 89109",
//         "Price": "$58 - $85 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Excalibur_Hotel_and_Casino_2010.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.0989,
//           "Longitude": -115.1756
//         },
//         "Rating": 3.5,
//         "Description": "A medieval-themed resort offering some of the best value on the South Strip. Ideal for couples who want a resort feel without the high price tag. Features a large pool area and multiple budget dining options."
//       },
//       {
//         "HotelName": "Luxor Hotel and Casino",
//         "HotelAddress": "3900 S Las Vegas Blvd, Las Vegas, NV 89119",
//         "Price": "$59 - $90 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Luxor_Hotel_Las_Vegas.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.0956,
//           "Longitude": -115.1758
//         },
//         "Rating": 3.6,
//         "Description": "Iconic pyramid-shaped hotel with an Ancient Egyptian theme. It offers unique architecture and a great location near the South Strip. Very budget-friendly for couples seeking a memorable stay."
//       },
//       {
//         "HotelName": "The STRAT Hotel, Casino & Tower",
//         "HotelAddress": "2000 S Las Vegas Blvd, Las Vegas, NV 89104",
//         "Price": "$63 - $95 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/1/15/The_Strat_tower_and_resort_2017.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.1475,
//           "Longitude": -115.1554
//         },
//         "Rating": 3.8,
//         "Description": "Located at the north end of the Strip, this hotel features the tallest observation tower in the US. It's a great pick for couples who enjoy heights and want modern, affordable rooms."
//       },
//       {
//         "HotelName": "Flamingo Las Vegas Hotel & Casino",
//         "HotelAddress": "3555 S Las Vegas Blvd, Las Vegas, NV 89109",
//         "Price": "$68 - $110 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Flamingo_Las_Vegas_2017.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.1161,
//           "Longitude": -115.1706
//         },
//         "Rating": 3.7,
//         "Description": "The oldest operating resort on the Strip, offering a classic Vegas vibe with a center-strip location. The wildlife habitat is free to visit and perfect for couples."
//       },
//       {
//         "HotelName": "Circus Circus Hotel & Casino",
//         "HotelAddress": "2880 S Las Vegas Blvd, Las Vegas, NV 89109",
//         "Price": "$52 - $75 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Circus_Circus_Las_Vegas_2011.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.1367,
//           "Longitude": -115.1629
//         },
//         "Rating": 3.0,
//         "Description": "Often the cheapest option on the Strip, featuring free circus acts throughout the day. While older, it is unbeatable for pure budget savings."
//       }
//     ],
//     "Itinerary": [
//       {
//         "Day": 1,
//         "DayPlan": "South Strip & Iconic Landmarks",
//         "BestTimeToVisit": "Morning to Night",
//         "Schedule": [
//           {
//             "placeName": "Welcome to Fabulous Las Vegas Sign",
//             "PlaceDetails": "The iconic neon sign marking the start of the Strip. Arrive early to beat the photo lines.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Welcome_to_Fabulous_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.0820,
//               "Longitude": -115.1728
//             },
//             "ticketPricing": "Free",
//             "rating": 4.6,
//             "TimeSpent": "30 minutes"
//           },
//           {
//             "placeName": "Seven Magic Mountains",
//             "PlaceDetails": "A colorful public art installation in the desert featuring seven towers of stacked boulders.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Seven_Magic_Mountains%2C_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 35.8400,
//               "Longitude": -115.2711
//             },
//             "ticketPricing": "Free",
//             "rating": 4.3,
//             "TimeSpent": "1 hour"
//           },
//           {
//             "placeName": "Bellagio Fountains & Conservatory",
//             "PlaceDetails": "Choreographed water show set to music and a stunning indoor botanical garden with seasonal displays.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Bellagio_Fountains_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1125,
//               "Longitude": -115.1741
//             },
//             "ticketPricing": "Free",
//             "rating": 4.8,
//             "TimeSpent": "1.5 hours"
//           },
//           {
//             "placeName": "The Linq Promenade",
//             "PlaceDetails": "An open-air shopping and dining district. Great for a romantic evening walk. Optional ride on the High Roller.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/32/Linq_Promenade_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1176,
//               "Longitude": -115.1684
//             },
//             "ticketPricing": "Free to walk (High Roller ~$35)",
//             "rating": 4.5,
//             "TimeSpent": "2 hours"
//           }
//         ]
//       },
//       {
//         "Day": 2,
//         "DayPlan": "Adventure & Engineering Marvels",
//         "BestTimeToVisit": "Morning",
//         "Schedule": [
//           {
//             "placeName": "Hoover Dam (Mike O'Callaghan-Pat Tillman Memorial Bridge)",
//             "PlaceDetails": "Walk across the bypass bridge for the best aerial views of the Hoover Dam and Lake Mead.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/af/Hoover_Dam_from_bridge.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.0160,
//               "Longitude": -114.7378
//             },
//             "ticketPricing": "Free (Parking ~$10)",
//             "rating": 4.7,
//             "TimeSpent": "2 hours"
//           },
//           {
//             "placeName": "Red Rock Canyon National Conservation Area",
//             "PlaceDetails": "A scenic 13-mile loop drive through stunning red sandstone formations. Perfect for hiking or a romantic sunset drive.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Red_Rock_Canyon_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1356,
//               "Longitude": -115.4272
//             },
//             "ticketPricing": "$20 per vehicle",
//             "rating": 4.8,
//             "TimeSpent": "3-4 hours"
//           },
//           {
//             "placeName": "Eiffel Tower Viewing Deck (Paris Las Vegas)",
//             "PlaceDetails": "Experience a half-scale replica of the Eiffel Tower with panoramic views of the Strip and Bellagio Fountains.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Paris_Las_Vegas_Eiffel_Tower.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1124,
//               "Longitude": -115.1705
//             },
//             "ticketPricing": "~$25 per person",
//             "rating": 4.4,
//             "TimeSpent": "1 hour"
//           }
//         ]
//       },
//       {
//         "Day": 3,
//         "DayPlan": "Downtown & Old Vegas Culture",
//         "BestTimeToVisit": "Afternoon to Late Night",
//         "Schedule": [
//           {
//             "placeName": "Fremont Street Experience",
//             "PlaceDetails": "The historic heart of Vegas. Famous for the Viva Vision LED canopy and free nightly concerts.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/0/09/Fremont_Street_Experience_2015.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1707,
//               "Longitude": -115.1439
//             },
//             "ticketPricing": "Free",
//             "rating": 4.5,
//             "TimeSpent": "3 hours"
//           },
//           {
//             "placeName": "Container Park",
//             "PlaceDetails": "An open-air shopping center made from shipping containers. Features a giant fire-breathing mantis and local food.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Downtown_Container_Park.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1680,
//               "Longitude": -115.1378
//             },
//             "ticketPricing": "Free",
//             "rating": 4.5,
//             "TimeSpent": "1.5 hours"
//           },
//           {
//             "placeName": "Las Vegas Arts District (18b)",
//             "PlaceDetails": "A cool neighborhood with galleries, vintage shops, and local breweries. Very walkable and romantic for an evening stroll.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Las_Vegas_Arts_District.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1555,
//               "Longitude": -115.1531
//             },
//             "ticketPricing": "Free",
//             "rating": 4.3,
//             "TimeSpent": "2 hours"
//           },
//           {
//             "placeName": "Viva Vision Light Show",
//             "PlaceDetails": "A spectacular light show on the world's largest LED screen, spanning the Fremont Street pedestrian mall.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Viva_Vision_Light_Show.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1707,
//               "Longitude": -115.1439
//             },
//             "ticketPricing": "Free",
//             "rating": 4.7,
//             "TimeSpent": "30 minutes"
//           }
//         ]
//       }
//     ]
//   }
// }
// \`\`\``,
//       },
//     ],
//   },
//   {
//     role: "user",
//     content: "INSERT_INPUT_HERE",
//   },
// ];




// ai21Frontend.ts
// import { AI21 } from "ai21";

// const apiKey = import.meta.env.VITE_AI21_API_KEY;
// if (!apiKey) {
//   throw new Error("AI21_API_KEY is not set. Please export it as an environment variable.");
// }

// export const ai = new AI21({
//   apiKey,
// });

// export const model = "j2-jumbo"; // or any HF-style AI21 model

// export const generationConfig = {
//   temperature: 1,
//   topP: 0.95,
//   maxOutputTokens: 8192,
//   responseMimeType: "application/json",
// };

// export const contents = [
//   {
//     role: 'user',
//     parts: [
//       {
//         text: `Generate Travel Plan for Location: Las Vegas, for 3 Days for Couple with a Cheap budget, Give me a Hotels options list with HotelName, Hotel address, Price, hotel image url, geo coordinates, rating, descriptions and suggest itinerary with placeName, Place Details, Place Image Url, Geo Coordinates, ticket Pricing, rating, Time  travel each of the location for 3 days with each day plan with best time to visit in JSON format.`,
//       },
//     ],
//   },
//   {
//     role: 'model',
//     parts: [
//       {
//         text: `**Initiating Hotel Search**

// I'm currently focused on finding budget-friendly hotel options in Las Vegas specifically geared towards couples. I am gathering details like hotel names, addresses, price ranges, ratings, and descriptions to narrow down the search. I will also look for popular hotels.


// **Listing Vegas Hotels**

// I've got a promising start on finding affordable hotels in Las Vegas. Currently, the search has identified Circus Circus, Excalibur, and Luxor, with pricing between $58 and $59 per night. I'm noting each hotel's name, address (mostly), price, ratings, and descriptions to build a useful dataset.


// **Expanding Hotel Selection**

// I've added The STRAT, Flamingo, Silver Sevens, Main Street Station, Bposhtels, and El Cortez to the hotel list, with prices ranging from $40 to $73 per night. I'm also expanding the itinerary ideas to cover more potential options, for example, the Fremont Street Experience and a trip to Hoover Dam. Now, I'm focusing on locating precise geo-coordinates and image URLs for each location, along with exact ticket pricing, especially budget-friendly options, so I can provide precise budget guidance.


// **Gathering Initial Data**

// I have compiled a foundation of information. I've gathered hotel names, addresses, prices, ratings, and descriptions for several key budget-friendly hotels: Circus Circus, Excalibur, Luxor, The STRAT, and Flamingo. I can include more, such as Motel 6 or Silver Sevens, if needed.


// **Adding Image URLs**

// I've successfully linked representative image URLs for each hotel, enhancing the data set. Coordinates are ready for Circus Circus. I've compiled a potential itinerary, focusing on free activities and budget-conscious options, including a breakdown of day-by-day activities. My itinerary includes the Welcome to Fabulous Las Vegas Sign, Seven Magic Mountains, Bellagio Fountains, Linq Promenade, Eiffel Tower, Hoover Dam, Lake Mead, Red Rock Canyon, Fremont Street, Viva Vision, The Mob Museum, Container Park, and the Arts District, considering ticket pricing or free admission.


// **Finalizing Coordinates & Data**

// I've finished inputting the coordinates, completing a comprehensive location dataset. I am verifying those image URLs now. I also added "Visiting Duration" and "Best Time" to the data structure to improve clarity, and I'm adding cheap food option descriptions to the itinerary to match the theme. The plan is to create the final data structure, and then to synthesize the data into JSON. I will be refining hotel descriptions to ensure they are couple-oriented and budget-focused. I am also checking ticket information.


// **Verifying Ratings and Data**

// I've double-checked the ratings for both hotels and itinerary locations, pulling values from sources like Travelocity and Google/Tripadvisor, to provide the most realistic rating data. I'm verifying the image URLs now, planning to use direct links from reliable sources to avoid any issues. I'm preparing for the final structure; all the data is accurate.


// `,
//       },
//       {
//         text: `\`\`\`json
// {
//   "TravelPlan": {
//     "Location": "Las Vegas, Nevada",
//     "Duration": "3 Days",
//     "BudgetCategory": "Cheap/Budget-Friendly",
//     "TravelerType": "Couple",
//     "HotelOptions": [
//       {
//         "HotelName": "Excalibur Hotel & Casino",
//         "HotelAddress": "3850 S Las Vegas Blvd, Las Vegas, NV 89109",
//         "Price": "$58 - $85 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Excalibur_Hotel_and_Casino_2010.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.0989,
//           "Longitude": -115.1756
//         },
//         "Rating": 3.5,
//         "Description": "A medieval-themed resort offering some of the best value on the South Strip. Ideal for couples who want a resort feel without the high price tag. Features a large pool area and multiple budget dining options."
//       },
//       {
//         "HotelName": "Luxor Hotel and Casino",
//         "HotelAddress": "3900 S Las Vegas Blvd, Las Vegas, NV 89119",
//         "Price": "$59 - $90 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Luxor_Hotel_Las_Vegas.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.0956,
//           "Longitude": -115.1758
//         },
//         "Rating": 3.6,
//         "Description": "Iconic pyramid-shaped hotel with an Ancient Egyptian theme. It offers unique architecture and a great location near the South Strip. Very budget-friendly for couples seeking a memorable stay."
//       },
//       {
//         "HotelName": "The STRAT Hotel, Casino & Tower",
//         "HotelAddress": "2000 S Las Vegas Blvd, Las Vegas, NV 89104",
//         "Price": "$63 - $95 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/1/15/The_Strat_tower_and_resort_2017.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.1475,
//           "Longitude": -115.1554
//         },
//         "Rating": 3.8,
//         "Description": "Located at the north end of the Strip, this hotel features the tallest observation tower in the US. It's a great pick for couples who enjoy heights and want modern, affordable rooms."
//       },
//       {
//         "HotelName": "Flamingo Las Vegas Hotel & Casino",
//         "HotelAddress": "3555 S Las Vegas Blvd, Las Vegas, NV 89109",
//         "Price": "$68 - $110 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Flamingo_Las_Vegas_2017.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.1161,
//           "Longitude": -115.1706
//         },
//         "Rating": 3.7,
//         "Description": "The oldest operating resort on the Strip, offering a classic Vegas vibe with a center-strip location. The wildlife habitat is free to visit and perfect for couples."
//       },
//       {
//         "HotelName": "Circus Circus Hotel & Casino",
//         "HotelAddress": "2880 S Las Vegas Blvd, Las Vegas, NV 89109",
//         "Price": "$52 - $75 per night",
//         "HotelImageUrl": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Circus_Circus_Las_Vegas_2011.jpg",
//         "GeoCoordinates": {
//           "Latitude": 36.1367,
//           "Longitude": -115.1629
//         },
//         "Rating": 3.0,
//         "Description": "Often the cheapest option on the Strip, featuring free circus acts throughout the day. While older, it is unbeatable for pure budget savings."
//       }
//     ],
//     "Itinerary": [
//       {
//         "Day": 1,
//         "DayPlan": "South Strip & Iconic Landmarks",
//         "BestTimeToVisit": "Morning to Night",
//         "Schedule": [
//           {
//             "placeName": "Welcome to Fabulous Las Vegas Sign",
//             "PlaceDetails": "The iconic neon sign marking the start of the Strip. Arrive early to beat the photo lines.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Welcome_to_Fabulous_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.0820,
//               "Longitude": -115.1728
//             },
//             "ticketPricing": "Free",
//             "rating": 4.6,
//             "TimeSpent": "30 minutes"
//           },
//           {
//             "placeName": "Seven Magic Mountains",
//             "PlaceDetails": "A colorful public art installation in the desert featuring seven towers of stacked boulders.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Seven_Magic_Mountains%2C_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 35.8400,
//               "Longitude": -115.2711
//             },
//             "ticketPricing": "Free",
//             "rating": 4.3,
//             "TimeSpent": "1 hour"
//           },
//           {
//             "placeName": "Bellagio Fountains & Conservatory",
//             "PlaceDetails": "Choreographed water show set to music and a stunning indoor botanical garden with seasonal displays.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Bellagio_Fountains_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1125,
//               "Longitude": -115.1741
//             },
//             "ticketPricing": "Free",
//             "rating": 4.8,
//             "TimeSpent": "1.5 hours"
//           },
//           {
//             "placeName": "The Linq Promenade",
//             "PlaceDetails": "An open-air shopping and dining district. Great for a romantic evening walk. Optional ride on the High Roller.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/32/Linq_Promenade_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1176,
//               "Longitude": -115.1684
//             },
//             "ticketPricing": "Free to walk (High Roller ~$35)",
//             "rating": 4.5,
//             "TimeSpent": "2 hours"
//           }
//         ]
//       },
//       {
//         "Day": 2,
//         "DayPlan": "Adventure & Engineering Marvels",
//         "BestTimeToVisit": "Morning",
//         "Schedule": [
//           {
//             "placeName": "Hoover Dam (Mike O'Callaghan-Pat Tillman Memorial Bridge)",
//             "PlaceDetails": "Walk across the bypass bridge for the best aerial views of the Hoover Dam and Lake Mead.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/af/Hoover_Dam_from_bridge.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.0160,
//               "Longitude": -114.7378
//             },
//             "ticketPricing": "Free (Parking ~$10)",
//             "rating": 4.7,
//             "TimeSpent": "2 hours"
//           },
//           {
//             "placeName": "Red Rock Canyon National Conservation Area",
//             "PlaceDetails": "A scenic 13-mile loop drive through stunning red sandstone formations. Perfect for hiking or a romantic sunset drive.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Red_Rock_Canyon_Las_Vegas.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1356,
//               "Longitude": -115.4272
//             },
//             "ticketPricing": "$20 per vehicle",
//             "rating": 4.8,
//             "TimeSpent": "3-4 hours"
//           },
//           {
//             "placeName": "Eiffel Tower Viewing Deck (Paris Las Vegas)",
//             "PlaceDetails": "Experience a half-scale replica of the Eiffel Tower with panoramic views of the Strip and Bellagio Fountains.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Paris_Las_Vegas_Eiffel_Tower.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1124,
//               "Longitude": -115.1705
//             },
//             "ticketPricing": "~$25 per person",
//             "rating": 4.4,
//             "TimeSpent": "1 hour"
//           }
//         ]
//       },
//       {
//         "Day": 3,
//         "DayPlan": "Downtown & Old Vegas Culture",
//         "BestTimeToVisit": "Afternoon to Late Night",
//         "Schedule": [
//           {
//             "placeName": "Fremont Street Experience",
//             "PlaceDetails": "The historic heart of Vegas. Famous for the Viva Vision LED canopy and free nightly concerts.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/0/09/Fremont_Street_Experience_2015.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1707,
//               "Longitude": -115.1439
//             },
//             "ticketPricing": "Free",
//             "rating": 4.5,
//             "TimeSpent": "3 hours"
//           },
//           {
//             "placeName": "Container Park",
//             "PlaceDetails": "An open-air shopping center made from shipping containers. Features a giant fire-breathing mantis and local food.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Downtown_Container_Park.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1680,
//               "Longitude": -115.1378
//             },
//             "ticketPricing": "Free",
//             "rating": 4.5,
//             "TimeSpent": "1.5 hours"
//           },
//           {
//             "placeName": "Las Vegas Arts District (18b)",
//             "PlaceDetails": "A cool neighborhood with galleries, vintage shops, and local breweries. Very walkable and romantic for an evening stroll.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Las_Vegas_Arts_District.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1555,
//               "Longitude": -115.1531
//             },
//             "ticketPricing": "Free",
//             "rating": 4.3,
//             "TimeSpent": "2 hours"
//           },
//           {
//             "placeName": "Viva Vision Light Show",
//             "PlaceDetails": "A spectacular light show on the world's largest LED screen, spanning the Fremont Street pedestrian mall.",
//             "PlaceImageUrl": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Viva_Vision_Light_Show.jpg",
//             "GeoCoordinates": {
//               "Latitude": 36.1707,
//               "Longitude": -115.1439
//             },
//             "ticketPricing": "Free",
//             "rating": 4.7,
//             "TimeSpent": "30 minutes"
//           }
//         ]
//       }
//     ]
//   }
// }
// \`\`\``,
//       },
//     ],
//   },
//   {
//     role: 'user',
//     parts: [
//       {
//         text: `INSERT_INPUT_HERE`,
//       },
//     ],
//   },
// ];

// export async function runAI21() {
//   const body = {
//     input: contents.map(c => ({
//       role: c.role,
//       content: c.parts.map(p => p.text).join("\n"),
//     })),
//     requirements: [
//       {
//         name: "factual_accuracy",
//         description: "Base insights on verifiable data from reliable sources.",
//       },
//       {
//         name: "clarity",
//         description: "Keep explanations concise and free of jargon.",
//       },
//       {
//         name: "tone",
//         description: "Neutral, professional tone suitable for general audience.",
//       },
//     ],
//   };

//   const result = await ai.beta.maestro.runs.createAndPoll(body, {
//     interval: 1000,
//     timeout: 100000,
//   });

//   return result;
// }
