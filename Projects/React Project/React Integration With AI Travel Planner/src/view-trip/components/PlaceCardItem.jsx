// import { Button } from '@/components/ui/button';
import React, { useEffect, useState } from 'react'
// import { FaMapLocationDot } from "react-icons/fa6";
import { Link } from 'react-router-dom';
import { getPlaceImage } from "@/api/unsplash";

function PlaceCardItem(place) {


    const placecard = place?.place

    // This is Unsplash
    const [placeImg, setPlaceImg] = useState('/placeholder.png');

    const placeName = place?.place?.placeName;

    useEffect(() => {
        const loadImage = async () => {
            if (!placeName) return;

            const img = await getPlaceImage(placeName);
            if (img) setPlaceImg(img);
        };

        loadImage();
    }, [placeName]);


    return (
        <Link to={'https://www.google.com/maps/search/?api=1&query=' + placecard?.placeName} target='_blank'>
            <div className='border rounded-xl p-3 mt-2 flex gap-5 hover:scale-105 transition-all hover:shadow-md cursor-pointer'>

                {/* <img src='/placeholder.png' className='w-[130px] h-[150px] rounded-xl' /> */}

                <img src={placeImg ? placeImg : '/placeholder.png'} className='w-[150px] h-[150px] rounded-xl object-cover' />

                <div>
                    <h2 className='font-bold text-lg text-black'>{placecard?.placeName}</h2>
                    <p className='text-sm text-gray-400'>{placecard?.PlaceDetails}</p>
                    <h2 className='mt-2 text-black'>🕙 {placecard?.timeToTravel}</h2>
                    {/* <Button size='sm'><FaMapLocationDot /></Button> */}
                </div>

            </div>
        </Link>
    )
}

export default PlaceCardItem
