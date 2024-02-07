import React from 'react';

function DisplayWindow({ outputDetails }) {
    return (
        <div>
            <h2>Output:</h2>
            <div className="w-full h-56 bg-[#1e293b] rounded-md text-white font-normal text-sm overflow-y-auto">
                {outputDetails && outputDetails.sentence}
            </div>
        </div>
    );
}

export default DisplayWindow;