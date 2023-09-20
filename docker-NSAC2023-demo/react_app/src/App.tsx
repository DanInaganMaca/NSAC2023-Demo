import React from 'react'
import { Button } from 'semantic-ui-react'
import './App.scss'

export const App = (props: {}) => {
  return (
    <div className='app'>
      <h1 className='app__title'>Hola mundo!</h1>
      <Button primary>Click Me</Button>
    </div>
  )
}
