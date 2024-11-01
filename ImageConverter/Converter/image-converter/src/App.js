import React, { useState } from 'react';
import './App.css';

function App() {
    const [image, setImage] = useState(null);
    const [convertedImage, setConvertedImage] = useState(null);
    const [message, setMessage] = useState('');

    const handleFileChange = (e) => {
        setImage(e.target.files[0]); // set the selected image file
        setConvertedImage(null); // reset converted image
        setMessage(''); // reset message
    };

    const handleSubmit = async (e) => {
      e.preventDefault(); // prevent the default form submission

      // error checking if an image is not selected
      if (!image) {
          setMessage('Please select an image to convert.'); 
          return; 
      }
  
      const reader = new FileReader(); // FileReader to read the image file
      reader.onloadend = async () => {
          const base64Image = reader.result.split(',')[1]; // extract the Base64 string
  
          try {
              const response = await fetch('https://hrqenyqyy6.execute-api.us-west-2.amazonaws.com/prod/convert', {
                  method: 'POST',
                  body: JSON.stringify({ body: base64Image }), // send Base64 image to the API
                  headers: {
                      'Content-Type': 'application/json',
                  },
              });
  
              // response to the console for debugging
              const data = await response.json(); // parse the JSON response
              console.log('API Response:', data); 
  
              if (!response.ok) {
                  throw new Error('Network response was not ok'); 
              }
  
              // extract the base64 image from the body of the response
              const base64String = data.body; // extract the base64 string
              setConvertedImage(base64String); // set the converted image 
              setMessage('Image converted successfully!');
          } catch (error) {
              console.error('Error:', error); 
              setMessage('Error converting image: ' + error.message); 
          }
      };
  
      reader.readAsDataURL(image); // read the selected image as a Data URL
  };  

    return (
        <div>
            <h1>Image Converter</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" accept="image/webp" onChange={handleFileChange} />
                <button type="submit">Convert Image</button>
            </form>
            {message && <p style={{ color: convertedImage ? 'green' : 'red' }}>{message}</p>} 
            {convertedImage && (
                <div>
                    <img src={`data:image/jpeg;base64,${convertedImage}`} alt="Converted" style={{ maxWidth: '100%', maxHeight: '400px' }} />
                    <h2>Base64 Encoded JPEG String:</h2>
                    <textarea 
                        readOnly 
                        value={`data:image/jpeg;base64,${convertedImage}`} 
                        rows={5} 
                        style={{ width: '100%', fontFamily: 'monospace', whiteSpace: 'pre', overflow: 'auto' }} 
                    />
                </div>
            )}
        </div>
    );
}

export default App;
