import { createContext, StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
// import './index.css'
import App from './App.jsx'
// import UserList from './components/usersList.jsx';
// import CustomSpinner from './components/CustomSpinner.jsx'
// import CustomNavbar from './components/CustomNavbar'
import 'bootstrap/dist/css/bootstrap.min.css';
// import CustomCarousel from './components/CustomCarousel.jsx';
// import FetchRecipes from './components/FetchRecipes.jsx';
// import Application from './Application.jsx';
import { BrowserRouter, Routes, Route } from "react-router";
import About from './components/About.jsx';
import Recipes from './components/Recipes.jsx';
import PageNotFound from './components/PageNotFound.jsx';

export const Waiter = createContext()

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Waiter value="Chicken Biryani">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/about" element={<About />} />
          <Route path="/recipes/:id" element={<Recipes />} />
          <Route path="*" element={<PageNotFound />} />
        </Routes>
      </BrowserRouter>,
    </Waiter>
    {/* <CustomNavbar/> */}
    {/* <CustomCarousel/> */}
    {/* <CustomSpinner/> */}
    {/* <FetchRecipes/> */}
    {/* <Application/> */}

    {/* <App /> */}
    {/* <UserList/> */}
  </StrictMode>,
)
