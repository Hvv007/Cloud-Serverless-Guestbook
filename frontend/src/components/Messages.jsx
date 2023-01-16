import React from 'react'

function Messages(props) {
    return (
        <div className="flex flex-col justify-center items-center mx-5">
            <p className='text-lg'>
                Guest name: {props.message}
            </p>
            <p className='text-lg'>
                Message: {props.name}
            </p>
        </div>
    )
}

export default Messages