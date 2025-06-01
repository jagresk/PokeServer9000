import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
	fetch('http://localhost:5000/usage')
	  .then(res => res.json())
	  .then(setData)
  }, [])


  return (
   <div>
    <h1>Pokemon Usage Stats</h1>
    <pre>{JSON.stringify(data, null, 2)}</pre>
   </div>
  )
}

export default App
