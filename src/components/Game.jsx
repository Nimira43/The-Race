import React, { useEffect, useState } from 'react'
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

  useEffect(() => {
    const handleKeyDown = (e) => {
      e.preventDefault()
      setKeys((prevKeys) => ({
        ...prevKeys,
        [e.key]: true
      }))
    }
    const handleKeyUp = (e) => {
      e.preventDefault()
      setKeys((prevKeys) => ({
        ...prevKeys,
        [e.key]: false
      }))
    }
    window.addEventListener('keydown', handleKeyDown)
    window.addEventListener('keyup', handleKeyUp)

    return () => {
      window.removeEventListener('keydown', handleKeyDown)
      window.removeEventListener('keyup', handleKeyUp)
    }
  }, [])

  const playGame = () => {
    // Logic for car movement and collisions
  }

  return (
    <div className='game'>
      <div className="score">Score: {player.score}</div>
      <Car style={{ left: player.x, top: player.y }}/>
      {/* <RivalCar /> */}
    </div>
  )
}

export default Game
