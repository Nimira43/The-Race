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
  const [rivals, setRivals] = useState([])

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

  const startGame = () => { 
    setPlayer({ 
      ...player, 
      start: true, 
      score: 0 
    })
    setPlayer({ ...player, start: true, score: 0 })
    const initialRivals = [ 
      { x: Math.random() * 350, y: -100 }, 
      { x: Math.random() * 350, y: -300 }, 
      { x: Math.random() * 350, y: -500 } 
    ] 
    setRivals(initialRivals) 
    playGame() 
  }

  const playGame = () => {
    if (player.start) {
      let newPlayer = { ...player }
  
      if (keys.ArrowUp && newPlayer.y > 0) {
        newPlayer.y -= newPlayer.speed
      }
      if (keys.ArrowDown && newPlayer.y < window.innerHeight - 100) {
        newPlayer.y += newPlayer.speed
      }
      if (keys.ArrowLeft && newPlayer.x > 0) {
        newPlayer.x -= newPlayer.speed
      }
      if (keys.ArrowRight && newPlayer.x < 350) {
        newPlayer.x += newPlayer.speed
      }
  
      setPlayer(newPlayer)
    
      requestAnimationFrame(playGame)
    }
  }
  
  return (
    <div className="game"> 
      <div className="score">Score: {player.score}</div> 
      {!player.start && <button onClick={startGame}>Start Game</button>
      } 
      <Car style={{ left: player.x, top: player.y }} /> 
      {rivals.map((rival, index) => ( 
        <RivalCar key={index} style={{ left: rival.x, top: rival.y }} /> 
      ))} 
    </div>
  )
}

export default Game
