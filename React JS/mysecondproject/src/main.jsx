import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// import './index.css'
// import App from './App.jsx'
import 'bootstrap/dist/css/bootstrap.min.css';
import Description from './components/sample.jsx'
import CustomNavbar from './components/CustomNavbar.jsx'
import CustomCarousels from './components/CustomCarousels.jsx';
import CounterApp from './classComponents/CounterApp.jsx';


createRoot(document.getElementById('root')).render(
  <StrictMode>
  <CustomNavbar/>
  <CustomCarousels/>
  <CounterApp/>
  <Description/>
    {/* <h1>React is a JS Library which is used Build UI</h1> */}
    {/* <App /> */}
  </StrictMode>,
)
