import React from 'react'
import Input from './components/Input'

function App() {
  return (
    <div className=''>
      <div className='flex flex-col justify-center items-center my-10'>
          <h1 className='lg:text-4xl md:text-3xl sm:text-xl text-lg'> Guestbook </h1>
          <p className='lg:text-2xl md:text-xl sm:text-sm text-sm'> You can leave your message below</p>
      </div>
      <Input/>
    </div>
  )
}

export default App