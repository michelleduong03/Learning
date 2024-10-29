// document.getElementById('upload-button').addEventListener('click', async () => {
//     const fileInput = document.getElementById('file-input');
//     const file = fileInput.files[0];

//     if (!file) {
//         alert('Please select a file.');
//         return;
//     }

//     const reader = new FileReader();
//     reader.readAsDataURL(file);
//     reader.onload = async () => {
//         const base64Image = reader.result.split(',')[1]; // Extract base64 string

//         try {
//             const response = await fetch('https://0au0qyekq0.execute-api.us-west-2.amazonaws.com/dev/convert', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ body: base64Image }),
//             });

//             if (!response.ok) {
//                 throw new Error('Network response was not ok ' + response.statusText);
//             }

//             const result = await response.json();
//             displayImage(result.body); // Display the converted image
//         } catch (error) {
//             console.error('Error:', error);
//         }
//     };
// });

// function displayImage(base64String) {
//     const img = document.createElement('img');
//     img.src = 'data:image/jpeg;base64,' + base64String;
//     img.alt = 'Converted Image';
//     img.width = 300; // Set width to your preference

//     const resultDiv = document.getElementById('result');
//     resultDiv.innerHTML = ''; // Clear previous results
//     resultDiv.appendChild(img);
// }
document.getElementById('upload-button').addEventListener('click', async () => {
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select an image to upload.');
        return;
    }

    // Convert the image to base64
    const reader = new FileReader();
    reader.onloadend = async () => {
        const base64Image = reader.result.split(',')[1]; // Get base64 string without the header

        try {
            const response = await fetch('https://0au0qyekq0.execute-api.us-west-2.amazonaws.com/dev/conversion', {
                method: 'POST',
                body: JSON.stringify({ body: base64Image }),
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            alert(result.body);  // Display the result message
        } catch (error) {
            alert('Error: ' + error.message);
        }
    };
    reader.readAsDataURL(file);
});
