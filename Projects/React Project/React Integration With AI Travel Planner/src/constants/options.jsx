export const SelectTravelesList = [
    {
        id : 1,
        title : "Just Me",
        desc : "A sole traveles in explorations",
        icon : "✈️",
        people : "1"
    },
    {
        id : 2,
        title : "A Couple",
        desc : "Two traveles in tandem",
        icon : "🥂",
        people : "2 People"
    },
    {
        id : 3,
        title : "Family",
        desc : "A group of fun loving adv",
        icon : "🏡",
        people : "3 to 5 People"
    },
    {
        id : 4,
        title : "Friends",
        desc : "A bunch of thrill-seekes",
        icon : "🐦‍🔥",
        people : "5 to 10 People"
    },
]

export const SelectBudgetOptions = [
    {
        id : 1,
        title : "Cheap",
        desc : "Stay conscious of costs",
        icon : "💴" 
    },
    {
        id : 2,
        title : "Moderate",
        desc : "Keep code on the average side",
        icon : "💰"
    },
    {
        id : 3,
        title : "Luxury",
        desc : "Dont worry about cost",
        icon : "💸"
    },
]


// export const AI_PROMPT = "Generate Travel Plan for Location: {location}, for {totalDays} Days for {traveler} with a {budget} budget, Give me a Hotels options list with HotelName, Hotel address, Price, hotel image url, geo coordinates, rating, descriptions and suggest itinerary with placeName, Place Details, Place Image Url, Geo Coordinates, ticket Pricing, rating, Time  travel each of the location for 3 days with each day plan with best time to visit in JSON format."

export const AI_PROMPT = `
You are a travel API. 
Return ONLY valid JSON. No markdown. No explanation. No extra keys.

Follow this schema EXACTLY:

{
  "TravelPlan": {
    "Location": "string",
    "Duration": "string",
    "BudgetCategory": "string",
    "TravelerType": "string",
    "HotelOptions": [
      {
        "HotelName": "string",
        "HotelAddress": "string",
        "Price": "string",
        "HotelImageUrl": "string",
        "GeoCoordinates": { "Latitude": number, "Longitude": number },
        "Rating": number,
        "Description": "string"
      },
      {
        "HotelName": "string",
        "HotelAddress": "string",
        "Price": "string",
        "HotelImageUrl": "string",
        "GeoCoordinates": { "Latitude": number, "Longitude": number },
        "Rating": number,
        "Description": "string"
      },
      {
        "HotelName": "string",
        "HotelAddress": "string",
        "Price": "string",
        "HotelImageUrl": "string",
        "GeoCoordinates": { "Latitude": number, "Longitude": number },
        "Rating": number,
        "Description": "string"
      },
      {
        "HotelName": "string",
        "HotelAddress": "string",
        "Price": "string",
        "HotelImageUrl": "string",
        "GeoCoordinates": { "Latitude": number, "Longitude": number },
        "Rating": number,
        "Description": "string"
      }
    ],
    "Itinerary": [
      {
        "Day": number,
        "DayPlan": "string",
        "BestTimeToVisit": "string",
        "Schedule": [
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          }
        ]
      },
      {
        "Day": number,
        "DayPlan": "string",
        "BestTimeToVisit": "string",
        "Schedule": [
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          }
        ]
      },
      {
        "Day": number,
        "DayPlan": "string",
        "BestTimeToVisit": "string",
        "Schedule": [
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          },
          {
            "placeName": "string",
            "PlaceDetails": "string",
            "PlaceImageUrl": "string",
            "GeoCoordinates": { "Latitude": number, "Longitude": number },
            "ticketPricing": "string",
            "time": "string" - "string",
            "timeToTravel": "string",
            "rating": number,
            "TimeSpent": "string"
          }
        ]
      }
    ]
  }
}
Generate for:
Location: {location} 
Days: {totalDays}  
Travelers: {traveler}
Budget: {budget} 
`;