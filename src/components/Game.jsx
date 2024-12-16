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
  const [keys, setKeys] = useState({ 
    ArrowUp: false, 
    ArrowDown: false, 
    ArrowLeft: false, 
    ArrowRight: false
  })

  return (
    <div className='game'>
      <h1>Game</h1>
      <div className="score">Score: {player.score}</div>
      <Car style={{ left: player.x, top: player.y }}/>
      <RivalCar />
    </div>
  )
}

export default Game
