import React from 'react'
import Car from './Car'
import RivalCar from './RivalCar'
import '../styles/Game.css'

const Game = () => {
  return (
    <div className='game-container'>
      <h1>Game</h1>
      <Car/>
      <RivalCar />
    </div>
  )
}

export default Game
