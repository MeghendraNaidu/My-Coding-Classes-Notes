import React, { useEffect, useState } from 'react'
import axios from "axios";
import { Input } from '@/components/ui/input';
import { AI_PROMPT, SelectBudgetOptions, SelectTravelesList } from '@/constants/options';
import { Button } from '@/components/ui/button';
import { toast } from 'sonner';
import { chat } from '@/service/AIModal';

import { FcGoogle } from "react-icons/fc";
import { AiOutlineLoading3Quarters } from "react-icons/ai";

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { useGoogleLogin } from '@react-oauth/google';
import { doc, setDoc } from 'firebase/firestore';
import { db } from '@/service/firebaseConfig';
import { useNavigate } from 'react-router-dom';



function CreateTrip() {

  const [formData, setformData] = useState([])

  const [openDialog, setOpenDialog] = useState(false)

  const [loading, setLoading] = useState(false)

  const navigate = useNavigate()

  const handleInputChange = (name, value) => {
    setformData({
      ...formData,
      [name]: value
    })
  }
  useEffect(() => {
    console.log(formData)
  }, [formData])

  const login = useGoogleLogin({
    onSuccess: (codeResp) => GetUserProfile(codeResp),
    onError: (error) => console.log(error)
  })

  const OnGenerateTrip = async () => {

    const user = localStorage.getItem("user")

    if (!user) {
      setOpenDialog(true)
      return
    }

    if (formData?.noOfDays > 9 && !formData?.location || !formData?.budget || !formData?.traveler) {
      toast("Please fill all the Detailes.")
      return;
    }
    // console.log(formData)

    setLoading(true)

    const FINAL_PROMPT = AI_PROMPT
      .replace("{location}", `${formData?.location?.address_line1}, ${formData?.location?.address_line2}`)
      .replace("{totalDays}", formData?.noOfDays)
      .replace("{traveler}", formData?.traveler)
      .replace("{budget}", formData?.budget)

    // console.log(FINAL_PROMPT)

    // This is Onriginal One

    const result = await chat.sendMessage({
      message: FINAL_PROMPT
    });
    let text = result.text;
    text = text.replace(/```json/g, "").replace(/```/g, "").trim();

    const tripPlan = JSON.parse(text);

    console.log(tripPlan);
    setLoading(false)
    SaveAiTrip(tripPlan)

  }

  const SaveAiTrip = async (TripData) => {
    setLoading(true)
    const user = JSON.parse(localStorage.getItem("user"))
    const docId = Date.now().toString()
    await setDoc(doc(db, "AITrips", docId), {
      userSelection: formData,
      tripData: TripData,
      userEmail: user?.email,
      id: docId
    });
    setLoading(false)
    navigate('/view-trip/' + docId)
  }

  const GetUserProfile = (tokenInfo) => {
    axios.get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${tokenInfo?.access_token}`, {
      headers: {
        Authorization: `Bearer ${tokenInfo?.access_token}`,
        Accept: `Application/json`
      }
    }).then((resp) => {
      console.log(resp)
      localStorage.setItem("user", JSON.stringify(resp.data))
      setOpenDialog(false)
      OnGenerateTrip()
    })
  }

  // This code is for Maps and places Api fetch
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
                      // console.log(place.properties)
                      handleInputChange("location", place.properties)
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

          <Input placeholder={'Ex.3'} type="number"
            onChange={(e) => handleInputChange("noOfDays", e.target.value)}
          />
        </div>

      </div>

      <div>
        <h2 className='text-xl my-3 font-medium'>What is your Budget?</h2>
        <div className='grid grid-cols-3 gap-4 mt-5'>
          {SelectBudgetOptions.map((item, index) => (
            <div key={index}
              onClick={() => handleInputChange("budget", item.title)}
              className={`p-4 border rounded-lg hover:shadow-lg cursor-pointer
                ${formData?.budget == item.title && 'shadow-lg border-black'}
              `}>
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
            <div key={index}
              onClick={() => handleInputChange("traveler", item.people)}
              className={`p-4 border rounded-lg hover:shadow-lg cursor-pointer
                ${formData?.traveler == item.people && 'shadow-lg border-black'}
              `}>
              <h2 className='text-4xl'>{item.icon}</h2>
              <h2 className='font-bold text-lg'>{item.title}</h2>
              <h2 className='text-sm text-gray-500'>{item.desc}</h2>
            </div>
          ))}
        </div>
      </div>

      <div className='my-10 flex justify-end'>
        <Button
          disabled={loading}
          onClick={OnGenerateTrip}>
          {loading ?
            <AiOutlineLoading3Quarters className='h-7 w-7 animate-spin' /> : "Generate Trip"
          }
        </Button>
      </div>

      <Dialog open={openDialog}>
        <DialogContent>
          <DialogHeader>
            <DialogDescription>
              <img src='/logo.svg' />
              <h2 className='font-bold text-lg mt-7'>Sign In With Google</h2>
              <p>Sign in to the App with Google authentication securely.</p>
              <Button
                onClick={login}
                className="w-full mt-5 flex gap-5 items-center">
                <FcGoogle className='h-7 w-7' />
                Sign In With Google
              </Button>
            </DialogDescription>
          </DialogHeader>
        </DialogContent>
      </Dialog>


    </div>
  )
}

export default CreateTrip
