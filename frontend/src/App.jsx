import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import react from 'react'
import './App.css'
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/protectedRoute"
import Home from "./pages/Home"


/* This is where to define how your app routing should be like */
function Logout(){
  localStorage.clear()
  return <Navigate to="/login"/>
}

/* when someone is registering, so that you dont send access token, just clear it up to work properly */
function RegisterAndLogout(){
  localStorage.clear()
  return <Register />
}
function App() {

  return (
   <BrowserRouter>
   <Routes>
    <Route
      path="/"
      element={
        <ProtectedRoute>{/*you cannot access home unless you have the access token and it is valid. This is only for people that are loggedin*/}
          <Home />
        </ProtectedRoute>
      }
    />
    <Route path="/login" element={<Login/>}/>
    <Route path="/logout" elemtent={<Logout/>}/>
    <Route path="/register" element={<RegisterAndLogout/>}/>
    <Route path="*" element={<NotFound/>}/>
   </Routes>
   </BrowserRouter>
  )
}

export default App
