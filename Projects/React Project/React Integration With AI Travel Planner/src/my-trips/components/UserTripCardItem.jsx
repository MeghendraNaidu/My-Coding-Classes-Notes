import { getPlaceImage } from '@/api/unsplash';
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom';

function UserTripCardItem(trip) {

    const [placeImg, setPlaceImg] = useState("/placeholder.png");

    const locationName = `${trip?.trip?.userSelection?.location?.address_line1 || ""} ${trip?.trip?.userSelection?.location?.address_line2 || ""}`;

    useEffect(() => {
        const loadImage = async () => {
            if (!locationName.trim()) return;

            const img = await getPlaceImage(locationName);
            if (img) setPlaceImg(img);
        };

        loadImage();
    }, [locationName]);


    return (
        <Link to={'/view-trip/' + trip?.trip?.id}>
            <div className='hover:scale-105 transition-all'>
                {/* <img src='/placeholder.png' className='object-cover rounded-xl'/> */}

                <img src={placeImg} className='h-[200px] w-[250px] object-cover rounded-xl' />

                <div>
                    <h2 className='font-bold text-lg text-black'>{trip?.trip?.userSelection?.location?.address_line1},{" "}{trip?.trip?.userSelection?.location?.address_line2}</h2>
                    <h2 className='text-sm text-gray-500'>{trip?.trip?.userSelection?.noOfDays} Days trip {trip?.trip?.userSelection?.budget} Budget</h2>
                </div>
            </div>
        </Link>
    )
}

export default UserTripCardItem
