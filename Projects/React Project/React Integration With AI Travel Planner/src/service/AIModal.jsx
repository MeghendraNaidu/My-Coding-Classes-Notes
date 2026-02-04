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
