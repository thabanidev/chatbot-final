import React from 'react'
// clerk sign in and sign p
import { SignIn, SignedIn, UserButton } from '@clerk/nextjs'

function page() {
  return (
    <div className='flex flex-col gap-4 items-center justify-center h-screen p-20'>
      <h1 className='text-3xl text-center font-bold'>Welcome to the Customer Service AI Chatbot</h1>
      <p className='text-lg text-center'>This chatbot is designed to assist customers with their queries and provide them with the best possible service.</p>
      <div className='flex flex-col lg:flex-row gap-4'>
        <a href='/sign-in' className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'>
          Sign In
        </a>
        {/* outline  */}
        <a href='/sign-up' className=' hover:text-blue-500 text-white font-bold py-2 px-4 rounded underline'>
          Sign Up
        </a>
      </div>
    </div>
  )
}

export default page