import React, { useState } from 'react'
import Car from './Car'
import RivalCar from './RivalCar'
import '../styles/Game.css'

const Game = () => {
  const [player, setPlayer] = useState({ 
    x: 0, 
    y: 0, 
    speed: 5, 
    score: 0
  })

  return (
    <div className='game-container'>
      <h1>Game</h1>
      <div className="score">Score: 50</div>
      <Car/>
      <RivalCar />
    </div>
  )
}

export default Game
