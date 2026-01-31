// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAj7c5DBOnKDZQAsXYvhBzHIgXlG7g1Zd8",
  authDomain: "my-react-ai-trip-planner.firebaseapp.com",
  projectId: "my-react-ai-trip-planner",
  storageBucket: "my-react-ai-trip-planner.firebasestorage.app",
  messagingSenderId: "583395235142",
  appId: "1:583395235142:web:fa27b28fa0579bfeb28147",
  measurementId: "G-3RR27LZH50"
};

// Initialize Firebase
export  const app = initializeApp(firebaseConfig);
export const db = getFirestore(app)
// const analytics = getAnalytics(app);