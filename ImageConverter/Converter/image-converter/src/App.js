import React, { useState } from 'react';
import './App.css';

function App() {
    const [image, setImage] = useState(null);
    const [convertedImage, setConvertedImage] = useState(null);
    const [message, setMessage] = useState('');

    const handleFileChange = (e) => {
        setImage(e.target.files[0]);
        setConvertedImage(null);
        setMessage('');
    };

    const handleSubmit = async (e) => {
      e.preventDefault();

      if (!image) {
          setMessage('Please select an image to convert.'); 
          return; 
      }
  
      const reader = new FileReader();
      reader.onloadend = async () => {
          const base64Image = reader.result.split(',')[1];
  
          try {
              const response = await fetch('https://hrqenyqyy6.execute-api.us-west-2.amazonaws.com/prod/convert', {
                  method: 'POST',
                  body: JSON.stringify({ body: base64Image }),
                  headers: {
                      'Content-Type': 'application/json',
                  },
              });
  
              const data = await response.json();
              console.log('API Response:', data); 
  
              if (!response.ok) {
                  throw new Error('Network response was not ok'); 
              }
  
              const base64String = data.body;
              setConvertedImage(base64String);
              setMessage('Image converted successfully!');
          } catch (error) {
              console.error('Error:', error); 
              setMessage('Error converting image: ' + error.message); 
          }
      };
  
      reader.readAsDataURL(image);
  };  

    return (
        <div className="container">
            <h1>Webp To Jpeg Image Converter</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" accept="image/webp" onChange={handleFileChange} />
                <button type="submit">Convert Image</button>
            </form>
            <div style={{ textAlign: 'center' }}>
              {message && <p style={{ color: convertedImage ? 'green' : 'red' }}>{message}</p>} 
            </div>
            {convertedImage && (
                <div>
                    <img src={`data:image/jpeg;base64,${convertedImage}`} alt="Converted" style={{ maxWidth: '100%', maxHeight: '400px' }} />

                    <div style={{ textAlign: 'center', marginTop: '10px' }}>
                      <a 
                        href={`data:image/jpeg;base64,${convertedImage}`} 
                        download="converted_image.jpg" 
                        style={{ display: 'inline-block', padding: '10px 20px', backgroundColor: '#5c6bc0', color: '#fff', textDecoration: 'none', borderRadius: '5px', fontSize: '16px', hover: '#3949ab' }}
                      >
                      Download Converted Image
                      </a>
                    </div>
                </div>
            )}
        </div>
    );
}

export default App;
