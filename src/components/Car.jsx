import React from 'react'
import carImage from '../assets/f1-car.png'
import '../styles/Car.css'

const Car = (props) => {
  return (
    <img src={carImage} alt='F1 Car' className='car' style={props.style}/>
  )
}

export default Car
