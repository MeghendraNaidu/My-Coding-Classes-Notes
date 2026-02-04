import { Button } from '@/components/ui/button'
import { FaShare } from "react-icons/fa6";
import React, { useEffect, useState } from 'react'
import { getPlaceImage } from "@/api/unsplash";

function InfoSection({ trip }) {

    // This is Unsplash
    const [placeImg, setPlaceImg] = useState("/placeholder.png");

    const locationName = `${trip?.userSelection?.location?.address_line1 || ""} ${trip?.userSelection?.location?.address_line2 || ""}`;

    useEffect(() => {
        const loadImage = async () => {
            if (!locationName.trim()) return;

            const img = await getPlaceImage(locationName);
            if (img) setPlaceImg(img);
        };

        loadImage();
    }, [locationName]);


    return (
        <div>
            {/* <img src='/placeholder.png' className='h-[340px] w-full object-cover rounded-xl' /> */}

            {/* <img src={placeImg ? placeImg : '/placeholder.png'} className='h-[340px] w-full object-cover rounded-xl' /> */}
            
            <img src={placeImg} className='h-[340px] w-full object-cover rounded-xl'/>

            <div className='flex justify-between items-center'>
                <div className='my-5 flex flex-col gap-2'>
                    {/* <h2>{trip?.userSelection?.location?.address_line1}</h2> */}
                    <h2 className='font-bold text-2xl'>{trip?.userSelection?.location?.address_line1},{" "}{trip?.userSelection?.location?.address_line2}</h2>
                    <div className='flex gap-5'>
                        <h2 className='p-1 px-3 bg-gray-200 rounded-full text-gray-500 text-xs md:text-md'>📅 {trip?.userSelection?.noOfDays} Day</h2>
                        <h2 className='p-1 px-3 bg-gray-200 rounded-full text-gray-500 text-xs md:text-md'>💰 {trip?.userSelection?.budget} Budget</h2>
                        <h2 className='p-1 px-3 bg-gray-200 rounded-full text-gray-500 text-xs md:text-md'>🥂 No Of Traveler : {trip?.userSelection?.traveler}</h2>
                    </div>
                </div>
                <Button><FaShare /></Button>
            </div>
        </div>
    )
}

export default InfoSection
