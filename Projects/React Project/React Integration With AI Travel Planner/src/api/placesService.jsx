import { geocodePlace, getPlaces } from "./geoapify";
import { getPlaceImage } from "./unsplash";

export const getPlacesWithImages = async (address) => {
  const geo = await geocodePlace(address);
  const { lat, lon } = geo.data.features[0].properties;

  const placesRes = await getPlaces(lat, lon);

  return Promise.all(
    placesRes.data.features.map(async (p) => {
      const name = p.properties.name;
      const image = await getPlaceImage(name);

      return {
        ...p.properties,
        image: image || "/placeholder.png",
      };
    })
  );
};
