import React from 'react'
import '../styles/Car.css'

const Car = (props) => {
  return (
    <img src='../assets/f1-car.png' alt='F1 Car' className='car' style={props.style}/>
  )
}

export default Car
