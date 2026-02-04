import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getPlaceImage } from "@/api/unsplash";


function Hotels(trip) {

  // console.log("TRIP FULL:", trip);
  // console.log("tripData:", trip?.trip?.tripData);
  // console.log("TravelPlan:", trip?.trip?.tripData?.TravelPlan);
  // console.log("HotelOptions:", trip?.trip?.tripData?.TravelPlan?.HotelOptions);

  const Hotels = trip?.trip?.tripData?.TravelPlan?.HotelOptions

  // This is Unsplash
  const hotelList = trip?.trip?.tripData?.TravelPlan?.HotelOptions;
  const [images, setImages] = useState({});

  useEffect(() => {
    if (!hotelList) return;

    const loadImages = async () => {
      const newImages = {};

      await Promise.all(
        hotelList.map(async (hotel) => {
          if (images[hotel.HotelName]) return;

          const img = await getPlaceImage(hotel.HotelName);
          newImages[hotel.HotelName] = img || "/placeholder.png";
        })
      );

      setImages(prev => ({ ...prev, ...newImages }));
    };

    loadImages();
  }, [hotelList]);


  return (
    <div>
      <h2 className='font-bold text-xl mt-5'>Hotel Recommendation</h2>

      <div className='grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-5'>
        {Hotels?.map((hotel, index) => (
          <Link to={'https://www.google.com/maps/search/?api=1&query=' + hotel?.HotelName + "," + hotel?.HotelAddress} target='_blank'>
            <div key={index} className='hover:scale-105 transition-all cursor-pointer'>

              {/* <img src='/placeholder.png' className='rounded-xl' /> */}

              <img
                src={images[hotel.HotelName] ? images[hotel.HotelName] : "/placeholder.png"}
                className="rounded-xl h-40 w-full object-cover"
                alt={hotel.HotelName}
              />

              <div className='my-2 flex flex-col gap-3'>
                <h2 className='font-medium text-black'>{hotel?.HotelName}</h2>
                <h2 className='text-xs text-gray-500'>📍 {hotel?.HotelAddress}</h2>
                <h2 className='text-xs text-black'>💰 {hotel?.Price}</h2>
                <h2 className='text-xs text-black'>⭐ {hotel?.Rating}</h2>
              </div>

            </div>
          </Link>

        ))}
      </div>

    </div >
  )
}

export default Hotels
