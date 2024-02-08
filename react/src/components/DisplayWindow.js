import React from 'react';

function DisplayWindow({ outputDetails }) {
    return (
        <div>
            <h2 className='font-sans hover:font-serif'>Output:</h2>
            <div className="w-full h-56 focus:outline-none w-full border-2 border-black z-10 rounded-md px-4 py-2 hover:shadow transition duration-200 bg-white mt-2">
                {outputDetails && outputDetails.sentence}
            </div>
        </div>
    );
}

export default DisplayWindow;