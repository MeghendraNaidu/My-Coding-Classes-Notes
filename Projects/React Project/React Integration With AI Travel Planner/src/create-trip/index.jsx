import React, { useState } from 'react'
// import GooglePlacesAutocomplete from 'react-google-places-autocomplete'
import axios from "axios";
import { Input } from '@/components/ui/input';
import { SelectBudgetOptions, SelectTravelesList } from '@/constants/options';
import { Button } from '@/components/ui/button';



function CreateTrip() {
  // const [place, setPlace] = useState()

  const[formData, setformData] = useState([])

  const handleInputChange = (name, value){
    
  }

  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  // eslint-disable-next-line no-unused-vars
  const [selectedPlace, setSelectedPlace] = useState(null);

  const GEOAPIFY_KEY = import.meta.env.VITE_GEOAPIFY_API_KEY;

  const fetchPlaces = async (text) => {
    if (!text) return setSuggestions([]);

    try {
      const res = await axios.get(
        `https://api.geoapify.com/v1/geocode/autocomplete`,
        {
          params: {
            text,
            apiKey: GEOAPIFY_KEY,
            limit: 10,
          },
        }
      );

      setSuggestions(res.data.features);
    } catch (err) {
      console.error("Geoapify error:", err);
    }
  };


  return (
    <div className='sm:px-10 md:px-32 lg:px-56 xl:px-60 px-5 mt-10 mb-10'>

      <h2 className='font-bold text-3xl'>Tell us your Travel Preferences 🏕️🌴</h2>
      <p className='mt-3 text-gray-500 text-[18px]'>Just provide some basic information, and our trip planner will generate a customized itinerary based on your Preferences.</p>

      <div className='mt-15 flex flex-col gap-10'>
        <div>
          <h2 className='text-xl my-3 font-medium'>What is your destination of choice?</h2>

          {/* <GooglePlacesAutocomplete
            apiKey={import.meta.env.GEOAPIFY_API_KEY}
            selectProps={{
              place,
              onChange: (v) => { setPlace(v); console.log(v) }
            }}
          /> */}
          <div className="relative">
            <input type="text" value={query} onChange={(e) => {
              setQuery(e.target.value);
              fetchPlaces(e.target.value);
            }}
              placeholder="Enter a city or place"
              className="w-full p-3 border rounded-lg"
            />

            {suggestions.length > 0 && (
              <div className="absolute z-10 w-full border rounded-lg mt-1 bg-white shadow-md max-h-60 overflow-y-auto">
                {suggestions.map((place) => (
                  <div key={place.properties.place_id} className="p-2 hover:bg-gray-100 cursor-pointer"
                    onClick={() => {
                      setSelectedPlace(place);
                      console.log(place.properties)
                      setQuery(place.properties.formatted);
                      setSuggestions([]);
                    }}>
                    {place.properties.formatted}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        <div>
          <h2 className='text-xl my-3 font-medium'>How many days are you planning your trip?</h2>

          <Input placeholder={'Ex.3'} type="number" />
        </div>

      </div>

      <div>
        <h2 className='text-xl my-3 font-medium'>What is your Budget?</h2>
        <div className='grid grid-cols-3 gap-4 mt-5'>
          {SelectBudgetOptions.map((item, index) => (
            <div key={index} className='p-4 border rounded-lg hover:shadow-lg cursor-pointer'>
              <h2 className='text-4xl'>{item.icon}</h2>
              <h2 className='font-bold text-lg'>{item.title}</h2>
              <h2 className='text-sm text-gray-500'>{item.desc}</h2>
            </div>
          ))}
        </div>
      </div>

      <div>
        <h2 className='text-xl my-3 font-medium'>Who do you plan on traveling with on your next adventure?</h2>
        <div className='grid grid-cols-3 gap-4 mt-5'>
          {SelectTravelesList.map((item, index) => (
            <div key={index} className='p-4 border rounded-lg hover:shadow-lg cursor-pointer'>
              <h2 className='text-4xl'>{item.icon}</h2>
              <h2 className='font-bold text-lg'>{item.title}</h2>
              <h2 className='text-sm text-gray-500'>{item.desc}</h2>
            </div>
          ))}
        </div>
      </div>

      <div className='my-10 flex justify-end'>
        <Button>Generate Trip</Button>
      </div>
      

    </div>
  )
}

export default CreateTrip



// import React, { useState } from "react";
// import axios from "axios";

// function CreateTrip() {
// const [query, setQuery] = useState("");
// const [suggestions, setSuggestions] = useState([]);
// const [selectedPlace, setSelectedPlace] = useState(null);

// const GEOAPIFY_KEY = import.meta.env.VITE_GEOAPIFY_API_KEY;

// const fetchPlaces = async (text) => {
//   if (!text) return setSuggestions([]);

//   try {
//     const res = await axios.get(
//       `https://api.geoapify.com/v1/geocode/autocomplete`,
//       {
//         params: {
//           text,
//           apiKey: GEOAPIFY_KEY,
//           limit: 5,
//         },
//       }
//     );

//     setSuggestions(res.data.features);
//   } catch (err) {
//     console.error("Geoapify error:", err);
//   }
// };

//   return (
//     <div className="sm:px-10 md:px-32 lg:px-56 xl:px-60 px-5 mt-10">
//       <h2 className="font-bold text-3xl">Tell us your Travel Preferences</h2>
//       <p className="mt-3 text-gray-500 text-[18px]">
//         Just provide some basic information, and our trip planner will generate
//         a customized itinerary.
//       </p>

//       <div className="mt-10">
//         <h2 className="text-xl my-3 font-medium">
//           What is your destination of choice?
//         </h2>

//         {/* INPUT */}
//         <input
//           type="text"
//           value={query}
//           onChange={(e) => {
//             setQuery(e.target.value);
//             fetchPlaces(e.target.value);
//           }}
//           placeholder="Enter a city or place"
//           className="w-full p-3 border rounded-lg"
//         />

//         {/* DROPDOWN */}
//         {suggestions.length > 0 && (
//           <div className="border rounded-lg mt-2 bg-white shadow-md">
//             {suggestions.map((place) => (
//               <div
//                 key={place.properties.place_id}
//                 className="p-2 hover:bg-gray-100 cursor-pointer"
//                 onClick={() => {
//                   setSelectedPlace(place);
//                   console.log(place)
//                   setQuery(place.properties.formatted);
//                   setSuggestions([]);
//                 }}
//               >
//                 {place.properties.formatted}
//               </div>
//             ))}
//           </div>
//         )}
//       </div>
//     </div>
//   );
// }

// export default CreateTrip;
