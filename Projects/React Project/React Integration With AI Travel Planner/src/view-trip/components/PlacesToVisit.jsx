import React from 'react'
import PlaceCardItem from './PlaceCardItem'

function PlacesToVisit(trip) {

    // console.log("TRIP FULL:", trip);
    // console.log("tripData:", trip?.trip?.tripData);
    // console.log("TravelPlan:", trip?.trip?.tripData?.TravelPlan);
    // console.log("Itinerary:", trip?.trip?.tripData?.TravelPlan?.Itinerary);

    const places = trip?.trip?.tripData?.TravelPlan?.Itinerary

    return (
        <div>
            <h2 className='font-bold text-lg'>Places To Visit</h2>

            <div>
                {places?.map((item, index) => (
                    <div key={index} className='mt-5'>
                        <h2 className='font-medium text-lg'>Day : {item?.Day}</h2>

                        <div className='grid md:grid-cols-2 gap-5'>
                            {item?.Schedule?.map((place, index) => (
                                <div key={index} className='my-3'>
                                    <h2 className='font-medium text-sm text-orange-600'>{place?.time}</h2>
                                    <PlaceCardItem place={place} />
                                </div>
                            ))}
                        </div>

                    </div>
                ))}
            </div>

        </div >
    )
}

export default PlacesToVisit
