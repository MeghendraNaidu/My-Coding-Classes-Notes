import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
// import './index.css'
// import App from './App.jsx'
// import UserList from './components/usersList.jsx';
// import CustomNavbar from './components/CustomNavbar.jsx'
// import CustomSpinner from './components/CustomSpinner.jsx'
// import CustomCarousels from './components/CustomCarousels.jsx'
import 'bootstrap/dist/css/bootstrap.min.css';
import Application from './Application.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
  {/* <CustomNavbar/> */}
  {/* <CustomSpinner/> */}
  {/* <CustomCarousels/> */}
  <Application/>

  {/* <App /> */}
  {/* <UserList/> */}
  </StrictMode>,
)
